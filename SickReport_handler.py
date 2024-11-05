from db import Database
from datetime import datetime
import cx_Oracle

class SickReport_handler :
    @staticmethod
    def has_already_reported_sick(user_id):
        conn = Database.get_connection()
        if conn:
            cur = conn.cursor()
            query = '''SELECT SEQ FROM SICK_RAPORTS 
                        WHERE EMPLOYEE_ID = :user_id 
                        AND STARTDATE = TRUNC(SYSDATE)'''
            try:
                cur.execute(query, [user_id])
                result = cur.fetchone()
                return True if result else False
            except cx_Oracle.Error as e:
                print(f"Error checking for existing sick report: {e}")
            finally:
                conn.close()
        return False

    @staticmethod
    def save_sick_report(user_id):
        conn = Database.get_connection()
        if conn:
            try:
                cur = conn.cursor()
                query = '''INSERT INTO SICK_RAPORTS (EMPLOYEE_ID, STARTDATE, DESCRIPTION) 
                           VALUES (:user_id, TRUNC(SYSDATE), 'Ziek gemeld')'''
                cur.execute(query, [user_id])
                conn.commit()
            except cx_Oracle.Error as e:
                print(f"Error saving the sick report: {e}")
            finally:
                conn.close()
