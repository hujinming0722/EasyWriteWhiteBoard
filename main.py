#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
全屏叠加式白板应用
核心功能：PPT叠加使用、悬浮窗工具、形状绘制、翻页清屏、橡皮擦双击交互
"""

import sys
import time
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QColorDialog, QInputDialog, QMessageBox, QLayout, QButtonGroup, QFrame,
    QSizePolicy, QMenu
)
from PySide6.QtGui import (
    QPainter, QPen, QColor, QPixmap, QMouseEvent, QPaintEvent, 
    QKeyEvent, QPainterPath, QCursor, QFont, QIcon
)
from PySide6.QtCore import (
    Qt, QPoint, QRect, QTimer, QEvent, QSize, 
    QCoreApplication, QEventLoop
)
from ui.Ui_mainui import Ui_MainWindow


class DrawingBoard(QWidget):
    """绘图板组件"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        # 绘图状态
        self.drawing = False
        self.current_tool = "pen"  # 当前工具：pen, line, rect, circle, ellipse, eraser
        self.start_point = QPoint()
        self.end_point = QPoint()
        self.last_point = QPoint()
        
        # 绘图属性
        self.pen_color = QColor(255, 0, 0)  # 默认红色
        self.pen_width = 5  # 默认粗细
        
        # 初始化绘图缓存
        screen_geometry = QApplication.primaryScreen().geometry()
        self.pixmap = QPixmap(screen_geometry.width(), screen_geometry.height())
        self.pixmap.fill(Qt.transparent)  # 透明背景
        
        # 设置焦点策略
        self.setFocusPolicy(Qt.NoFocus)
    
    def resizeEvent(self, event):
        """窗口大小改变时，重新调整绘图缓存"""
        screen_geometry = QApplication.primaryScreen().geometry()
        new_pixmap = QPixmap(screen_geometry.width(), screen_geometry.height())
        new_pixmap.fill(Qt.transparent)  # 透明背景
        
        # 复制旧内容到新缓存
        if not self.pixmap.isNull():
            painter = QPainter(new_pixmap)
            painter.drawPixmap(0, 0, self.pixmap)
            painter.end()
        
        self.pixmap = new_pixmap
        super().resizeEvent(event)
    
    def paintEvent(self, event):
        """绘制事件"""
        painter = QPainter(self)
        
        # 绘制缓存内容
        if not self.pixmap.isNull():
            painter.drawPixmap(0, 0, self.pixmap)
        
        # 实时预览（拖动时）
        if self.drawing and self.current_tool != "pen":
            self.draw_preview(painter)
    
    def draw_preview(self, painter):
        """绘制实时预览"""
        pen = QPen(self.pen_color, self.pen_width, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        pen.setStyle(Qt.DashLine)  # 虚线预览
        painter.setPen(pen)
        
        # 根据当前工具绘制不同形状的预览
        if self.current_tool == "line":
            painter.drawLine(self.start_point, self.end_point)
        elif self.current_tool == "rect":
            painter.drawRect(self.get_rect())
        elif self.current_tool == "circle":
            radius = min(abs(self.end_point.x() - self.start_point.x()), 
                        abs(self.end_point.y() - self.start_point.y()))
            painter.drawEllipse(self.start_point, radius, radius)
        elif self.current_tool == "ellipse":
            painter.drawEllipse(self.get_rect())
    
    def get_rect(self):
        """获取矩形区域"""
        x = min(self.start_point.x(), self.end_point.x())
        y = min(self.start_point.y(), self.end_point.y())
        width = abs(self.end_point.x() - self.start_point.x())
        height = abs(self.end_point.y() - self.start_point.y())
        return QRect(x, y, width, height)
    
    def mousePressEvent(self, event):
        """鼠标按下事件"""
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.start_point = event.position().toPoint()
            self.end_point = event.position().toPoint()
            self.last_point = event.position().toPoint()
    
    def mouseMoveEvent(self, event):
        """鼠标移动事件"""
        if event.buttons() & Qt.LeftButton and self.drawing:
            self.end_point = event.position().toPoint()
            
            # 画笔模式下实时绘制
            if self.current_tool == "pen":
                painter = QPainter(self.pixmap)
                pen = QPen(self.pen_color, self.pen_width, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
                painter.setPen(pen)
                painter.drawLine(self.last_point, self.end_point)
                painter.end()
                self.last_point = self.end_point
            
            self.update()
    
    def mouseReleaseEvent(self, event):
        """鼠标释放事件"""
        if event.button() == Qt.LeftButton and self.drawing:
            self.drawing = False
            self.end_point = event.position().toPoint()
            
            # 绘制最终图形（非画笔工具）
            if self.current_tool != "pen":
                painter = QPainter(self.pixmap)
                
                # 设置画笔属性
                if self.current_tool == "eraser":
                    # 橡皮擦使用白色
                    pen = QPen(QColor(255, 255, 255), self.pen_width, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
                else:
                    pen = QPen(self.pen_color, self.pen_width, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
                
                painter.setPen(pen)
                
                # 根据工具绘制不同形状
                if self.current_tool == "line":
                    painter.drawLine(self.start_point, self.end_point)
                elif self.current_tool == "rect":
                    painter.drawRect(self.get_rect())
                elif self.current_tool == "circle":
                    radius = min(abs(self.end_point.x() - self.start_point.x()), 
                                abs(self.end_point.y() - self.start_point.y()))
                    painter.drawEllipse(self.start_point, radius, radius)
                elif self.current_tool == "ellipse":
                    painter.drawEllipse(self.get_rect())
                elif self.current_tool == "eraser":
                    painter.drawLine(self.start_point, self.end_point)
                
                painter.end()
            
            self.update()
    
    def clear(self):
        """清空绘图板"""
        if not self.pixmap.isNull():
            self.pixmap.fill(Qt.transparent)
            self.update()
    
    def set_tool(self, tool):
        """设置当前工具"""
        self.current_tool = tool
    
    def set_pen_color(self, color):
        """设置画笔颜色"""
        self.pen_color = color
    
    def set_pen_width(self, width):
        """设置画笔粗细"""
        self.pen_width = width





class MainWindow(QMainWindow, Ui_MainWindow):
    """主窗口"""
    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        
        # 初始化UI
        self.setupUi(self)
        
        # 创建绘图区域
        self.drawing_board = DrawingBoard(self)
        
        # 替换默认的drawing_board为自定义组件
        drawing_board_layout = self.verticalLayout
        if drawing_board_layout:
            # 移除原有的绘图区域
            old_board = self.centralwidget.findChild(QWidget, "drawing_board")
            if old_board:
                drawing_board_layout.removeWidget(old_board)
                old_board.deleteLater()
            # 添加自定义绘图区域
            drawing_board_layout.insertWidget(0, self.drawing_board)
        
        # 创建悬浮工具窗口
        self.create_float_tool_window()
        
        # 清屏按钮定时器
        self.clearBtn_timer = QTimer(self)
        self.clearBtn_timer.setSingleShot(True)
        self.clearBtn_timer.timeout.connect(self.hide_clear_button)
        
        # 绑定信号和槽
        self.bind_signals()
        
        # 显示窗口
        self.showFullScreen()
        self.float_tool_widget.show()
    
    def setupUi(self, MainWindow):
        """设置UI"""
        # 设置主窗口
        MainWindow.resize(1920, 1080)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        
        # 创建中央部件和绘图区域
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.setCentralWidget(self.centralwidget)
        
        # 创建主布局
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        
        # 添加清屏按钮
        self.clearBtn = QPushButton(self.centralwidget)
        self.clearBtn.setObjectName(u"clearBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearBtn.sizePolicy().hasHeightForWidth())
        self.clearBtn.setSizePolicy(sizePolicy)
        self.clearBtn.setGeometry(QRect(910, 1000, 100, 50))
        self.clearBtn.setMaximumSize(QSize(100, 50))
        self.clearBtn.setVisible(False)
        self.clearBtn.setStyleSheet(u"QPushButton {\n"""
"    background-color: rgba(60, 60, 60, 0.9);\n"""
"    color: white;\n"""
"    border-radius: 10px;\n"""
"    font-size: 16px;\n"""
"}\n"""
"QPushButton:hover {\n"""
"    background-color: rgba(80, 80, 80, 0.9);\n"""
"}\n"""
"QPushButton:pressed {\n"""
"    background-color: rgba(100, 100, 100, 0.9);\n"""
"}")
        self.clearBtn.setText("清屏")
        
        self.verticalLayout.addWidget(self.clearBtn)
    
    def create_float_tool_window(self):
        """创建悬浮工具窗口"""
        # 创建悬浮工具窗口
        self.float_tool_widget = QWidget()
        self.float_tool_widget.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.float_tool_widget.setAttribute(Qt.WA_TranslucentBackground, True)
        self.float_tool_widget.setStyleSheet("background-color: rgba(40, 40, 40, 0.85); border-radius: 12px;")
        
        # 创建悬浮窗口布局 - 改为水平布局
        float_layout = QHBoxLayout(self.float_tool_widget)
        float_layout.setSpacing(15)
        float_layout.setContentsMargins(10, 10, 10, 10)
        
        # 添加所有工具按钮
        buttons = [
            ("btnPen", "P\n画笔", True),
            ("btnLine", "L\n直线", True),
            ("btnRect", "R\n矩形", True),
            ("btnCircle", "C\n圆形", True),
            ("btnEllipse", "O\n椭圆", True),
        ]
        
        # 创建按钮组用于互斥
        tool_group = QButtonGroup(self)
        
        # 添加绘图工具按钮
        icon_map = {
            "btnPen": "ui/icons/pen.png",
            "btnLine": "ui/icons/arrow.png",  # 使用箭头图标代替直线
            "btnRect": "ui/icons/correction.png",  # 使用修正图标代替矩形
            "btnCircle": "ui/icons/settings.png",  # 使用设置图标代替圆形
            "btnEllipse": "ui/icons/save.png",  # 使用保存图标代替椭圆
            "btnEraser": "ui/icons/eraser.png",
            "btnPPTPrev": "ui/icons/minimize.png",  # 使用最小化图标代替上一页
            "btnPPTNext": "ui/icons/minimize.png",  # 使用最小化图标代替下一页
            "btnExit": "ui/icons/exit.png"
        }
        
        for name, text, checkable in buttons:
            btn = QPushButton()
            btn.setObjectName(name)
            btn.setMinimumSize(40, 40)
            btn.setMaximumSize(40, 40)
            btn.setStyleSheet("QPushButton { background-color: rgba(60, 60, 60, 0.7); color: white; border-radius: 8px; text-align: center; } QPushButton:hover { background-color: rgba(80, 80, 80, 0.7); } QPushButton:pressed, QPushButton:checked { background-color: rgba(100, 100, 100, 0.7); }")
            btn.setCheckable(checkable)
            
            # 设置图标
            if name in icon_map:
                icon_path = icon_map[name]
                btn.setIcon(QIcon(icon_path))
                btn.setIconSize(QSize(24, 24))  # 设置图标大小
            
            if checkable:
                tool_group.addButton(btn)
            float_layout.addWidget(btn)
        
        # 添加分隔线
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("background-color: rgba(80, 80, 80, 0.5);")
        float_layout.addWidget(line)
        
        # 添加分隔线
        line2 = QFrame()
        line2.setFrameShape(QFrame.VLine)
        line2.setFrameShadow(QFrame.Sunken)
        line2.setStyleSheet("background-color: rgba(80, 80, 80, 0.5);")
        float_layout.addWidget(line2)
        
        # 添加橡皮擦按钮
        eraser_btn = QPushButton()
        eraser_btn.setObjectName("btnEraser")
        eraser_btn.setMinimumSize(40, 40)
        eraser_btn.setMaximumSize(40, 40)
        eraser_btn.setStyleSheet("QPushButton { background-color: rgba(60, 60, 60, 0.7); color: white; border-radius: 8px; text-align: center; } QPushButton:hover { background-color: rgba(80, 80, 80, 0.7); } QPushButton:pressed, QPushButton:checked { background-color: rgba(100, 100, 100, 0.7); }")
        eraser_btn.setCheckable(True)
        
        # 设置图标
        if "btnEraser" in icon_map:
            icon_path = icon_map["btnEraser"]
            eraser_btn.setIcon(QIcon(icon_path))
            eraser_btn.setIconSize(QSize(24, 24))
        
        tool_group.addButton(eraser_btn)
        float_layout.addWidget(eraser_btn)
        
        # 添加分隔线
        line3 = QFrame()
        line3.setFrameShape(QFrame.VLine)
        line3.setFrameShadow(QFrame.Sunken)
        line3.setStyleSheet("background-color: rgba(80, 80, 80, 0.5);")
        float_layout.addWidget(line3)
        
        # 添加PPT控制和退出按钮
        control_buttons = [
            ("btnPPTPrev", "上页", False),
            ("btnPPTNext", "下页", False),
            ("btnExit", "退出", False),
        ]
        
        for name, text, checkable in control_buttons:
            btn = QPushButton()
            btn.setObjectName(name)
            btn.setMinimumSize(40, 40)
            btn.setMaximumSize(40, 40)
            btn.setStyleSheet("QPushButton { background-color: rgba(60, 60, 60, 0.7); color: white; border-radius: 8px; } QPushButton:hover { background-color: rgba(80, 80, 80, 0.7); } QPushButton:pressed { background-color: rgba(100, 100, 100, 0.7); }")
            btn.setCheckable(checkable)
            
            # 设置图标
            if name in icon_map:
                icon_path = icon_map[name]
                btn.setIcon(QIcon(icon_path))
                btn.setIconSize(QSize(24, 24))
            
            float_layout.addWidget(btn)
        
        # 设置悬浮窗口大小和位置 - 调整为底部横向排列
        screen_geometry = QApplication.primaryScreen().geometry()
        window_width = 600  # 增加宽度以适应水平排列
        window_height = 60  # 减小高度
        x_pos = (screen_geometry.width() - window_width) // 2  # 居中显示
        y_pos = screen_geometry.height() - window_height - 50  # 距离底部50像素
        self.float_tool_widget.setGeometry(x_pos, y_pos, window_width, window_height)
        
        # 查找所有按钮并绑定信号
        for name in ["btnPen", "btnLine", "btnRect", "btnCircle", "btnEllipse", "btnEraser", "btnPPTPrev", "btnPPTNext", "btnExit"]:
            # 查找按钮
            btn = None
            for child in self.float_tool_widget.findChildren(QPushButton):
                if child.objectName() == name:
                    btn = child
                    break
            
            if btn:
                setattr(self, name, btn)
    
    def bind_signals(self):
        """绑定信号和槽"""
        # 确保所有按钮都存在
        buttons = [
            'btnPen', 'btnLine', 'btnRect', 'btnCircle', 'btnEllipse',
            'btnEraser', 'btnPPTPrev', 'btnPPTNext', 'btnExit'
        ]
        
        for button_name in buttons:
            button = getattr(self, button_name, None)
            if not button:
                print(f"警告: 找不到按钮 {button_name}")
                continue
                
            # 绘图工具按钮信号
            if button_name == 'btnPen':
                # 为画笔按钮添加右键菜单功能和双击功能
                button.clicked.connect(lambda: self.set_tool("pen"))
                button.setContextMenuPolicy(Qt.CustomContextMenu)
                button.customContextMenuRequested.connect(self.show_pen_context_menu)
                # 添加双击事件处理
                button.installEventFilter(self)
            elif button_name == 'btnLine':
                button.clicked.connect(lambda: self.set_tool("line"))
            elif button_name == 'btnRect':
                button.clicked.connect(lambda: self.set_tool("rect"))
            elif button_name == 'btnCircle':
                button.clicked.connect(lambda: self.set_tool("circle"))
            elif button_name == 'btnEllipse':
                button.clicked.connect(lambda: self.set_tool("ellipse"))
            elif button_name == 'btnEraser':
                button.clicked.connect(lambda: self.set_tool("eraser"))
            
            # PPT控制按钮信号
            elif button_name == 'btnPPTPrev':
                button.clicked.connect(lambda: self.simulate_ppt_key(Qt.Key_Left))
            elif button_name == 'btnPPTNext':
                button.clicked.connect(lambda: self.simulate_ppt_key(Qt.Key_Right))
            
            # 退出按钮信号
            elif button_name == 'btnExit':
                button.clicked.connect(self.exit_fullscreen)
        
        # 清屏按钮信号
        if hasattr(self, 'clearBtn'):
            self.clearBtn.clicked.connect(self.clear_drawing)
    
    def eventFilter(self, obj, event):
        """事件过滤器，用于处理按钮的双击事件"""
        if event.type() == QEvent.MouseButtonDblClick:
            # 检查是否是画笔按钮
            if obj.objectName() == 'btnPen':
                # 双击画笔按钮时显示子功能菜单
                self.show_pen_context_menu(event.position().toPoint())
                return True  # 事件已处理
        return super().eventFilter(obj, event)
    
    def set_tool(self, tool):
        """设置当前绘图工具"""
        self.current_tool = tool
        if hasattr(self, 'drawing_board'):
            self.drawing_board.set_tool(tool)
        print(f"切换到工具: {tool}")
    
    def choose_color(self):
        """选择颜色"""
        color = QColorDialog.getColor()
        if color.isValid():
            self.pen_color = color
            if hasattr(self, 'drawing_board'):
                self.drawing_board.set_pen_color(color)
            print(f"选择颜色: {color.name()}")
    
    def set_pen_width(self):
        """设置画笔粗细"""
        width, ok = QInputDialog.getInt(self, "设置画笔粗细", "请输入画笔粗细(1-20):", self.pen_width, 1, 20, 1)
        if ok:
            self.pen_width = width
            if hasattr(self, 'drawing_board'):
                self.drawing_board.set_pen_width(width)
            print(f"设置画笔粗细为: {width}")
    
    def show_pen_context_menu(self, position):
        """显示画笔上下文菜单"""
        menu = QMenu()
        color_action = menu.addAction("选择颜色")
        width_action = menu.addAction("设置粗细")
        
        # 连接动作到相应的处理方法
        color_action.triggered.connect(self.choose_color)
        width_action.triggered.connect(self.set_pen_width)
        
        # 在按钮位置显示菜单
        sender = self.sender()
        menu.exec(sender.mapToGlobal(position))
    
    def clear_drawing(self):
        """清空画布"""
        if hasattr(self, 'drawing_board'):
            self.drawing_board.clear()
            print("画布已清空")
    
    def hide_clear_button(self):
        """隐藏清屏按钮"""
        self.clearBtn.hide()
    
    def exit_fullscreen(self):
        """退出全屏"""
        self.close()
        print("退出全屏")
    
    def keyPressEvent(self, event):
        """键盘事件"""
        if event.key() == Qt.Key_Escape:
            # Esc键退出全屏
            self.exit_fullscreen()
        elif event.key() in (Qt.Key_Left, Qt.Key_Up):
            # 左/上箭头键：PPT上一页
            self.simulate_ppt_key(Qt.Key_Left)
        elif event.key() in (Qt.Key_Right, Qt.Key_Down):
            # 右/下箭头键：PPT下一页
            self.simulate_ppt_key(Qt.Key_Right)
        elif event.key() == Qt.Key_P:
            # P键：画笔工具
            self.set_tool("pen")
        elif event.key() == Qt.Key_L:
            # L键：直线工具
            self.set_tool("line")
        elif event.key() == Qt.Key_R:
            # R键：矩形工具
            self.set_tool("rect")
        elif event.key() == Qt.Key_C:
            # C键：圆形工具
            self.set_tool("circle")
        elif event.key() == Qt.Key_O:
            # O键：椭圆工具
            self.set_tool("ellipse")
        elif event.key() == Qt.Key_E:
            # E键：橡皮擦工具
            self.set_tool("eraser")
    
    def mouseDoubleClickEvent(self, event):
        """鼠标双击事件（橡皮擦模式下显示清屏按钮）"""
        if self.drawing_board.current_tool == "eraser":
            # 显示清屏按钮
            self.clearBtn.show()
            # 3秒后自动隐藏
            self.clearBtn_timer.start(3000)
    
    def simulate_ppt_key(self, key):
        """模拟PPT翻页按键"""
        # 1. 生成键盘按下事件
        key_press_event = QKeyEvent(QEvent.KeyPress, key, Qt.NoModifier)
        QCoreApplication.postEvent(QApplication.instance(), key_press_event)
        
        # 2. 短暂延迟
        loop = QEventLoop()
        QTimer.singleShot(10, loop.quit)
        loop.exec()
        
        # 3. 生成键盘释放事件
        key_release_event = QKeyEvent(QEvent.KeyRelease, key, Qt.NoModifier)
        QCoreApplication.postEvent(QApplication.instance(), key_release_event)
        
        # 4. 清空绘图
        self.clear_drawing()
    



def main():
    """主函数"""
    print("Starting EasyWriteWhiteBoard...")
    # 创建应用程序
    app = QApplication(sys.argv)
    print("QApplication created successfully")
    
    # 应用样式表
    try:
        with open('style.qss', 'r', encoding='utf-8') as f:
            style_sheet = f.read()
            app.setStyleSheet(style_sheet)
    except FileNotFoundError:
        print("未找到样式文件 style.qss，使用默认样式")
    
    # 创建主窗口
    window = MainWindow()
    print("MainWindow created successfully")
    window.show()
    print("Window shown")
    
    # 运行应用程序
    sys.exit(app.exec())


if __name__ == "__main__":
    main()