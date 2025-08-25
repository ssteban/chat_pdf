import psycopg2 as bd
from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG: dict = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": "5432"
}

class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = bd.connect(**DB_CONFIG)
            print("Conexión a la base de datos exitosa")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Conexión a la base de datos cerrada")

    def get_connection(self):
        if not self.connection:
            self.connect()
        return self.connection

    def __enter__(self):
        self.connect()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

