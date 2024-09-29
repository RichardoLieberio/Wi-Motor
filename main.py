import sys
import sqlite3
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic

class Sparepart:
    def __init__(self):
        self.__conn = sqlite3.connect('wimotor.db')

    def start(self):
        self.__create_table__()
        self.__get_data__()

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

    def __get_data__(self):
        cursor = self.__conn.cursor()
        cursor.execute('''
            SELECT * FROM sparepart
        ''')
        self.data = cursor.fetchall()

    def tambah_barang_baru(self):
        data = ('KODE/0008', 'Kampas Rem', 8, 'Steleng kanan atas')
        cursor = self.__conn.cursor()
        cursor.execute('''
            INSERT INTO sparepart (kode_barang, nama_barang, kuantiti, lokasi)
            VALUES (?, ?, ?, ?)
        ''', data)
        self.__conn.commit()

    def hapus_barang(self):
        id = (2,)
        cursor = self.__conn.cursor()
        cursor.execute('''
            DELETE FROM sparepart
            WHERE id = ?
        ''', id)
        self.__conn.commit()

    def update_kuantiti(self, id, kuantiti):
        cursor = self.__conn.cursor()
        cursor.execute('''
            UPDATE sparepart
            SET kuantiti = ?
            WHERE id = ?
        ''', (kuantiti, id))
        self.__conn.commit()

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        try:
            self.__db = Sparepart()
            self.__db.start()
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
            self.__change_page_to_gudang__()
            self.__bind_menu__()

    def __create_gudang_table__(self):
        for i in range (len(self.__db.data)):
            row = TableRow(i + 1, self.__db.data[i])
            row = row.__create_row__()
            self.table_body.addWidget(row)

    def __bind_menu__(self):
        self.gudang.clicked.connect(self.__change_page_to_gudang__)
        self.bon.clicked.connect(self.__change_page_to_bon__)
        self.mekanik.clicked.connect(self.__change_page_to_mekanik__)

    def __change_page_to_gudang__(self):
        self.main_page.setCurrentIndex(0)

    def __change_page_to_bon__(self):
        self.main_page.setCurrentIndex(1)

    def __change_page_to_mekanik__(self):
        self.main_page.setCurrentIndex(2)

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

    def set_new_kuantiti(self, amount):
        self.__kuantiti.setText(f'{amount}')

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
            kuantiti = self.input.text().strip()
            error = self.__validate_simpan__(kuantiti)
            if (error):
                if (self.error_message.text() == ''):
                    self.setFixedSize(self.width(), self.height() + 18)
                    self.layout.setSpacing(24)
                    pixmap = QPixmap('./assets/Error.png').scaled(14, 14)
                    self.error_icon.setPixmap(pixmap)
                    self.error_icon.setStyleSheet('''
                        background-color: rgb(255, 255, 255);
                    ''')
                    self.input.setStyleSheet('''
                        border: 1px solid rgb(156, 0, 0);
                    ''')
                self.error_message.setText(error)
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
        if not kuantiti:
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