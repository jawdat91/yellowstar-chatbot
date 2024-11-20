import unittest
from unittest.mock import patch, MagicMock
import cx_Oracle
from db import Database
from SickReport_handler import SickReport_handler
from telegram_bot import TelegramBot
from Vacation_handler import Vacation_handler
from intent_analyzer import IntentAnalyzer
import os

# Tests for database connection
class TestDatabaseConnection(unittest.TestCase):
    @patch('cx_Oracle.connect')
    def test_db_connection_success(self, mock_connect):
        mock_connect.return_value = MagicMock()
        conn = Database.get_connection()
        self.assertIsNotNone(conn)

    @patch('cx_Oracle.connect')
    def test_db_connection_failure(self, mock_connect):
        mock_connect.side_effect = cx_Oracle.Error("Database connection error")
        conn = Database.get_connection()
        self.assertIsNone(conn)

# Tests for fetching user by Telegram ID
class TestGetUserByTelegramId(unittest.TestCase):
    @patch('cx_Oracle.connect')
    def test_get_user_by_telegram_id_success(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = (1, "John", "Doe")
        
        user = Database.get_user_by_telegram_id(12345)
        self.assertEqual(user, (1, "John Doe"))

    @patch('cx_Oracle.connect')
    def test_get_user_by_telegram_id_not_found(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None
        
        user = Database.get_user_by_telegram_id(12345)
        self.assertIsNone(user)

# Tests for checking existing sick report
class TestHasAlreadyReportedSick(unittest.TestCase):
    @patch('cx_Oracle.connect')
    def test_has_already_reported_sick_true(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = (1,)
        
        result = SickReport_handler.has_already_reported_sick(1)
        self.assertTrue(result)

    @patch('cx_Oracle.connect')
    def test_has_already_reported_sick_false(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None
        
        result = SickReport_handler.has_already_reported_sick(1)
        self.assertFalse(result)

# Tests for saving sick report
class TestSaveSickReport(unittest.TestCase):
    @patch('cx_Oracle.connect')
    def test_save_sick_report(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor       
        SickReport_handler.save_sick_report(1)
        mock_cursor.execute.assert_called_once()
        args, _ = mock_cursor.execute.call_args
        query = args[0]
        self.assertIn("INSERT INTO SICK_RAPORTS", query)
        self.assertIn("VALUES (:user_id, TRUNC(SYSDATE), 'Ziek gemeld')", query)

# Tests for intent analysis
class TestAnalyzeIntent(unittest.TestCase):
    def test_analyze_intent_greeting(self):
        result = IntentAnalyzer.analyze_intent("hallo")
        self.assertEqual(result, "greeting")

    def test_analyze_intent_sick(self):
        result = IntentAnalyzer.analyze_intent("Ik ben ziek")
        self.assertEqual(result, "sick")

    def test_analyze_intent_vacation(self):
        result = IntentAnalyzer.analyze_intent("Ik wil vakantie aanvragen")
        self.assertEqual(result, "vacation")

    def test_analyze_intent_vacation_overview(self):
        result = IntentAnalyzer.analyze_intent("geef mij een overzicht van mijn vakantiedagen")
        self.assertEqual(result, "vacation_overview")

    def test_analyze_intent_unknown(self):
        result = IntentAnalyzer.analyze_intent("Wat is het weer vandaag?")
        self.assertEqual(result, "unknown")

# Tests for sending a message via Telegram
class TestSendMessage(unittest.TestCase):
    @patch('requests.post')
    def test_send_message(self, mock_post):
        chat_id = 12345
        text = "Testbericht"
        
        TelegramBot.send_message(chat_id, text)
        
        mock_post.assert_called_once_with(
            f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage",
            json={'chat_id': chat_id, 'text': text}
        )


    @patch('cx_Oracle.connect')
    def test_save_vacation_request(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        Vacation_handler.save_vacation_request(1, "2025-01-01", "2025-01-07", "Vakantie")

        # Extract the actual query that was executed
        mock_cursor.execute.assert_called_once()
        args, _ = mock_cursor.execute.call_args
        query = args[0]

        # check if key parts of the query are present
        self.assertIn("INSERT INTO HOLIDAY_FORM", query)
        self.assertIn("VALUES (:user_id, :start_date, :end_date, :reason, 'Requested')", query)


    # test overlapping vacation
    @patch('cx_Oracle.connect')
    def test_has_overlapping_vacation(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [("2025-01-01", "2025-01-10")]
        
        result = Vacation_handler.has_overlapping_vacation(1, "2025-01-05", "2025-01-07")
        self.assertTrue(result)

    # test no overlapping vacation   
    @patch('cx_Oracle.connect')
    def test_no_overlapping_vacation(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [("2025-01-01", "2025-01-10")]
        
        result = Vacation_handler.has_overlapping_vacation(1, "2025-01-11", "2025-01-15")
        self.assertFalse(result)

# Entry point for the test runner
if __name__ == '__main__':
    unittest.main()
