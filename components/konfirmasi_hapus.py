from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt

from views.py.KonfirmasiHapus import Ui_KonfirmasiHapus

class KonfirmasiHapus(QtWidgets.QDialog, Ui_KonfirmasiHapus):
    def __init__(self, text):
        super().__init__()
        self.__text = text
        self.__show_app__()
        self.__start__()

    def __show_app__(self):
        self.setupUi(self)
        self.setWindowTitle(f'Konfirmasi Penghapusan {self.__text[0].upper() + self.__text[1:].lower()}')
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setFixedSize(self.size())

    def __start__(self):
        self.setFocus()
        self.__show_information__()
        self.__bind_widgets__()

    def __show_information__(self):
        self.title.setText(f'Hapus {self.__text}?')
        self.text.setText(f'{self.__text[0].upper() + self.__text[1:].lower()} yang telah dihapus tidak dapat dikembalikan')

    def __bind_widgets__(self):
        self.batal_btn.clicked.connect(lambda: self.__batal__())
        self.hapus_btn.clicked.connect(lambda: self.__hapus__())

    def __batal__(self):
        self.reject()

    def __hapus__(self):
        self.accept()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.__hapus__()
        else:
            super(KonfirmasiHapus, self).keyPressEvent(event)