import services.user_input_validation_service as user_input_validation_service
from view.ticket_view import TicketView
import sys


class MainMenuView:
    def __init__(self):
        self.validation_service = user_input_validation_service.UserInputValidationService()

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
        try:
            user_input = input('Enter an option (or enter <q> to quit): ')
            self.validation_service.validate_main_menu_input(
                user_input=user_input)
        except Exception as e:
            print('\nInvalid input.')
            return
        if user_input == 'q':
            sys.exit()
        elif user_input == '1':
            TicketView().display_tickets()
        elif user_input == '2':
            TicketView().display_single_ticket()
            # TODO: Create specific exception for unexpected input
