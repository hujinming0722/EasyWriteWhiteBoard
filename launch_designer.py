import subprocess
import sys
import os

def launch_qt_designer():
    """启动Qt Designer并打开mainui.ui文件"""
    try:
        # 获取当前目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file_path = os.path.join(current_dir, "ui", "mainui.ui")
        
        # 检查UI文件是否存在
        if not os.path.exists(ui_file_path):
            print(f"错误: 找不到UI文件 {ui_file_path}")
            return False
            
        # 启动Qt Designer
        print(f"正在启动 Qt Designer 并打开 {ui_file_path}")
        subprocess.Popen(["pyside6-designer", ui_file_path])
        print("Qt Designer 已启动")
        return True
        
    except Exception as e:
        print(f"启动 Qt Designer 时出错: {e}")
        return False

if __name__ == "__main__":
    launch_qt_designer()