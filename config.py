import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",  # Host MySQL
        user="root",       # Username MySQL
        password="",  # Password MySQL
        database="sanke_db"  # Nama database yang digunakan
    )