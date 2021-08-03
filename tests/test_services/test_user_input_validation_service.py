from exceptions import TicketException
from models.ticket import Ticket
from services.user_input_validation_service import UserInputValidationService
import unittest


class Test(unittest.TestCase):

    def test_valid_input_mm(self):
        try:
            UserInputValidationService().validate_main_menu_input('1')
            UserInputValidationService().validate_main_menu_input('2')
            UserInputValidationService().validate_main_menu_input('q')
        except Exception:
            assert False

    def test_invalid_input_single_ticket(self):
        with self.assertRaises(TicketException):
            UserInputValidationService().validate_view_single_ticket_input('A')
        with self.assertRaises(TicketException):
            UserInputValidationService().validate_view_single_ticket_input('391.2')

    def test_valid_input_single_ticket(self):
        try:
            UserInputValidationService().validate_view_single_ticket_input('1143')
            UserInputValidationService().validate_view_single_ticket_input('21')
            UserInputValidationService().validate_view_single_ticket_input('3901')
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
