import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.Ui_mainui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # 确保窗口在最前面显示
    window.raise_()
    window.activateWindow()
    sys.exit(app.exec())