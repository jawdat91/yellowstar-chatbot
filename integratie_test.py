import unittest
from datetime import datetime, timedelta
from db import Database
import unittest
from db import Database
from SickReport_handler import SickReport_handler
from Vacation_handler import Vacation_handler
from config import CLS_USER_ID,CLS_EMAIL,CLS_MANAGERID,CLS_TELEGRAM_ID,HR_EMAIL,USER_NAME

from email_service import EmailService

class IntegrationTest(unittest.TestCase):   
    @classmethod
    def setUpClass(cls):
        # Setup environment variables and establish a test connection
        cls.conn = Database.get_connection()
        cls.user_id = CLS_USER_ID  # Example user_id for tests
        cls.telegram_id = CLS_TELEGRAM_ID
        cls.manager_id = CLS_MANAGERID
        cls.email = CLS_EMAIL

    # Test retrieving a user based on telegram_id
    def test_get_user_by_telegram_id(self):
        user_id, username = Database.get_user_by_telegram_id(self.telegram_id)
        self.assertEqual(user_id, self.user_id)
        self.assertEqual(username, USER_NAME)

    # Test if an employee has already reported sick today"""
    def test_has_already_reported_sick(self):
    # Create a sick report
        SickReport_handler.save_sick_report(self.user_id)
        # Check if the report has been saved
        already_reported = SickReport_handler.has_already_reported_sick(self.user_id)
        self.assertTrue(already_reported)

    # Test saving a sick report for the employee
    def test_save_sick_report(self):
        result = SickReport_handler.save_sick_report(self.user_id)
        self.assertIsNone(result)  # Save function returns None if successful

   # Test saving a vacation request 
    def test_save_vacation_request(self):
        start_date = datetime.today()
        end_date = start_date + timedelta(days=7)
        state = "Requested"
        # Add a vacation request and check if the request has been saved        
        Vacation_handler.save_vacation_request(self.user_id, start_date, end_date, state)
        vacations = Vacation_handler.get_vacation_days(self.user_id)
        self.assertGreater(len(vacations), 0)
        
        # Verify that the saved data matches the entered data
        latest_vacation = vacations[0]
        self.assertEqual(latest_vacation[0].date(), start_date.date())
        self.assertEqual(latest_vacation[1].date(), end_date.date())
        self.assertEqual(latest_vacation[2], state)

    # Test for overlapping vacation requests
    def test_has_overlapping_vacation(self):
        # First, add a vacation request that can serve as an overlap
        initial_start_date = datetime.today()
        initial_end_date = initial_start_date + timedelta(days=7)
        Vacation_handler.save_vacation_request(self.user_id, initial_start_date, initial_end_date, "Requested")

        # Test with a new vacation request that overlaps with the first request
        start_date = initial_start_date + timedelta(days=3)  # Overlaps with the first request
        end_date = start_date + timedelta(days=4)
        
        overlapping = Vacation_handler.has_overlapping_vacation(self.user_id, start_date, end_date)
        self.assertTrue(overlapping)

    # Test for retrieving an employee's vacation overview    
    def test_get_vacation_overview(self):
        overview = Vacation_handler.get_vacation_overview(self.user_id)
        self.assertIn("Hier is een overzicht van je vakantiedagen:", overview)
    
    # Test retrieving the email addresses for HR and the manager
    def test_get_email_addresses(self):
        hr_email, manager_email = EmailService.get_email_addresses(self.user_id)
        self.assertEqual(hr_email, HR_EMAIL)
        self.assertEqual(manager_email, self.email)
    
    @classmethod
    # Clean up all test data
    def tearDownClass(cls):
        if cls.conn:
            cur = cls.conn.cursor()
            # Verwijder de testgegevens uit de database om te cleanen na de tests
            cur.execute("DELETE FROM SICK_RAPORTS WHERE EMPLOYEE_ID = :1", [cls.user_id])
            cur.execute("DELETE FROM HOLIDAY_FORM WHERE EMPLOYEE_ID = :1", [cls.user_id])
            cls.conn.commit()
            cls.conn.close()

if __name__ == "__main__":
    unittest.main()
