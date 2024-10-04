import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt

from components.gudang_edit_barang import GudangEditBarang
from components.konfirmasi_hapus import KonfirmasiHapus

class InformasiBarang(QtWidgets.QDialog):
    def __init__(self, gudang, data):
        super().__init__()
        self.__gudang = gudang
        self.__data = data
        self.__show_app__()
        self.__start__()

    def __show_app__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, '../views/InformasiBarang.ui')
        uic.loadUi(ui_path, self)
        self.__show_information__()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setFixedSize(self.size())

    def __start__(self):
        self.setFocus()
        self.__bind_widgets__()
        self.__disable_tab__()

    def __show_information__(self):
        self.kode_info.setText(f'{self.__data[1]}')
        self.nama_info.setText(f'{self.__data[2]}')
        self.kuantiti_info.setText(f'{self.__data[3]}')
        self.lokasi_info.setText(f'{self.__data[4]}')

    def __bind_widgets__(self):
        self.edit_btn.clicked.connect(lambda: self.__edit_barang__())
        self.hapus_btn.clicked.connect(lambda: self.__hapus_barang__())

    def __disable_tab__(self):
        self.setFocusPolicy(Qt.StrongFocus)
        self.edit_btn.setFocusPolicy(Qt.NoFocus)
        self.hapus_btn.setFocusPolicy(Qt.NoFocus)

    def __edit_barang__(self):
        dialog = GudangEditBarang(self.__gudang, self.__data)
        if (dialog.exec_() == QtWidgets.QDialog.Accepted):
            self.status = 'edited'
            self.data = dialog.data
            self.accept()

    def __hapus_barang__(self):
        dialog = KonfirmasiHapus('barang')
        if (dialog.exec_() == QtWidgets.QDialog.Accepted):
            try:
                self.__gudang.sparepart.hapus_barang(self.__data[0])
            except:
                self.__gudang.app.show_error('Gagal menghapus barang')
            else:
                self.status = 'deleted'
                self.accept()