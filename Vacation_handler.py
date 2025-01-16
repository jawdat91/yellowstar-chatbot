from datetime import datetime
from db import Database
import cx_Oracle

class Vacation_handler: 
    @staticmethod
    def save_vacation_request(user_id, start_date, end_date, reason):
        conn = Database.get_connection()
        if conn:
            try:
                cur = conn.cursor()
                query = '''INSERT INTO HOLIDAY_FORM (EMPLOYEE_ID, STARTDATE, ENDDATE, DESCRIPTION, STATE) 
                           VALUES (:user_id, :start_date, :end_date, :reason, 'Requested')'''
                cur.execute(query, [user_id, start_date, end_date, reason])
                conn.commit()
            except cx_Oracle.Error as e:
                print(f"Error saving the vacation request: {e}")
            finally:
                conn.close()


    @staticmethod
    def has_overlapping_vacation(user_id, new_start_date, new_end_date):
        existing_vacations = Vacation_handler.get_vacation_days(user_id)
        
        # Zorg ervoor dat de input datums `datetime.date` objecten zijn
        if isinstance(new_start_date, datetime):
            new_start_date = new_start_date.date()
        if isinstance(new_end_date, datetime):
            new_end_date = new_end_date.date()
        
        for row in existing_vacations:
            start_date = row[0].date() if isinstance(row[0], datetime) else row[0]
            end_date = row[1].date() if isinstance(row[1], datetime) else row[1]
            
            # Controleer op overlap
            if (new_start_date >= start_date and new_start_date <= end_date) or \
            (new_end_date >= start_date and new_end_date <= end_date) or \
            (new_start_date <= start_date and new_end_date >= end_date):
                return True
        return False
    


    @staticmethod
    def get_vacation_days(user_id):
        # Obtain a connection to the Oracle database
        conn = Database.get_connection()
        if conn:
            try:
                cur = conn.cursor()
                query = 'SELECT STARTDATE, ENDDATE, STATE FROM HOLIDAY_FORM WHERE EMPLOYEE_id = :1'
                cur.execute(query, (user_id,))
                results = cur.fetchall()
                return results

            except cx_Oracle.DatabaseError as e:
                error, = e.args
                print(f"Error fetching vacation days: {error.message}")
            
            finally:
                cur.close()
                conn.close()
        
        # Return an empty list if connection or query fails
        return []

    @staticmethod
    def get_vacation_overview(employee_id):

        conn = Database.get_connection()
        if conn:
            try:
                cur = conn.cursor()                
                vacation_requests = []
                vacation_days = Vacation_handler.get_vacation_days(employee_id)
                
                if vacation_days:
                    for start_date, end_date, request_state in vacation_days:
                        start_date_str = start_date.strftime('%Y-%m-%d') if start_date else "Onbekend"
                        end_date_str = end_date.strftime('%Y-%m-%d') if end_date else "Onbekend"
                        vacation_requests.append(f"Van {start_date_str} tot {end_date_str}  Status: {request_state}")
                else:
                    vacation_requests.append("Geen vakantieaanvragen gevonden.")

                # Retrieve vacation balances from the HOLIDAY table
                query_summary = '''SELECT HOLIDAY_YEAR, HOLIDAY_DAYS, BUILT_DAYS, ESTIMATED_DAYS, STARTING_BALANCE
                                   FROM HOLIDAY
                                   WHERE EMPLOYEE_ID = :employee_id
                                   ORDER BY HOLIDAY_YEAR DESC'''
                cur.execute(query_summary, [employee_id])
                summary_rows = cur.fetchall()

                # Build the summary of vacation days per year
                summary = ""
                for holiday_year, holiday_days, built_days, estimated_days, starting_balance in summary_rows:
                    summary += (f"\nVakantiejaar: {holiday_year}\n"
                                f"Vakantiedagen: {holiday_days}\n"
                                f"Gebouwde dagen: {built_days}\n"
                                f"Ingeschatte dagen: {estimated_days}\n"
                                f"Startsaldo: {starting_balance}\n")

                # Combine the vacation requests and the summary
                return "Hier is een overzicht van je vakantiedagen:\n" + "\n".join(vacation_requests) + "\n" + summary

            except cx_Oracle.DatabaseError as e:
                error, = e.args
                print(f"Database error: {error.message}")
                return f"Er is een fout opgetreden bij het ophalen van je vakantiedagen."

            finally:
                cur.close()
                conn.close()
        else:
            return "Kan geen verbinding maken met de database."