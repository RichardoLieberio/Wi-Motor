from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel

from views.py.Kelola import Ui_Kelola

class GudangKelola(QtWidgets.QDialog, Ui_Kelola):
    def __init__(self, gudang, id, current_kuantiti, tipe):
        super().__init__()
        self.__gudang = gudang
        self.__id = id
        self.__current_kuantiti = current_kuantiti
        self.__tipe = tipe
        self.__show_app__()
        self.__start__()

    def __show_app__(self):
        self.setupUi(self)
        self.setWindowTitle(f'Kelola - {self.__tipe} Barang')
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setFixedSize(self.size())

    def __start__(self):
        self.__bind_widgets__()
        self.__tab_reorder__()

    def __bind_widgets__(self):
        self.batal_btn.clicked.connect(lambda: self.__batal__())
        self.simpan_btn.clicked.connect(lambda: self.__simpan__())

    def __tab_reorder__(self):
        self.setTabOrder(self.kuantiti_input, self.batal_btn)
        self.setTabOrder(self.batal_btn, self.simpan_btn)
        self.setTabOrder(self.simpan_btn, self.kuantiti_input)

    def __batal__(self):
        self.reject()

    def __simpan__(self):
        kuantiti = self.kuantiti_input.text().strip()
        error = self.__validate_kuantiti__(kuantiti)
        if (error):
            self.__show_kuantiti_error__(error)
        else:
            self.new_kuantiti = self.__current_kuantiti - int(kuantiti) if self.__tipe == 'Ambil' else self.__current_kuantiti + int(kuantiti)
            try:
                self.__gudang.sparepart.update_kuantiti(self.__id, self.new_kuantiti)
            except:
                self.__gudang.app.show_error('Gagal menyimpan perubahan')
            else:
                self.accept()

    def __validate_kuantiti__(self, kuantiti):
        error = ''
        if (not kuantiti):
            error = 'Kuantiti wajib diisi'
        else:
            try:
                kuantiti = int(kuantiti)
            except:
                error = 'Kuantiti wajib berupa angka'
            else:
                if (self.__tipe == 'Ambil' and self.__current_kuantiti == 0):
                    error = 'Barang kosong'
                elif (kuantiti <= 0):
                    error = 'Kuantiti tidak boleh dibawah 1'
                elif (self.__tipe != 'Ambil' and kuantiti > 10000):
                    error = 'Kuantiti tidak boleh melebihi 10000'
                elif (self.__tipe == 'Ambil' and kuantiti > self.__current_kuantiti):
                    error = f'Kuantiti tidak boleh melebihi {self.__current_kuantiti}'
        return error

    def __show_kuantiti_error__(self, error):
        kuantiti_error = self.findChild(QWidget, 'kuantiti_error')
        if (kuantiti_error):
            self.__kuantiti_error_message.setText(error)
        else:
            kuantiti_error_layout = QHBoxLayout()
            kuantiti_error_layout.setContentsMargins(0, 0, 0, 0)
            kuantiti_error_layout.setSpacing(4)

            pixmap = QPixmap('assets/Error.png').scaled(14, 14)

            kuantiti_error_icon = QLabel()
            kuantiti_error_icon.setPixmap(pixmap)
            kuantiti_error_icon.setFixedSize(14, 14)
            kuantiti_error_icon.setStyleSheet('''
                color: rgb(156, 0, 0);
            ''')

            self.__kuantiti_error_message = QLabel()
            self.__kuantiti_error_message.setText(error)
            self.__kuantiti_error_message.setStyleSheet('''
                color: rgb(156, 0, 0);
                font-size: 12px;
            ''')

            self.kuantiti_input.setStyleSheet('''
                border: 1px solid rgb(156, 0, 0);
            ''')

            kuantiti_error_layout.addWidget(kuantiti_error_icon)
            kuantiti_error_layout.addWidget(self.__kuantiti_error_message)

            kuantiti_error = QWidget()
            kuantiti_error.setObjectName('kuantiti_error')
            kuantiti_error.setLayout(kuantiti_error_layout)
            self.setFixedSize(self.width(), self.height() + 18)
            self.gridLayout.addWidget(kuantiti_error, 1, 3)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.__simpan__()
        else:
            super(GudangKelola, self).keyPressEvent(event)