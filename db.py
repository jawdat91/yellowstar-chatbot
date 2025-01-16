import cx_Oracle
import os
import cx_Oracle
from config import DB_USER, DB_PASSWORD,DSN


class Database:
    @staticmethod
    def get_connection():
        try:
            conn = cx_Oracle.connect(
                user=DB_USER,
                password=DB_PASSWORD,
                dsn=DSN
            )
            return conn
        except cx_Oracle.Error as e:
            print(f"Error connecting to the Oracle database: {e}")
            return None


  
    @staticmethod
    def get_user_by_telegram_id(telegram_id):
        conn = Database.get_connection()
        if conn:
            try:
                cur = conn.cursor()
                query = 'SELECT ID, FIRST_NAME, LAST_NAME FROM EMPLOYEES WHERE TELEGRAM_ID = :telegram_id'
                cur.execute(query, (str(telegram_id),))
                user = cur.fetchone()
                if user:
                    user_id, first_name, last_name = user
                    username = f"{first_name} {last_name}"  # Combine for use as username
                    return user_id, username 
                else:
                    return None
            except cx_Oracle.Error as e:
                print(f"Error fetching user: {e}")
            finally:
                conn.close()
        return None
