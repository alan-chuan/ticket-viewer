from exceptions import TicketException


class UserInputValidationService:
    '''
    This class validates user input and displays an appropriate message
    '''

    def __init__(self):
        pass

    def validate_main_menu_input(self, user_input):
        '''
        This method validates user inputs from the main menu.
        Parameters
        ----------
            user_input: str
                user's input
        '''
        if user_input not in ['1', '2', 'q']:
            print('Invalid input. Please select from available options.')
            return

    def validate_view_single_ticket_input(self, user_input):
        '''
        This method validates the ticket ID entered is an integer.
        Parameters
        ----------
            user_input: str
                user's input
        Raises
        ----------
            TicketException if the user_input is not a valid integer.
        '''
        try:
            int(user_input)
            return
        except ValueError:
            print('Please enter a valid integer ticket ID.')
            raise TicketException

    def validate_display_tickets_input(self, user_input, current_page, total_pages):
        '''
        This method validates the input entered under [View all tickets] option
        Parameters
        ----------
            user_input: str
                user's input
        '''
        if user_input not in ['n', 'm', 'p']:
            print('Invalid input, please select from the available options.')
            return
        if current_page == total_pages and user_input == 'n':
            print('Invalid input, please select from the available options.')
            return
        if current_page == 1 and user_input == 'p':
            print('Invalid input, please select from the available options.')
            return
        if user_input == 'm':
            return
