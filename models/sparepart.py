import sqlite3

class Sparepart:
    def __init__(self):
        self.__conn = sqlite3.connect('wimotor.db')
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

    def fetch_data(self):
        cursor = self.__conn.cursor()
        cursor.execute('''
            SELECT * FROM sparepart
            ORDER BY id DESC
        ''')
        return cursor.fetchall()

    def search_data(self, search):
        cursor = self.__conn.cursor()
        cursor.execute('''
            SELECT * FROM sparepart
                WHERE LOWER(kode_barang) LIKE LOWER(?) OR LOWER(nama_barang) LIKE LOWER(?)
                ORDER BY id DESC
        ''', (f'%{search}%', f'%{search}%'))
        return cursor.fetchall()

    def tambah_barang_baru(self, kode, nama, kuantiti, lokasi):
        cursor = self.__conn.cursor()
        cursor.execute('''
            INSERT INTO sparepart (kode_barang, nama_barang, kuantiti, lokasi)
            VALUES (?, ?, ?, ?)
        ''', (kode, nama, kuantiti, lokasi))
        self.__conn.commit()

    def update_kuantiti(self, id, kuantiti):
        cursor = self.__conn.cursor()
        cursor.execute('''
            UPDATE sparepart
            SET kuantiti = ?
            WHERE id = ?
        ''', (kuantiti, id))
        self.__conn.commit()

    # def hapus_barang(self):
    #     id = (2,)
    #     cursor = self.__conn.cursor()
    #     cursor.execute('''
    #         DELETE FROM sparepart
    #         WHERE id = ?
    #     ''', id)
    #     self.__conn.commit()