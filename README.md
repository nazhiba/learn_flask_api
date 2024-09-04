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






