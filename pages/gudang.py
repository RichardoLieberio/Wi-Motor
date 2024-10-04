from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from models.sparepart import Sparepart
from components.gudang_tambah_barang import GudangTambahBarang
from components.gudang_table_row import GudangTableRow

class Gudang():
    def __init__(self, app):
        self.app = app
        self.sparepart = self.__connect_and_get_sparepart__()
        self.__start__()

    def __connect_and_get_sparepart__(self):
        try:
            sparepart = Sparepart()
            sparepart.start()
            return sparepart
        except:
            self.app.show_error('Koneksi database gagal')
            self.app.quit_app()

    def __start__(self):
        self.__table = 'original'
        self.__search = ''
        self.__table_rows = []
        self.__bind_widgets__()
        self.__setup_table__()

    def __bind_widgets__(self):
        self.app.cari_barang_input.editingFinished.connect(lambda: self.__cari_barang__())
        self.app.tambah_barang_btn.clicked.connect(lambda: self.__tambah_barang__())

    def __setup_table__(self):
        sparepart_data = self.sparepart.fetch_data()
        for i in range (len(sparepart_data)):
            self.__create_and_save_new_row__(i + 1, sparepart_data[i])

    def __create_and_save_new_row__(self, index, data):
        row = GudangTableRow(self, index, data)
        self.__table_rows.append(row)
        self.app.gudang_table_body.addWidget(row.create_row())

    def __cari_barang__(self):
        search = self.app.cari_barang_input.text()
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
        dialog = GudangTambahBarang(self)
        if (dialog.exec_() == QtWidgets.QDialog.Accepted):
            dialog.data.insert(0, self.sparepart.get_latest_id())
            self.__create_and_save_new_row__(len(self.__table_rows) + 1, dialog.data)
            if (self.__table == 'original'):
                self.__redisplay_original_table__()
            else:
                self.__redisplay_filtered_table__(self.__search)

    def __redisplay_original_table__(self):
        sparepart_data = self.sparepart.fetch_data()
        for i in range (len(sparepart_data)):
            self.__table_rows[i].redisplay(i + 1, sparepart_data[i])
            self.__change_row_display__(i + 1, 'show')

    def __redisplay_filtered_table__(self, search):
        sparepart_data = self.sparepart.search_data(search)
        i = -1
        for i in range (len(sparepart_data)):
            self.__table_rows[i].redisplay(i + 1, sparepart_data[i])
            self.__change_row_display__(i + 1, 'show')
        else:
            for n in range (i + 1, len(self.__table_rows)):
                self.__change_row_display__(n + 1, 'hide')

    def __change_row_display__(self, index, type):
        row = self.app.findChild(QWidget, f'row{index}')
        if (row is not None):
            if (type == 'show'):
                row.show()
            else:
                row.hide()

    def delete_row(self):
        last_row = self.app.findChild(QWidget, f'row{len(self.__table_rows)}')
        if (last_row is not None):
            self.app.gudang_table_body.removeWidget(last_row)
            last_row.deleteLater()
            self.__table_rows.pop()
            if (self.__table == 'original'):
                self.__redisplay_original_table__()
            else:
                self.__redisplay_filtered_table__(self.__search)