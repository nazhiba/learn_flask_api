# How to Run Flask App?
## Dengan Environment Variabel
```python
from flask import Flask
aplikasi = Flask(__name__)

@aplikasi.route('/')
def index():
     return "hello world"
```
### if you using Windows OS, you need to write this command in your windows terminal (make sure you in the correct directory)

```shell
set FLASK_APP=app.py
```

### dan jalankan command berikut

```shell
flask run
```

## Dengan Progammatically

### untuk menjalankan program secara terprogram anda perlu menambahkan ```aplikasi.run()``` dan menambahkan script ```if __name__ == "__main__"``` (ini memastikan bahwa ```aplikasi.run()``` dijalankan hanya saat file app.py dijalankan). berikut contoh programnya

```python
from flask import Flask
aplikasi = Flask(__name__)

@aplikasi.route('/')
def index():
     return "hello world"


if __name__ == "__main__":
     aplikasi.run()
```

### lalu jalakan

```python
python app.py
```

# Dynamic Routing

## contoh kode
```python
from flask import Flask
aplikasi = Flask(__name__)

@aplikasi.route('/')
def index():
     return "hello world"

# KODE BARU YANG DITAMBAHKAN
@aplikasi.route('/<nama>')
def cetak_nama(nama):
     return f"Hallo {nama}"


if __name__ == "__main__":
     aplikasi.run()
```

## Jalankan dan Open browser
### Open [http://127.0.0.1:5000/nazhiba](http://127.0.0.1:5000/nazhiba) maka akan ada tulisan Hallo nazhiba.kamu bisa merubah "/nazhiba" dengan namamu contoh [http://127.0.0.1:5000/namau](http://127.0.0.1:5000/namamu)

# Debugging di Flask

## Re-Loader
- melihat semua file yang dirubah
- sangat berguna saat devolopment
- intinya <mark>jika</mark> anda menggunakan kode <mark>terprogam</mark> tambahkan ```debug=True``` pada
  ```python
  if __name__ == "__main__":
     aplikasi.run(debug=True) # UPDATED CODE
  ```
- <mark>jika</mark> menggunakan <mark>environment variabel</mark> anda bisa menambahkan command di Terminal ```set FLASK_DEBUG=1``` (ingat 1 berarti True dan 0 adalah false)

## Debugger
- alat berbasis web
- interaktif
- intinya tinggal bikin kodenya error nanti bakal muncul error di web

# Flask Shell Command
```shell
flask --help
```

# Membuat REST API sederhana menggunakan Flask

## buat list data json
### contoh

```json
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
```

## lalu tambahkan ini dibawah list tersebut

```python
# dibawahnya
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
```
### fungsinya apa?
- #### kode ini akan melakukan GET(READ) semua id dan melakukan print list tersebut
  
- #### kode ini akan melakukan POST(CREATE) kolom baru dengan judul yang bisa anda tetukan, namun kekurangan dari kode ini adalah setiap data yang kalian tambahkan tidak akan tersimpan di program (list data json tidak bertambah otomatis). hal ini dikarenakan saat melakukan POST dengan data seperti ini data akan disimpan di memori alih alih menambahkannya ke list data json
### gimana solusinya?
#### nahh di readme selanjutnya kita akan belajar membuat database dari semua data yang kita miliki

## lalu tambahkan 
```python
# dibawahnya
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
```
### fungsinya apa?
#### besok lagi males ngetik





