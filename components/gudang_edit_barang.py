import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel

from views.py.EditBarang import Ui_EditBarang

class GudangEditBarang(QtWidgets.QDialog, Ui_EditBarang):
    def __init__(self, gudang, data):
        super().__init__()
        self.__gudang = gudang
        self.__data = data
        self.__show_app__()
        self.__start__()

    def __show_app__(self):
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setFixedSize(self.size())

    def __start__(self):
        self.kode_input.setFocus()
        self.__show_information__()
        self.__bind_widgets__()
        self.__tab_reorder__()

    def __show_information__(self):
        self.kode_input.setText(f'{self.__data[1]}')
        self.nama_input.setText(f'{self.__data[2]}')
        self.lokasi_input.setText(f'{self.__data[4]}')

    def __bind_widgets__(self):
        self.batal_btn.clicked.connect(lambda: self.__batal__())
        self.simpan_btn.clicked.connect(lambda: self.__simpan__())

    def __tab_reorder__(self):
        self.setTabOrder(self.kode_input, self.nama_input)
        self.setTabOrder(self.nama_input, self.lokasi_input)
        self.setTabOrder(self.lokasi_input, self.batal_btn)
        self.setTabOrder(self.batal_btn, self.simpan_btn)
        self.setTabOrder(self.simpan_btn, self.kode_input)

    def __batal__(self):
        self.reject()

    def __simpan__(self):
        kode = self.kode_input.text().strip()
        nama = self.nama_input.text().strip()
        lokasi = self.lokasi_input.text().strip()
        if (kode == self.__data[1] and nama == self.__data[2] and lokasi == self.__data[4]):
            self.__batal__()
        error = self.__validate_nama__(nama)
        if (error):
            self.__show_input_error__(error)
        else:
            try:
                self.__gudang.sparepart.update_barang(self.__data[0], kode, nama, lokasi)
            except:
                self.__gudang.app.show_error('Gagal menyimpan perubahan')
            else:
                self.data = [kode, nama, lokasi]
                self.accept()

    def __validate_nama__(self, nama):
        error = ''

        if (nama == ''):
            error = 'Nama barang wajib diisi'

        return error

    def __show_input_error__(self, error):
        nama_error = self.findChild(QWidget, 'nama_error')

        if (nama_error is None):
            self.__nama_error_layout = QHBoxLayout()
            self.__nama_error_layout.setContentsMargins(0, 0, 0, 0)
            self.__nama_error_layout.setSpacing(4)

            current_dir = os.path.dirname(os.path.abspath(__file__))
            error_path = os.path.join(current_dir, '../assets/Error.png')
            pixmap = QPixmap(error_path).scaled(14, 14)

            self.__nama_error_icon = QLabel()
            self.__nama_error_icon.setPixmap(pixmap)
            self.__nama_error_icon.setFixedSize(14, 14)
            self.__nama_error_icon.setStyleSheet('''
                color: rgb(156, 0, 0);
            ''')

            self.__nama_error_message = QLabel()
            self.__nama_error_message.setText(error)
            self.__nama_error_message.setStyleSheet('''
                color: rgb(156, 0, 0);
                font-size: 12px;
            ''')

            self.nama_input.setStyleSheet('''
                border: 1px solid rgb(156, 0, 0);
            ''')

            self.__nama_error_layout.addWidget(self.__nama_error_icon)
            self.__nama_error_layout.addWidget(self.__nama_error_message)

            self.__nama_error = QWidget()
            self.__nama_error.setObjectName('nama_error')
            self.__nama_error.setLayout(self.__nama_error_layout)
            self.setFixedSize(self.width(), self.height() + 18)
            self.gridLayout.addWidget(self.__nama_error, 2, 3)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.__simpan__()
        else:
            super(GudangEditBarang, self).keyPressEvent(event)