import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT
from datetime import datetime
from db import Database

class Vacation_handler: 
    @staticmethod
    def save_vacation_request(user_id, start_date, end_date, reason):
        conn = Database.get_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(
                    'INSERT INTO vacation_requests (user_id, start_date, end_date, reason) VALUES (%s, %s, %s, %s)',
                    (user_id, start_date, end_date, reason)
                )
                conn.commit()
                cur.close()
            except psycopg2.Error as e:
                print(f"Error saving the vacation request: {e}")
            finally:
                conn.close()

    @staticmethod
    # Check if the vacation dates overlap with existing ones
    def has_overlapping_vacation(user_id, new_start_date, new_end_date):
        existing_vacations = Vacation_handler.get_vacation_days(user_id)
        
        for start_date, end_date in existing_vacations:
            # Check if the new vacation overlaps with any existing vacation
            if (new_start_date >= start_date and new_start_date <= end_date) or \
            (new_end_date >= start_date and new_end_date <= end_date) or \
            (new_start_date <= start_date and new_end_date >= end_date):
                return True
        return False


    @staticmethod
    def get_vacation_days(user_id):
        conn = Database.get_connection()
        if conn:
            try:
                cur = conn.cursor()
                query = 'SELECT start_date, end_date FROM vacation_requests WHERE user_id = %s'
                cur.execute(query, (user_id,))
                results = cur.fetchall()
                return results
            except psycopg2.Error as e:
                print(f"Error fetching vacation days: {e}")
            finally:
                conn.close()
        return []

   
