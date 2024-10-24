import psycopg2
from datetime import datetime
from db import Database

class SickReport_handler :
    @staticmethod
    def has_already_reported_sick(user_id):
        conn = Database.get_connection()
        if conn:
            date = datetime.now().strftime("%Y-%m-%d")
            try:
                cur = conn.cursor()
                cur.execute('SELECT id FROM sick_reports WHERE user_id = %s AND date = %s', (user_id, date))
                result = cur.fetchone()
                return True if result else False
            except psycopg2.Error as e:
                print(f"Error checking for existing sick report: {e}")
            finally:
                conn.close()
        return False

    @staticmethod
    def save_sick_report(user_id):
        conn = Database.get_connection()
        if conn:
            date = datetime.now().strftime("%Y-%m-%d")
            try:
                cur = conn.cursor()
                cur.execute('INSERT INTO sick_reports (user_id, date, reason) VALUES (%s, %s, %s)', (user_id, date, "Ziek gemeld"))
                conn.commit()
                cur.close()
            except psycopg2.Error as e:
                print(f"Error saving the sick report: {e}")
            finally:
                conn.close()
