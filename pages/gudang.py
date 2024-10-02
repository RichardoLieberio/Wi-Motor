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
            sparepart.start()
            return sparepart
        except:
            self.__app.show_error('Koneksi database gagal')
            self.__app.quit_app()

    def __start__(self):
        self.__table = 'original'
        self.__search = ''
        self.__table_rows = []
        self.__bind_widgets__()
        self.__setup_and_save_table_rows__()

    def __bind_widgets__(self):
        self.__app.cari_barang_input.editingFinished.connect(lambda: self.__cari_barang__())
        self.__app.tambah_barang_btn.clicked.connect(lambda: self.__tambah_barang__())

    def __setup_and_save_table_rows__(self):
        sparepart_data = self.__sparepart.fetch_data()
        for i in range (len(sparepart_data)):
            self.__create_and_save_new_row__(i + 1, sparepart_data[i])

    def __create_and_save_new_row__(self, index, data):
        row = GudangTableRow(index, data)
        self.__table_rows.append(row)
        self.__app.gudang_table_body.addWidget(row.create_row())

    def __redisplay_original_table__(self):
        sparepart_data = self.__sparepart.fetch_data()
        for i in range (len(sparepart_data)):
            self.__table_rows[i].redisplay(i + 1, sparepart_data[i])
            self.__change_row_display(i + 1, 'show')

    def __redisplay_filtered_table__(self, search):
        sparepart_data = self.__sparepart.search_data(search)
        i = -1
        for i in range (len(sparepart_data)):
            self.__table_rows[i].redisplay(i + 1, sparepart_data[i])
            self.__change_row_display(i + 1, 'show')
        else:
            for n in range (i + 1, len(self.__table_rows)):
                self.__change_row_display(n + 1, 'hide')

    def __change_row_display(self, index, type):
        row = self.__app.findChild(QWidget, f'row{index}')
        if (row is not None):
            if (type == 'show'):
                row.show()
            else:
                row.hide()

    def __cari_barang__(self):
        search = self.__app.cari_barang_input.text()
        if (search != self.__search):
            if (len(search) >= 3):
                self.__search = search
                self.__table = 'filtered'
                self.__redisplay_filtered_table__(search)
            elif (len(search) < 3 and self.__table == 'filtered'):
                self.__search = ''
                self.__table = 'original'
                self.__redisplay_original_table__()

    def __tambah_barang__(self):
        dialog = GudangTambahBarang()
        if (dialog.exec_() == QtWidgets.QDialog.Accepted):
            dialog.data.insert(0, self.__sparepart.get_latest_id())
            self.__create_and_save_new_row__(len(self.__table_rows) + 1, dialog.data)
            if (self.__table == 'original'):
                self.__redisplay_original_table__()
            else:
                self.__redisplay_filtered_table__(self.__search)
            pass