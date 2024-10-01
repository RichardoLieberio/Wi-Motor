from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from models.sparepart import Sparepart
from components.gudang_tambah_barang import GudangTambahBarang
from components.gudang_table_row import GudangTableRow

class Gudang():
    def __init__(self, app):
        self.__app = app
        self.__sparepart = self.__connect_and_get_sparepart__()
        self.__start__()

    def __connect_and_get_sparepart__(self):
        try:
            sparepart = Sparepart()
            return sparepart
        except:
            self.__app.show_error('Koneksi database gagal')
            self.__app.quit_app()

    def __start__(self):
        self.__table = 'original'
        self.__search = ''
        self.__bind_widgets__()
        self.__create_and_show_table('original')

    def __bind_widgets__(self):
        self.__app.cari_barang_input.editingFinished.connect(lambda: self.__cari_barang__())
        self.__app.tambah_barang_btn.clicked.connect(lambda: self.__tambah_barang__())

    def __create_and_show_table(self, type):
        layout = self.__create_and_get_table_layout__()
        sparepart_data = self.__sparepart.fetch_data() if type == 'original' else self.__sparepart.search_data(self.__search)
        for i in range (len(sparepart_data)):
            row_widget = self.__create_and_get_table_row__(i + 1, sparepart_data[i])
            layout.addWidget(row_widget)

        container = self.__create_and_get_table_container__(layout)
        self.__app.gudang_table_body_layout.addWidget(container)

    def __empty_table__(self):
        gudang_table_body = self.__app.findChild(QWidget, 'gudang_table_body')
        if (gudang_table_body is not None):
            self.__app.gudang_table_body_layout.removeWidget(gudang_table_body)
            gudang_table_body.deleteLater()

    def __create_and_get_table_layout__(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        return layout

    def __create_and_get_table_container__(self, layout):
        container = QWidget()
        container.setObjectName('gudang_table_body')
        container.setLayout(layout)
        return container

    def __create_and_get_table_row__(self, index, data):
        row = GudangTableRow(index, data)
        return row.create_row()

    def __cari_barang__(self):
        search = self.__app.cari_barang_input.text()
        if (search != self.__search):
            if (len(search) >= 3):
                self.__search = search
                self.__table = 'filtered'
                self.__empty_table__()
                self.__create_and_show_table('filtered')
            elif (len(search) < 3 and self.__table == 'filtered'):
                self.__search = ''
                self.__table = 'original'
                self.__empty_table__()
                self.__create_and_show_table('original')

    def __tambah_barang__(self):
        dialog = GudangTambahBarang()
        if (dialog.exec_() == QtWidgets.QDialog.Accepted):
            self.__search = ''
            self.__table = 'original'
            self.__empty_table__()
            self.__create_and_show_table('original')
            pass