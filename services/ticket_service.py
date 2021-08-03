import services.error_handling_service
from . import session_service
from models.metadata import Metadata
from models.ticket import Ticket
from exceptions import *
from . import error_handling_service


class TicketService:
    '''
    This class is used to manage tickets retrieved

    Methods
    -------
    load_tickets(page_number, subdomain, tickets_per_page):
        loads tickets of a given page

    load_single_ticket(subdomain, ticket_id):
        load a single ticket
    '''

    def __init__(self):

        self.tickets = []
        self.metadata = None
        self.session = session_service.SessionService().create_session()
        self.error_handling_service = error_handling_service.ErrorHandlingService()

    def get_ticket_list(self, page_number, tickets_per_page):
        '''
        Returns all tickets of a given page

        Parameters
        ----------
            page_number : int
                page number to retrieve tickets from
            tickets_per_page : int
                tickets to display in a page
        Returns
        ----------
            The list of tickets retrieved

        '''
        # Phase 1: Load all tickets from API
        try:
            r = self.load_all_tickets(page_number, tickets_per_page)
        except TimeoutError:
            self.error_handling_service.handle_timeout_error()
        except Exception:
            self.error_handling_service.connection_error_handler()
        try:
            r.raise_for_status()
        except Exception as e:
            self.error_handling_service.load_ticket_handler(r)
            return
        # Phase 2: Parse retrieved data
        data = r.json()
        self.parse_all_tickets(data)

        # Return after parsing successfully
        return self.tickets

    def load_all_tickets(self, page_number, tickets_per_page):
        '''
        Loads all tickets of a given page from Zendesk Tickets API

        Parameters
        ----------
            page_number : int
                page number to retrieve tickets from
            tickets_per_page : int
                tickets to display in a page
        Returns
        ----------
            Response object
        '''
        return self.session.get(f'https://{session_service.SessionService().subdomain}.zendesk.com/api/v2/tickets.json', params={
            'page': page_number, 'per_page': tickets_per_page})

    def parse_all_tickets(self, data):
        '''
        Loads all tickets of a given page from Zendesk Tickets API

        Parameters
        ----------
            data : json
                the data to parse

        '''
        # extract metadata from API call
        next_page = data.get('next_page')
        previous_page = data.get('previous_page')
        count = data.get('count')
        # create a metadata object
        self.metadata = Metadata(next_page, previous_page, count)
        # get list of tickets
        ticket_list = data.get('tickets')
        # for every ticket json object
        self.tickets = []
        for item in ticket_list:
            # create a ticket object
            ticket = self.parse_single_ticket(item)
            # append newly created ticket object to list
            self.tickets.append(ticket)

    def get_single_ticket(self, ticket_id):
        '''
        Retrieves a single ticket with ticket_id

        Parameters
        ----------
            ticket_id : int
                ticket id of the ticket to retrieve
        Returns
        ----------
        Ticket string in detailed format
        '''
        # Phase 1: Load all tickets from API
        try:
            r = self.load_single_ticket(ticket_id)
        except TimeoutError:
            self.error_handling_service.timeout_error_handler()
        except Exception:
            self.error_handling_service.connection_error_handler()
        try:
            r.raise_for_status()
        except Exception as e:
            self.error_handling_service.load_ticket_handler(r)
            return
        data = r.json()
        # Phase 2: Parse retrieved data
        ticket = self.parse_single_ticket(data.get('ticket'))
        # Return after parsing successfully
        return ticket.get_detailed()

    def load_single_ticket(self, ticket_id):
        return self.session.get(
            f'https://{session_service.SessionService().subdomain}.zendesk.com/api/v2/tickets/{ticket_id}.json')

    def parse_single_ticket(self, data):
        '''
        Parses a single ticket

        Parameters
        ----------
            data : json
                single ticket json object
        Returns
        ----------
        Ticket object
        '''
        try:
            id = data.get('id')
            subject = data.get('subject')
            description = data.get('description')
            created_at = data.get('created_at')
            submitter_id = data.get('submitter_id')
            return Ticket(id, subject, description, created_at, submitter_id)
        except AttributeError:
            print(
                'Error getting an attribute, the ticket JSON object which was requested might have changed.')
