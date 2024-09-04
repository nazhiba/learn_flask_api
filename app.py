from flask import Flask, request, jsonify

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

@aplikasi.route('/books', methods=['GET','POST'])
def books():
     if request.method == "GET":
          if (len(list_buku)) > 0:
               return jsonify(list_buku)
          else:
               return "Tidak ditemukan", 404
     elif request.method == "POST":
          new_penulis = request.form["penulis"]
          new_bahasa = request.form["bahasa"]
          new_judul = request.form["judul"]
          new_deskripsi = request.form["deskripsi"]
          ID = list_buku[-1]['id']+1

          new_objek = {
               "id":ID,
               "penulis":new_penulis,
               "bahasa":new_bahasa,
               "judul":new_judul,
               "deskripsi":new_deskripsi
          }

          list_buku.append(new_objek)
          return jsonify(list_buku), 201

@aplikasi.route('/book/<int:id>', methods=["PUT","GET","DELETE"])
def satu_buku(id):
     if request.method == "GET":
          for buku in list_buku:
               if buku['id'] == id:
                    return jsonify(buku)
          return "Buku tidak ditemukan", 404
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
     aplikasi.run()
