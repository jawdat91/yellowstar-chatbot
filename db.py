import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT
from datetime import datetime

class Database:
    @staticmethod
    def get_connection():
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                port=DB_PORT
            )
            return conn
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")
            return None

    @staticmethod
    def get_user_by_telegram_id(telegram_id):
        conn = Database.get_connection()
        if conn:
            try:
                cur = conn.cursor()
                query = 'SELECT id, email FROM users WHERE telegram_id = %s'
                cur.execute(query, (str(telegram_id),))
                user = cur.fetchone()
                return user if user else None
            except psycopg2.Error as e:
                print(f"Error fetching user: {e}")
            finally:
                conn.close()
        return None
