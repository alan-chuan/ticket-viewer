from services.user_input_validation_service import UserInputValidationService
import unittest


class Test(unittest.TestCase):
    def test_invalid_input_mm(self):
        with self.assertRaises(Exception):
            UserInputValidationService().validate_main_menu_input('ABCDE')

    def test_valid_input_mm(self):
        try:
            UserInputValidationService().validate_main_menu_input('1')
            UserInputValidationService().validate_main_menu_input('2')
            UserInputValidationService().validate_main_menu_input('q')
        except Exception:
            assert False

    def test_invalid_input_single_ticket(self):
        with self.assertRaises(ValueError):
            UserInputValidationService().validate_view_single_ticket_input('A')
        with self.assertRaises(ValueError):
            UserInputValidationService().validate_view_single_ticket_input('391.2')

    def test_valid_input_single_ticket(self):
        try:
            UserInputValidationService().validate_view_single_ticket_input('1143')
            UserInputValidationService().validate_view_single_ticket_input('21')
            UserInputValidationService().validate_view_single_ticket_input('3901')
        except Exception:
            assert False

    def test_invalid_input_view_all_ticket(self):
        invalid_inputs = ['A', '143.1', '+`2', ' ', '\n', '#$$$']
        for input in invalid_inputs:
            with self.assertRaises(Exception):
                UserInputValidationService().validate_display_tickets_input(input)

    def test_valid_input_view_all_ticket(self):
        try:
            UserInputValidationService().validate_display_tickets_input('n')
            UserInputValidationService().validate_display_tickets_input('p')
            UserInputValidationService().validate_display_tickets_input('m')
        except Exception:
            assert False


if __name__ == '__main__':
    unittest.main()
