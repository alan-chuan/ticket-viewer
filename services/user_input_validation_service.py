class UserInputValidationService:

    def __init__(self):
        pass

    def validate_main_menu_input(self, user_input):

        if user_input in ['1', '2', 'q']:
            return

        else:
            raise Exception

    def validate_view_single_ticket_input(self, user_input):
        try:
            int(user_input)
            return
        except ValueError as e:
            raise ValueError(e)

    def validate_display_tickets_input(self, user_input):
        if user_input in ['n', 'p', 'm']:
            return
        else:
            raise Exception
