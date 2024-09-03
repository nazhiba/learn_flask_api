from flask import Flask
aplikasi = Flask(__name__)

@aplikasi.route('/')
def index():
     return "hello world"

@aplikasi.route('/<nama>')
def cetak_nama(nama):
     return f"Hallo {nama}"


if __name__ == "__main__":
     aplikasi.run(debug=True)
