from flask import Flask, request
from fuzzy import hitung_kualitas_air
import mysql.connector
from config import connect_db
from datetime import datetime

app = Flask(__name__)

@app.route('/kualitas-air', methods=['GET', 'POST'])
def kualitas_air():
    # Menggunakan request.form, bukan request.from
    suhu = float(request.form['suhu'])
    ph = float(request.form['ph'])
    id_alat = int(request.form['id_alat'])

    
    # Menghitung kualitas air
    kualitas = hitung_kualitas_air(ph, suhu)
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Membuka koneksi ke database
    db = connect_db()
    cursor = db.cursor()
    
    # Memasukkan data ke tabel kualitas_air
    sql = "INSERT INTO kualitas_air (ph, suhu, id_alat, label, created_at) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (ph, suhu, id_alat, kualitas, timestamp))
    
    # Commit perubahan
    db.commit()

    # Menutup koneksi database
    cursor.close()
    db.close()

    return 'Data berhasil disimpan', 200

if __name__ == '__main__':
    app.run(debug=True)
