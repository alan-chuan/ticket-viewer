from services.error_handling_service import ErrorHandlingService
from exceptions import TicketException
import unittest
from unittest.mock import patch
from requests.models import Response


class TestErrorHandlingService(unittest.TestCase):

    def test_ticket_not_found(self):
        response = Response()
        response.status_code = 404
        error_handling_service = ErrorHandlingService()
        with self.assertRaises(TicketException):
            error_handling_service.load_ticket_handler(response)
            with self.assertRaises(SystemExit) as cm:
                error_handling_service.load_ticket_handler(response)
                self.assertEqual(cm.exception.code, 1)

    def test_authentication_error(self):
        response = Response()
        response.status_code = 401
        error_handling_service = ErrorHandlingService()
        with self.assertRaises(SystemExit) as cm:
            error_handling_service.load_ticket_handler(response)
        self.assertEqual(cm.exception.code, 1)
