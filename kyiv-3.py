from PyQt6 import QtCore, QtWidgets
from qt_main import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        translator = QtCore.QTranslator()
        if translator.load(".\\Locales\\Ukrainian.qm"):
            QtCore.QCoreApplication.installTranslator(translator)
        else:
            print("Failed to load translation")
        self.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())