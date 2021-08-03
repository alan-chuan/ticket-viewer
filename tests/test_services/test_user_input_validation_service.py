from exceptions import TicketException
from models.ticket import Ticket
from services import user_input_validation_service
from services.user_input_validation_service import UserInputValidationService
import unittest


class Test(unittest.TestCase):

    def test_valid_input_mm(self):
        user_input_validation_service = UserInputValidationService()
        try:
            for input in ['1', '2', 'q']:
                user_input_validation_service.validate_main_menu_input(input)
        except Exception:
            assert False

    def test_invalid_input_single_ticket(self):
        user_input_validation_service = UserInputValidationService()

        try:
            for input in ['A', '391.20', '`@_~']:
                with self.assertRaises(TicketException):
                    user_input_validation_service.validate_view_single_ticket_input(
                        input)
        except Exception:
            assert False

    def test_valid_input_single_ticket(self):
        user_input_validation_service = UserInputValidationService()

        try:
            for input in ['1143', '21', '3901']:
                user_input_validation_service.validate_view_single_ticket_input(
                    input)
        except Exception:
            assert False

    def test_invalid_input_view_all_ticket(self):
        invalid_inputs = ['A', '143.1', '+`2', ' ',
                          '\n', '#$$$', '1093842', 'p', 'i', ]
        for input in invalid_inputs:
            with self.assertRaises(Exception):
                UserInputValidationService().validate_display_tickets_input(input)


if __name__ == '__main__':
    unittest.main()
