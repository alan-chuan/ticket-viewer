from . import session_service
from models.metadata import Metadata
from models.ticket import Ticket


class TicketService:
    '''
    This class is used to managed tickets retrieved

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

    def parse_tickets(self, page_number, tickets_per_page):
        '''
        Loads all tickets of a given page

        Parameters
        ----------
            page_number : int
                page number to retrieve tickets from
            tickets_per_page : int
                tickets to display in a page

        '''
        try:
            r = self.load_all_tickets(page_number, tickets_per_page)
            r.raise_for_status()
        except Exception as e:
            print(e)
            # TODO: Implement proper error handling for HTTPErrors
        data = r.json()
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
            ticket = Ticket(item.get('id'), item.get(
                'subject'), item.get('description'))
            # append newly created ticket object to list
            self.tickets.append(ticket)

    def load_all_tickets(self, page_number, tickets_per_page):
        return self.session.get(f'https://{session_service.SessionService().subdomain}.zendesk.com/api/v2/tickets.json', params={
            'page': page_number, 'per_page': tickets_per_page})

    def get_ticket_list(self, page_number, tickets_per_page):
        self.parse_tickets(page_number, tickets_per_page)
        return self.tickets

    def get_single_ticket(self, ticket_id):
        '''
        Gets and returns a single ticket instance

        Parameters
        ----------
            ticket_id : int
                ticket id of the ticket to retrieve

        '''
        return self.parse_single_ticket(ticket_id)

    def parse_single_ticket(self, ticket_id):
        '''
        Loads a single ticket from a given subdomain

        Parameters
        ----------
            page_number : int
                page number to retrieve tickets from
            ticket_id : int
                ticket id of the ticket to retrieve
        '''
        try:
            r = self.load_single_ticket(ticket_id)
            r.raise_for_status()
        except Exception as e:
            print(e)
            # TODO: Implement proper error handling for HTTPErrors
        data = r.json()
        ticket_data = data.get('ticket')
        ticket = Ticket(ticket_data.get('id'), ticket_data.get(
            'subject'), ticket_data.get('description'))
        return ticket.get_detailed()

    def load_single_ticket(self, ticket_id):
        return self.session.get(
            f'https://{session_service.SessionService().subdomain}.zendesk.com/api/v2/tickets/{ticket_id}.json')
