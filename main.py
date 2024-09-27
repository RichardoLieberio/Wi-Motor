import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Database:
    def __init__(self):
        self.__conn = sqlite3.connect('wimotor.db')
        self.__create_table__()

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

    def tambah_barang_baru(self):
        data = ('KODE/0002', 'Ban dalam B', 5, 'Bawah rak')
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

    def ambil_barang(self):
        id = (1,)
        cursor = self.__conn.cursor()
        cursor.execute('''
            SELECT kuantiti FROM sparepart
            WHERE id = ?
        ''', id)
        result = cursor.fetchone()
        data = (result[0] - 3, 1)
        cursor.execute('''
            UPDATE sparepart
            SET kuantiti = ?
            WHERE id = ?
        ''', data)
        self.__conn.commit()

    def tambah_barang(self):
        id = (1,)
        cursor = self.__conn.cursor()
        cursor.execute('''
            SELECT kuantiti FROM sparepart
            WHERE id = ?
        ''', id)
        result = cursor.fetchone()
        data = (result[0] + 5, 1)
        cursor.execute('''
            UPDATE sparepart
            SET kuantiti = ?
            WHERE id = ?
        ''', data)
        self.__conn.commit()

    def close(self):
        if (self.__conn):
            self.__conn.close()

class App:
    def __init__(self, root):
        self.__root = root
        self.__root.title('Wi Motor')
        self.__root.state('zoomed')
        self.__root.minsize(800, 600)
        self.__root.configure(bg='white')
        self.__font_default = ('Helvetica', 11)
        self.__style = ttk.Style(self.__root)

        try:
            self.__db = Database()
        except:
            messagebox.showerror('Error', 'Koneksi database error')
            self.__db.close()
            self.__root.destroy()
        else:
            self.__create_widget__()

    def __create_widget__(self):
        self.__style.configure('padded.TEntry', padding=[10, 5, 10, 5])

        frame = tk.Frame(self.__root, bg='white')
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        main_container = tk.Frame(frame, bg='white')
        main_container.pack(fill=tk.X)

        left_container = tk.Frame(main_container, bg='white')
        left_container.pack(side=tk.LEFT)

        search_label = tk.Label(left_container, text='Cari barang', font=self.__font_default, bg='white')
        search_label.pack(side=tk.LEFT, padx=5, pady=5)

        search_entry = ttk.Entry(left_container, width=40, font=self.__font_default, style='padded.TEntry')
        search_entry.pack(side=tk.LEFT, padx=5, pady=5)

        right_container = tk.Frame(main_container, bg='white')
        right_container.pack(side=tk.RIGHT)

        tambah_barang_baru_btn = tk.Button(right_container, text='Tambah', command=self.__tambah_barang_baru__, bg='black', fg='white', bd=1, relief='solid', font=self.__font_default, width=15, pady=5, cursor='hand2')
        tambah_barang_baru_btn.pack(side=tk.LEFT, padx=5, pady=5)

        tambah_barang_baru_btn.bind('<Enter>', lambda e: tambah_barang_baru_btn.config(bg='#444'))
        tambah_barang_baru_btn.bind('<Leave>', lambda e: tambah_barang_baru_btn.config(bg='black'))

        hapus_barang_btn = tk.Button(right_container, text='Hapus', command=self.__hapus_barang__, bg='white', fg='black', bd=1, relief='solid', font=self.__font_default, width=15, pady=5, cursor='hand2')
        hapus_barang_btn.pack(side=tk.LEFT, padx=5, pady=5)

        hapus_barang_btn.bind('<Enter>', lambda e: hapus_barang_btn.config(bg='#eee'))
        hapus_barang_btn.bind('<Leave>', lambda e: hapus_barang_btn.config(bg='white'))

        header_frame = tk.Frame(frame, bg='black')
        header_frame.pack(fill=tk.X, padx=5, pady=(20, 5))

        header_frame.grid_columnconfigure(0, weight=3)
        header_frame.grid_columnconfigure(1, weight=7)
        header_frame.grid_columnconfigure(2, weight=1)
        header_frame.grid_columnconfigure(3, weight=2, minsize=120)
        header_frame.grid_rowconfigure(0, minsize=40)

        header_kode = tk.Label(header_frame, text='Kode barang', bg='black', fg='white', font=self.__font_default, anchor='w', padx=10)
        header_kode.grid(row=0, column=0, sticky='news')

        header_nama = tk.Label(header_frame, text='Nama barang', bg='black', fg='white', font=self.__font_default, anchor='w', padx=10)
        header_nama.grid(row=0, column=1, sticky='news')

        header_kuantiti = tk.Label(header_frame, text='Kuantiti', bg='black', fg='white', font=self.__font_default, anchor='w', padx=10)
        header_kuantiti.grid(row=0, column=2, sticky='news')

        header_kelola = tk.Label(header_frame, text='Kelola', bg='black', fg='white', font=self.__font_default, anchor='w', padx=10)
        header_kelola.grid(row=0, column=3, sticky='news')

        items = [
            ['KODE/001', 'Ban dalam OS', 11],
            ['KODE/002', 'Ban luar OS', 5],
            ['KODE/003', 'Ban dalam Kuning', 8],
            ['KODE/004', 'Ban dalam Merah', 15],
            ['KODE/005', 'Ban luar Hijau', 20],
            ['KODE/001', 'Ban dalam OS', 11],
            ['KODE/002', 'Ban luar OS', 5],
            ['KODE/003', 'Ban dalam Kuning', 8],
            ['KODE/004', 'Ban dalam Merah', 15],
            ['KODE/005', 'Ban luar Hijau', 20],
            ['KODE/001', 'Ban dalam OS', 11],
            ['KODE/002', 'Ban luar OS', 5],
            ['KODE/003', 'Ban dalam Kuning', 8],
            ['KODE/004', 'Ban dalam Merah', 15],
            ['KODE/005', 'Ban luar Hijau', 20],
            ['KODE/001', 'Ban dalam OS', 11],
            ['KODE/002', 'Ban luar OS', 5],
            ['KODE/003', 'Ban dalam Kuning', 8],
            ['KODE/004', 'Ban dalam Merah', 15],
            ['KODE/005', 'Ban luar Hijau', 20],
            ['KODE/001', 'Ban dalam OS', 11],
            ['KODE/002', 'Ban luar OS', 5],
            ['KODE/003', 'Ban dalam Kuning', 8],
            ['KODE/004', 'Ban dalam Merah', 15],
            ['KODE/005', 'Ban luar Hijau', 20],
            ['KODE/001', 'Ban dalam OS', 11],
            ['KODE/002', 'Ban luar OS', 5],
            ['KODE/003', 'Ban dalam Kuning', 8],
            ['KODE/004', 'Ban dalam Merah', 15],
            ['KODE/005', 'Ban luar Hijau', 20],
            ['KODE/001', 'Ban dalam OS', 11],
            ['KODE/002', 'Ban luar OS', 5],
            ['KODE/003', 'Ban dalam Kuning', 8],
            ['KODE/004', 'Ban dalam Merah', 15],
            ['KODE/005', 'Ban luar Hijau', 20],
            ['KODE/001', 'Ban dalam OS', 11],
            ['KODE/002', 'Ban luar OS', 5],
            ['KODE/003', 'Ban dalam Kuning', 8],
            ['KODE/004', 'Ban dalam Merah', 15],
            ['KODE/005', 'Ban luar Hijau', 20]
        ]

        for index, item in enumerate(items):
            self.__create_row__(header_frame, index + 1, item)

    def __create_row__(self, parent, row, item):
        if (row % 2 == 0):
            bg_color = '#eee'
        else:
            bg_color = 'white'

        parent.grid_rowconfigure(row, minsize=40)

        kode_label = tk.Label(parent, text=item[0], bg=bg_color, font=self.__font_default, anchor='w', padx=10)
        kode_label.grid(row=row, column=0, sticky='news')

        nama_label = tk.Label(parent, text=item[1], bg=bg_color, font=self.__font_default, anchor='w', padx=10)
        nama_label.grid(row=row, column=1, sticky='news')

        kuantiti_label = tk.Label(parent, text=item[2], bg=bg_color, font=self.__font_default, anchor='w', padx=10)
        kuantiti_label.grid(row=row, column=2, sticky='news')

        kelola_label = tk.Label(parent, text='Kelola', bg=bg_color, font=self.__font_default, anchor='w', padx=10)
        kelola_label.grid(row=row, column=3, sticky='news')

    def __tambah_barang_baru__(self):
        print('Tambah')

    def __hapus_barang__(self):
        print('Hapus')

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()