import os
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QMessageBox

from models.sparepart import Sparepart

class GudangTambahBarang(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.__show_app__()
        self.__start__()

    def __show_app__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, '../TambahBarang.ui')
        uic.loadUi(ui_path, self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setFixedSize(self.size())

    def __start__(self):
        self.batal_btn.clicked.connect(lambda: self.__batal__())
        self.simpan_btn.clicked.connect(lambda: self.__simpan__())

        self.kode_input.setFocus()
        self.setTabOrder(self.kode_input, self.nama_input)
        self.setTabOrder(self.nama_input, self.kuantiti_input)
        self.setTabOrder(self.kuantiti_input, self.lokasi_input)
        self.setTabOrder(self.lokasi_input, self.batal_btn)
        self.setTabOrder(self.batal_btn, self.simpan_btn)
        self.setTabOrder(self.simpan_btn, self.kode_input)

    def __batal__(self):
        self.reject()

    def __simpan__(self):
        try:
            self.__sparepart = Sparepart()
        except:
            self.__show_error__('Koneksi database error')
        else:
            kode = self.kode_input.text().strip()
            nama = self.nama_input.text().strip()
            kuantiti = self.kuantiti_input.text().strip()
            lokasi = self.lokasi_input.text().strip()
            error = self.__validate_simpan__(nama, kuantiti)
            if (error):
                self.__show_input_error__(error)
            else:
                try:
                    self.__sparepart.tambah_barang_baru(kode, nama, int(kuantiti), lokasi)
                except:
                    self.__show_error__('Gagal menyimpan perubahan')
                else:
                    self.accept()

    def __validate_simpan__(self, nama, kuantiti):
        error = {}

        if (nama == ''):
            error['nama'] = 'Nama barang wajib diisi'

        if (kuantiti):
            try:
                kuantiti = int(kuantiti)
            except:
                error['kuantiti'] = 'Kuantiti wajib berupa angka'
            else:
                if (kuantiti <= 0):
                    error['kuantiti'] = 'Kuantiti tidak boleh dibawah 1'
                elif (kuantiti > 10000):
                    error['kuantiti'] = 'Kuantiti tidak boleh melebihi 10000'

        return error

    def __show_input_error__(self, error):
        nama_error = self.findChild(QWidget, 'nama_error')
        kuantiti_error = self.findChild(QWidget, 'kuantiti_error')

        if (nama_error and 'nama' not in error):
            self.gridLayout.removeWidget(nama_error)
            nama_error.deleteLater()
            self.nama_input.setStyleSheet('')
            self.setFixedSize(self.width(), self.height() - 18)
        elif (nama_error is None and 'nama' in error):
            self.__nama_error_layout = QHBoxLayout()
            self.__nama_error_layout.setContentsMargins(0, 0, 0, 0)
            self.__nama_error_layout.setSpacing(4)

            pixmap = QPixmap('./assets/Error.png').scaled(14, 14)

            self.__nama_error_icon = QLabel()
            self.__nama_error_icon.setPixmap(pixmap)
            self.__nama_error_icon.setFixedSize(14, 14)
            self.__nama_error_icon.setStyleSheet('''
                color: rgb(156, 0, 0);
            ''')

            self.__nama_error_message = QLabel()
            self.__nama_error_message.setText(error['nama'])
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

        if (kuantiti_error and 'kuantiti' in error):
            self.__kuantiti_error_message.setText(error['kuantiti'])
        elif (kuantiti_error and 'kuantiti' not in error):
            self.gridLayout.removeWidget(kuantiti_error)
            kuantiti_error.deleteLater()
            self.kuantiti_input.setStyleSheet('')
            self.setFixedSize(self.width(), self.height() - 18)
        elif (kuantiti_error is None and 'kuantiti' in error):
            self.__kuantiti_error_layout = QHBoxLayout()
            self.__kuantiti_error_layout.setContentsMargins(0, 0, 0, 0)
            self.__kuantiti_error_layout.setSpacing(4)

            pixmap = QPixmap('./assets/Error.png').scaled(14, 14)

            self.__kuantiti_error_icon = QLabel()
            self.__kuantiti_error_icon.setPixmap(pixmap)
            self.__kuantiti_error_icon.setFixedSize(14, 14)
            self.__kuantiti_error_icon.setStyleSheet('''
                color: rgb(156, 0, 0);
            ''')

            self.__kuantiti_error_message = QLabel()
            self.__kuantiti_error_message.setText(error['kuantiti'])
            self.__kuantiti_error_message.setStyleSheet('''
                color: rgb(156, 0, 0);
                font-size: 12px;
            ''')

            self.kuantiti_input.setStyleSheet('''
                border: 1px solid rgb(156, 0, 0);
            ''')

            self.__kuantiti_error_layout.addWidget(self.__kuantiti_error_icon)
            self.__kuantiti_error_layout.addWidget(self.__kuantiti_error_message)

            self.__kuantiti_error = QWidget()
            self.__kuantiti_error.setObjectName('kuantiti_error')
            self.__kuantiti_error.setLayout(self.__kuantiti_error_layout)
            self.setFixedSize(self.width(), self.height() + 18)
            self.gridLayout.addWidget(self.__kuantiti_error, 4, 3)

    def __show_error__(self, message):
        msg = QMessageBox()
        msg.setWindowTitle('Error')
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.exec_()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.__simpan__()
        else:
            super(GudangTambahBarang, self).keyPressEvent(event)

    def accept(self):
        super(GudangTambahBarang, self).accept()