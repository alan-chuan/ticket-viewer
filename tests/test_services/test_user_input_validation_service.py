from services.user_input_validation_service import UserInputValidationService
import unittest


class Test(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaises(Exception):
            UserInputValidationService().validate_main_menu_input('ABCDE')

    def test_valid_input(self):
        try:
            UserInputValidationService().validate_main_menu_input('1')
            UserInputValidationService().validate_main_menu_input('2')
            UserInputValidationService().validate_main_menu_input('q')
        except Exception:
            assert False


if __name__ == '__main__':
    unittest.main()
