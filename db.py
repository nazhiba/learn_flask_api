import sqlite3
koneksi = sqlite3.connect('buku.sqlite')
kursor = koneksi.cursor()
sql_permintaan = """CREATE TABLE book (
     id integer PRIMARY KEY,
     penulis text NOT NULL,
     bahasa text NOT NULL,
     judul text NOT NULL,
     deskripsi text NOT NULL
)"""

kursor.execute(sql_permintaan)