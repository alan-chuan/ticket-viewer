from services.error_handling_service import ErrorHandlingService
from exceptions import TicketException
import unittest
from unittest.mock import patch
from requests.models import Response


class TestErrorHandlingService(unittest.TestCase):
    def test_authentication_error(self):
        response = Response()
        response.status_code = 401
        error_handling_service = ErrorHandlingService()
        with self.assertRaises(SystemExit) as cm:
            error_handling_service.load_ticket_handler(response)
            self.assertEqual(cm.exception.code, 1)

    def test_timeout_error(self):
        error_handling_service = ErrorHandlingService()
        with self.assertRaises(SystemExit) as cm:
            error_handling_service.timeout_error_handler()
            self.assertEqual(cm.exception.code, 1)

    def test_connection_error(self):
        error_handling_service = ErrorHandlingService()
        with self.assertRaises(SystemExit) as cm:
            error_handling_service.connection_error_handler()
            self.assertEqual(cm.exception.code, 1)
