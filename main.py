import sys
import sqlite3
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Sparepart:
    def __init__(self):
        self.__conn = sqlite3.connect('wimotor.db')
        self.__create_table__()
        self.__fetch_data__()

    def __create_table__(self):
        cursor = self.__conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sparepart (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                kode_barang TEXT(50),
                nama_barang TEXT(255),
                kuantiti INTEGER NOT NULL,
                lokasi TEXT(255)
            )
        ''')
        self.__conn.commit()

    def __fetch_data__(self):
        cursor = self.__conn.cursor()
        cursor.execute('''
            SELECT * FROM sparepart
            ORDER BY id DESC
        ''')
        self.__data = cursor.fetchall()

    def get_data(self):
        return self.__data

    def tambah_barang_baru(self, kode, nama, kuantiti, lokasi):
        data = (kode, nama, kuantiti, lokasi)
        cursor = self.__conn.cursor()
        cursor.execute('''
            INSERT INTO sparepart (kode_barang, nama_barang, kuantiti, lokasi)
            VALUES (?, ?, ?, ?)
        ''', data)
        self.__conn.commit()

    def update_kuantiti(self, id, kuantiti):
        cursor = self.__conn.cursor()
        cursor.execute('''
            UPDATE sparepart
            SET kuantiti = ?
            WHERE id = ?
        ''', (kuantiti, id))
        self.__conn.commit()

    def hapus_barang(self):
        id = (2,)
        cursor = self.__conn.cursor()
        cursor.execute('''
            DELETE FROM sparepart
            WHERE id = ?
        ''', id)
        self.__conn.commit()

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        try:
            self.__db = Sparepart()
            uic.loadUi('App.ui', self)
            self.showMaximized()
        except:
            msg = QMessageBox()
            msg.setWindowTitle('Error')
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Koneksi database error')
            msg.exec_()
            QApplication.quit()
            sys.exit()
        else:
            self.gudang.setChecked(True)
            self.__create_gudang_table__()
            self.__bind_menu__()
            self.__change_page_to_gudang__()
            self.__filter = ''
            self.cari_barang_input.editingFinished.connect(lambda: self.__search__(self.cari_barang_input.text()))
            self.tambah.clicked.connect(lambda: self.__tambah_clicked__())

    def __create_gudang_table__(self):
        self.__table = 'original'
        data = self.__db.get_data()
        self.__row = []
        self.__latest_id = data[0][0]
        for i in range (len(data)):
            row = TableRow(i + 1, data[i])
            self.__row.append(row)
            row = row.__create_row__()
            self.table_body.addWidget(row)

    def __bind_menu__(self):
        self.gudang.clicked.connect(lambda: self.__change_page_to_gudang__())
        self.bon.clicked.connect(lambda: self.__change_page_to_bon__())
        self.mekanik.clicked.connect(lambda: self.__change_page_to_mekanik__())

    def __change_page_to_gudang__(self):
        self.main_page.setCurrentIndex(0)

    def __change_page_to_bon__(self):
        self.main_page.setCurrentIndex(1)

    def __change_page_to_mekanik__(self):
        self.main_page.setCurrentIndex(2)

    def __search__(self, filter):
        if (self.__filter != filter):
            if (len(filter) >= 3):
                i = 0
                # Sudah ada table_body container. Tinggal hapus table_body terus buat baru dan tambahan ke table_body_container
                for n in range (len(self.__row)):
                    item = len(self.__row) - n - 1 + i
                    if (self.table_body.itemAt(item) and self.table_body.itemAt(item).widget()):
                        self.table_body.itemAt(item).widget().deleteLater()
                    if (self.__row[n].contains(filter)):
                        self.table_body.insertWidget(i, self.__row[n].__create_row__())
                        i += 1
                self.__filter = filter
                self.__table = 'filtered'
            elif (len(filter) < 3 and self.__table == 'filtered'):
                self.__filter = ''
                self.__create_gudang_table__()

    def __tambah_clicked__(self):
        dialog = TambahBarang()
        if (dialog.exec_() == QtWidgets.QDialog.Accepted):
            self.__latest_id += 1
            row = TableRow(self.__latest_id, [self.__latest_id, dialog.kode, dialog.nama, dialog.kuantiti, dialog.lokasi])
            self.__row.insert(0, row)
            row = row.__create_row__()
            self.table_body.insertWidget(0, row)
            self.__resort_table__()

    def __resort_table__(self):
        for i in range (len(self.__row)):
            self.__row[i].set_new_index(i + 1)

class TableRow():
    def __init__(self, index, data):
        self.__index = index
        self.__data = data

    def __create_row__(self):
        self.__layout = QHBoxLayout()
        self.__layout.setContentsMargins(8, 8, 8, 8)
        self.__layout.setSpacing(32)

        self.__layout.addWidget(self.__create_no__())
        self.__layout.addWidget(self.__create_kode__(), 1)
        self.__layout.addWidget(self.__create_nama__(), 2)
        self.__layout.addWidget(self.__create_kuantiti__())
        self.__layout.addWidget(self.__create_kelola__())

        self.__container = QWidget()
        self.__container.setObjectName(f'row{self.__index}')
        color = 255 if (self.__index % 2) else 225
        self.__container.setStyleSheet(f'''
            #{self.__container.objectName()} {{
                background-color: rgb({color}, {color}, {color});
            }}

            #{self.__container.objectName()}:hover {{
                background-color: rgb(200, 200, 200);
            }}
        ''')
        self.__container.setLayout(self.__layout)

        return self.__container

    def __create_no__(self):
        self.__no = QLabel(f'{self.__index}')
        self.__no.setMinimumWidth(40)
        self.__no.setMaximumWidth(40)
        self.__no.setStyleSheet('''
            font-size: 14px;
            color: rgb(30, 30, 30);
        ''')
        return self.__no

    def __create_kode__(self):
        self.__kode = QLabel(f'{self.__data[1]}')
        self.__kode.setMinimumWidth(90)
        self.__kode.setMaximumWidth(160)
        self.__kode.setStyleSheet('''
            font-size: 14px;
            color: rgb(30, 30, 30);
        ''')
        return self.__kode

    def __create_nama__(self):
        self.__nama = QLabel(f'{self.__data[2]}')
        self.__nama.setMinimumWidth(250)
        self.__nama.setStyleSheet('''
            font-size: 14px;
            color: rgb(30, 30, 30);
        ''')
        return self.__nama

    def __create_kuantiti__(self):
        self.__kuantiti = QLabel(f'{self.__data[3]}')
        self.__kuantiti.setMinimumWidth(70)
        self.__kuantiti.setMaximumWidth(70)
        self.__kuantiti.setStyleSheet('''
            font-size: 14px;
            color: rgb(30, 30, 30);
        ''')
        return self.__kuantiti

    def __create_kelola__(self):
        self.__kelola_layout = QHBoxLayout()
        self.__kelola_layout.setContentsMargins(0, 0, 0, 0)
        self.__kelola_layout.setSpacing(8)

        self.__kelola_layout.addWidget(self.__create_ambil__())
        self.__kelola_layout.addWidget(self.__create_tambah__())

        self.__kelola = QWidget()
        self.__kelola.setMinimumWidth(160)
        self.__kelola.setMaximumWidth(160)
        self.__kelola.setLayout(self.__kelola_layout)
        return self.__kelola

    def __create_ambil__(self):
        self.__ambil = QPushButton('Ambil')
        self.__ambil.setStyleSheet('''
            QPushButton {
                padding: 4px 0;
                font-size: 12px;
                color: rgb(255, 255, 255);
                background-color: rgb(88, 0, 169);
                border: 1px solid rgb(88, 0, 169);
            }

            QPushButton:hover {
                background-color: rgb(69, 0, 133);
            }
        ''')
        self.__ambil.setCursor(Qt.PointingHandCursor)
        self.__ambil.clicked.connect(lambda: self.__ambil_clicked__())
        return self.__ambil

    def __create_tambah__(self):
        self.__tambah = QPushButton('Tambah')
        self.__tambah.setStyleSheet('''
            QPushButton {
                padding: 4px 0;
                font-size: 12px;
                color: rgb(255, 255, 255);
                background-color: rgb(156, 0, 0);
                border: 1px solid rgb(156, 0, 0);
            }

            QPushButton:hover {
                background-color: rgb(120, 0, 0);
            }
        ''')
        self.__tambah.setCursor(Qt.PointingHandCursor)
        self.__tambah.clicked.connect(lambda: self.__tambah_clicked__())
        return self.__tambah

    def __ambil_clicked__(self):
        dialog = Kelola(self.__data[0], int(self.__kuantiti.text()), self.set_new_kuantiti, 'Ambil')
        if (dialog.exec_() == QtWidgets.QDialog.Accepted):
            pass

    def __tambah_clicked__(self):
        dialog = Kelola(self.__data[0], int(self.__kuantiti.text()), self.set_new_kuantiti, 'Tambah')
        if (dialog.exec_() == QtWidgets.QDialog.Accepted):
            pass

    def set_new_index(self, index):
        self.__no.setText(f'{index}')

    def set_new_kuantiti(self, amount):
        self.__kuantiti.setText(f'{amount}')

    def contains(self, filter):
        if (filter.lower() in self.__nama.text().lower() or filter.lower() in self.__kode.text().lower()):
            return True
        else:
            return False

class TambahBarang(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('TambahBarang.ui', self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setFixedSize(self.size())
        self.kode.setFocus()
        self.batal.clicked.connect(lambda: self.__batal__())
        self.simpan.clicked.connect(lambda: self.__simpan__())

        self.setTabOrder(self.kode, self.nama)
        self.setTabOrder(self.nama, self.kuantiti)
        self.setTabOrder(self.kuantiti, self.lokasi)
        self.setTabOrder(self.lokasi, self.batal)
        self.setTabOrder(self.batal, self.simpan)
        self.setTabOrder(self.simpan, self.kode)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.__simpan__()
        else:
            super(TambahBarang, self).keyPressEvent(event)

    def __batal__(self):
        self.reject()

    def __simpan__(self):
        try:
            self.__db = Sparepart()
        except:
            self.__show_error__('Koneksi database error')
        else:
            kode = self.kode.text().strip()
            nama = self.nama.text().strip()
            kuantiti = self.kuantiti.text().strip()
            lokasi = self.lokasi.text().strip()
            error = self.__validate_simpan__(nama, kuantiti)
            if (error):
                self.__show_input_error__(error)
            else:
                try:
                    self.__db.tambah_barang_baru(kode, nama, int(kuantiti), lokasi)
                except:
                    self.__show_error__('Gagal menyimpan perubahan')
                else:
                    self.kode = kode
                    self.nama = nama
                    self.kuantiti = int(kuantiti)
                    self.lokasi = lokasi
                    self.accept()

    def __validate_simpan__(self, nama, kuantiti):
        error = {}

        if (not nama):
            error['nama'] = 'Nama barang wajib diisi'

        if (kuantiti):
            try:
                kuantiti = int(kuantiti)
            except:
                error['kuantiti'] = 'Kuantiti wajib berupa angka'
            else:
                if (kuantiti > 10000):
                    error['kuantiti'] = 'Kuantiti tidak boleh melebihi 10000'

        return error

    def __show_input_error__(self, error):
        nama_error = self.findChild(QWidget, 'nama_error')
        kuantiti_error = self.findChild(QWidget, 'kuantiti_error')

        if (nama_error and 'nama' not in error):
            self.gridLayout.removeWidget(nama_error)
            nama_error.deleteLater()
            self.nama.setStyleSheet('')
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

            self.nama.setStyleSheet('''
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
            self.kuantiti.setStyleSheet('')
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

            self.kuantiti.setStyleSheet('''
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

class Kelola(QtWidgets.QDialog):
    def __init__(self, id, amount, set_new_kuantiti, tipe):
        super().__init__()
        self.__id = id
        self.__amount = amount
        self.__set_new_kuantiti = set_new_kuantiti
        self.__tipe = tipe

        uic.loadUi('Kelola.ui', self)
        self.setWindowTitle(f'Kelola - {self.__tipe} Barang')
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setFixedSize(self.size())
        self.batal.clicked.connect(lambda: self.__batal__())
        self.simpan.clicked.connect(lambda: self.__simpan__())

        self.setTabOrder(self.kuantiti, self.batal)
        self.setTabOrder(self.batal, self.simpan)
        self.setTabOrder(self.simpan, self.kuantiti)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.__simpan__()
        else:
            super(Kelola, self).keyPressEvent(event)

    def __batal__(self):
        self.reject()

    def __simpan__(self):
        try:
            self.__db = Sparepart()
        except:
            self.__show_error__('Koneksi database error')
        else:
            kuantiti = self.kuantiti.text().strip()
            error = self.__validate_simpan__(kuantiti)
            if (error):
                self.__show_input_error__(error)
            else:
                if (self.__tipe == 'Ambil'):
                    new_kuantiti = self.__amount - int(kuantiti)
                else:
                    new_kuantiti = self.__amount + int(kuantiti)
                try:
                    self.__db.update_kuantiti(self.__id, new_kuantiti)
                except:
                    self.__show_error__('Gagal menyimpan perubahan')
                else:
                    self.__set_new_kuantiti(new_kuantiti)
                    self.accept()

    def __validate_simpan__(self, kuantiti):
        error = ''
        if (not kuantiti):
            error = 'Kuantiti wajib diisi'
        else:
            try:
                kuantiti = int(kuantiti)
            except:
                error = 'Kuantiti wajib berupa angka'
            else:
                if (kuantiti <= 0):
                    error = 'Kuantiti tidak boleh dibawah 1'
                elif (self.__tipe != 'Ambil' and kuantiti > 10000):
                    error = 'Kuantiti tidak boleh melebihi 10000'
                elif (self.__tipe == 'Ambil' and kuantiti > self.__amount):
                    error = f'Kuantiti tidak boleh melebihi {self.__amount}'
        return error

    def __show_input_error__(self, message):
        kuantiti_error = self.findChild(QWidget, 'kuantiti_error')
        if (kuantiti_error):
            self.__kuantiti_error_message.setText(message)
        else:
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
            self.__kuantiti_error_message.setText(message)
            self.__kuantiti_error_message.setStyleSheet('''
                color: rgb(156, 0, 0);
                font-size: 12px;
            ''')

            self.kuantiti.setStyleSheet('''
                border: 1px solid rgb(156, 0, 0);
            ''')

            self.__kuantiti_error_layout.addWidget(self.__kuantiti_error_icon)
            self.__kuantiti_error_layout.addWidget(self.__kuantiti_error_message)

            self.__kuantiti_error = QWidget()
            self.__kuantiti_error.setObjectName('kuantiti_error')
            self.__kuantiti_error.setLayout(self.__kuantiti_error_layout)
            self.setFixedSize(self.width(), self.height() + 18)
            self.gridLayout.addWidget(self.__kuantiti_error, 1, 3)

    def __show_error__(self, message):
        msg = QMessageBox()
        msg.setWindowTitle('Error')
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.exec_()

def main():
    app = QApplication([])
    window = App()
    app.exec_()

if __name__ == '__main__':
    main()