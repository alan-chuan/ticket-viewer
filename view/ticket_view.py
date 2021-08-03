from requests import exceptions
from services.ticket_service import TicketService
from services.user_input_validation_service import UserInputValidationService
from exceptions import TicketException
import math


class TicketView:
    '''
        This class manages the view that is displayed if the user selects option [1] or [2] from the main menu.

        Methods
        ----------
        display_tickets():
            display all tickets
        display_single()
            display a single ticket
    '''

    def __init__(self):
        # handle ticket loading service
        self.ticket_service = TicketService()
        self.validation_service = UserInputValidationService()
        self.ticket_list = []

    def display_tickets(self):  # Option 1
        '''
        This method displays all tickets when user selects option 1 from the main menu
        '''
        current_page = 1
        tickets_per_page = 25
        while True:
            print("\n***** View all tickets *****")
            # call ticket_service.get_ticket_list to get a list of tickets
            self.ticket_list = self.ticket_service.get_ticket_list(
                page_number=current_page, tickets_per_page=tickets_per_page)
            if self.ticket_list is None:
                print('Unable to retrieve ticket list. Check your subdomain url.')
                return

            if len(self.ticket_list) == 0:
                print('No tickets found. All your customers are happy! :)')
                return
            else:
                for ticket in self.ticket_list:
                    print(ticket.get_summary())
                total_pages = self.ticket_service.metadata.count/tickets_per_page
                print(
                    f'\nCurrent page: {current_page}, Total pages: {math.ceil(total_pages)}')
                print(f'Options:')
                if current_page != 1:
                    print('[p] <- Previous Page')
                if current_page != total_pages:
                    print('[n] Next Page ->')
                print('[m] Return to Main Menu')
                user_input = input('Enter an option: ')
                # validate user input
                self.validation_service.validate_display_tickets_input(
                    user_input=user_input, current_page=current_page, total_pages=total_pages)
                if user_input == 'p':
                    if current_page > 1:
                        current_page -= 1
                elif user_input == 'n':
                    if current_page < total_pages:
                        current_page += 1
                if user_input == 'm':
                    break

    def display_single_ticket(self):
        '''
        This method displays a single tickets when user selects option 2 from the main menu
        '''
        user_input = input('Enter ticket ID: ')
        try:
            self.validation_service.validate_view_single_ticket_input(
                user_input=user_input)
            print(
                '==================================================================================')
            ticket = self.ticket_service.get_single_ticket(
                ticket_id=user_input)
            if ticket is not None:
                print(ticket)
            print(
                '==================================================================================')
        except TicketException as e:
            return
