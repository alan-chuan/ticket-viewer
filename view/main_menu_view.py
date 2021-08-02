import services.user_input_validation_service as user_input_validation_service
from services import ticket_service
import sys


class MainMenuView:
    def __init__(self):
        self.validation_service = user_input_validation_service.UserInputValidationService()
        self.ticket_service = None

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
            self.print_all_tickets()
        elif user_input == '2':
            # TODO: handle ticket loading service (single ticket)
            pass
            # TODO: Create specific exception for unexpected input

    def print_all_tickets(self):
        # handle ticket loading service (multiple tickets)
        self.ticket_service = ticket_service.TicketService()
        self.ticket_service.load_tickets_from_api(
            page_number=1, tickets_per_page=25)
        all_tickets = self.ticket_service.get_all_tickets()
        for ticket in all_tickets:
            print(ticket.get_ticket_details('summary'))
