from flask import Flask, request, jsonify
import sqlite3

aplikasi = Flask(__name__)

list_buku = [
     {
          "id":0,
          "penulis":"Nadzib",
          "bahasa":"Indonesia",
          "judul":"Tutorial cara bernafas",
          "deskripsi":"Sebelum mengikuti tutorial ini anda harus memiliki beberapa Organ seperti Paru-Paru, Hidung, Faring, Epiglotis, Trakea dan Brongkus, dan Diafragma. Biasannya organ ini sudah ada secara Default pada tubuh manusia,namun untuk memastikan silahkan dicek jika tidak ada bisa langsung hubungi Informasi Layanan PLN: 123"
     },
     {
          "id":1,
          "penulis":"Nadzib",
          "bahasa":"Indonesia",
          "judul":"Tutorial cara bernafas",
          "deskripsi":"Sebelum mengikuti tutorial ini anda harus memiliki beberapa Organ seperti Paru-Paru, Hidung, Faring, Epiglotis, Trakea dan Brongkus, dan Diafragma. Biasannya organ ini sudah ada secara Default pada tubuh manusia,namun untuk memastikan silahkan dicek jika tidak ada bisa langsung hubungi Informasi Layanan PLN: 123"
     },
     {
          "id":2,
          "penulis":"Nadzib",
          "bahasa":"Indonesia",
          "judul":"Tutorial cara bernafas",
          "deskripsi":"Sebelum mengikuti tutorial ini anda harus memiliki beberapa Organ seperti Paru-Paru, Hidung, Faring, Epiglotis, Trakea dan Brongkus, dan Diafragma. Biasannya organ ini sudah ada secara Default pada tubuh manusia,namun untuk memastikan silahkan dicek jika tidak ada bisa langsung hubungi Informasi Layanan PLN: 123"
     },
     {
          "id":3,
          "penulis":"Nadzib",
          "bahasa":"Indonesia",
          "judul":"Tutorial cara bernafas",
          "deskripsi":"Sebelum mengikuti tutorial ini anda harus memiliki beberapa Organ seperti Paru-Paru, Hidung, Faring, Epiglotis, Trakea dan Brongkus, dan Diafragma. Biasannya organ ini sudah ada secara Default pada tubuh manusia,namun untuk memastikan silahkan dicek jika tidak ada bisa langsung hubungi Informasi Layanan PLN: 123"
     }
]

def koneksi_php():
     koneksi = None
     try:
          koneksi = sqlite3.connect('buku.sqlite')
     except sqlite3.Error as e:
          print(e)
     return koneksi


@aplikasi.route('/books', methods=['GET','POST'])
def books():
     koneksi = koneksi_php()
     kursor = koneksi.cursor()

     if request.method == "GET":
          kursor = koneksi.execute("SELECT * FROM book")
          buku = [
               dict(id=row[0], penulis=row[1], bahasa=row[2], judul=row[3], deskripsi=row[4])
               for row in kursor.fetchall()
          ]
          if buku is not None:
               return jsonify(buku)

     elif request.method == "POST":
          new_penulis = request.form["penulis"]
          new_bahasa = request.form["bahasa"]
          new_judul = request.form["judul"]
          new_deskripsi = request.form["deskripsi"]
          
          sql_permintaan = """INSERT INTO book (penulis, bahasa, judul, deskripsi)
                              VALUES (? ,? ,?, ?)"""
          kursor = kursor.execute(sql_permintaan, (new_penulis, new_bahasa, new_judul, new_deskripsi))
          koneksi.commit()

          return f"Buku dengan id : {kursor.lastrowid} berhasil dibuat", 201

@aplikasi.route('/book/<int:id>', methods=["PUT","GET","DELETE"])
def satu_buku(id):
     koneksi = koneksi_php()
     kursor = koneksi.cursor()
     buku = None

     if request.method == "GET":
          kursor.execute("SELECT * FROM book WHERE id=?",(id,))
          rows = kursor.fetchall()
          for r in rows:
               buku = r
          if buku is not None:
               return jsonify(buku), 200
          else:
               return "Ada yang salah", 404          
     elif request.method == "PUT":
          for buku in list_buku:
               if buku['id'] == id:
                    buku['penulis'] = request.json['penulis']
                    buku['bahasa'] = request.json['bahasa']
                    buku['judul'] = request.json['judul']
                    buku['deskripsi'] = request.json['deskripsi']
                    updated_buku = {
                         'id':id,
                         'penulis':buku['penulis'],
                         'bahasa':buku['bahasa'],
                         'judul':buku['judul'],
                         'deskripsi':buku['deskripsi']
                    }
                    return jsonify(updated_buku)
          return "Buku tidak ditemukan", 404
     elif request.method == "DELETE":
          for index, buku in enumerate(list_buku):
               if buku['id'] == id:
                    list_buku.pop(index)
                    return jsonify(list_buku)
          return "Buku tidak ditemukan", 404

if __name__ == "__main__":
     aplikasi.run(debug= True)
