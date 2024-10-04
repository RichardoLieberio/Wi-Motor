import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from views.py.App import Ui_App
from pages.gudang import Gudang

class App(QMainWindow, Ui_App):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.__gudang_page = None
        # self.__bon_page = None
        # self.__mekanik_page = None
        self.__start__()

    def __start__(self):
        self.gudang_menu.setChecked(True)
        self.__bind_menu__()
        self.__change_page_to_gudang__()

    def __bind_menu__(self):
        self.gudang_menu.clicked.connect(lambda: self.__change_page_to_gudang__())
        self.bon_menu.clicked.connect(lambda: self.__change_page_to_bon__())
        self.mekanik_menu.clicked.connect(lambda: self.__change_page_to_mekanik__())

    def __change_page_to_gudang__(self):
        self.main_page.setCurrentIndex(0)
        if (self.__gudang_page is None):
            self.__gudang_page = Gudang(self)

    def __change_page_to_bon__(self):
        self.main_page.setCurrentIndex(1)

    def __change_page_to_mekanik__(self):
        self.main_page.setCurrentIndex(2)

    def show_error(self, message):
        msg = QMessageBox()
        msg.setWindowTitle('Error')
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.exec_()

    def quit_app(self):
        QApplication.quit()
        sys.exit()