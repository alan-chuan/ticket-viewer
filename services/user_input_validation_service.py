class UserInputValidationService:

    def __init__(self):
        pass

    def validate_main_menu_input(self, user_input):

        if user_input not in ['1', '2', 'q']:
            raise Exception

    def validate_view_single_ticket_input(self, user_input):
        try:
            int(user_input)
            return
        except ValueError as e:
            raise ValueError(e)

    def validate_display_tickets_input(self, user_input):
        if user_input not in ['n', 'p', 'm']:
            raise Exception
