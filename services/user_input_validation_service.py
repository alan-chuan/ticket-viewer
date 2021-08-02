class UserInputValidationService:

    def __init__(self):
        pass

    def validate_main_menu_input(self, user_input):

        if user_input in ['1', '2', 'q']:
            return

        else:
            raise Exception
