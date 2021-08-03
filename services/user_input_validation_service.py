from exceptions import TicketException


class UserInputValidationService:

    def __init__(self):
        pass

    def validate_main_menu_input(self, user_input):

        if user_input not in ['1', '2', 'q']:
            print('Invalid input. Please select from available options.')
            return

    def validate_view_single_ticket_input(self, user_input):
        try:
            int(user_input)
            return
        except ValueError:
            print('Please enter a valid integer ticket ID.')
            raise TicketException

    def validate_display_tickets_input(self, user_input, current_page, total_pages):

        if user_input not in ['n', 'm', 'p']:
            print('Invalid input, please select from the available options.')
            return
        if current_page == total_pages and user_input == 'n':
            print('Already on last page, no next page available.')
            return
        if current_page == 1 and user_input == 'p':
            print('Already on first page, no previous page available.')
            return
        if user_input == 'm':
            return
