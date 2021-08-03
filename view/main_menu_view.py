from services.user_input_validation_service import UserInputValidationService
from view.ticket_view import TicketView
import sys


class MainMenuView:
    '''
        This class manages the main menu view.

        Methods
        ----------
        display_main_menu()
            displays the main menu to the user
    '''

    def __init__(self):
        self.validation_service = UserInputValidationService()

    def display_main_menu(self):
        """
        This function displays the main menu options
        """
        print('\n***********************************************')
        print('*********  Welcome to Ticket Viewer!  *********')
        print('***********************************************')
        print('Main Menu')
        print('Options:')
        print('[1] View all tickets')
        print('[2] View single ticket')

        user_input = input('Enter an option (or enter <q> to quit): ')
        self.validation_service.validate_main_menu_input(
            user_input=user_input)
        if user_input == 'q':
            sys.exit()
        elif user_input == '1':
            TicketView().display_tickets()
        elif user_input == '2':
            TicketView().display_single_ticket()
