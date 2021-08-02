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

    def load_tickets_from_api(self, page_number, tickets_per_page):
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
            r = self.session.get(f'https://{session_service.SessionService().subdomain}.zendesk.com/api/v2/tickets.json', params={
                'page': page_number, 'per_page': tickets_per_page})
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
        for item in ticket_list:
            # create a ticket object
            ticket = Ticket(item.get('id'), item.get(
                'subject'), item.get('description'))
            # append newly created ticket object to list
            self.tickets.append(ticket)

    def get_all_tickets(self):
        return self.tickets

    def load_single_ticket(self, subdomain, ticket_id):
        '''
        Loads a single ticket from a given subdomain

        Parameters
        ----------
            page_number : int
                page number to retrieve tickets from
            subdomain : int
                subdomain to query from
            ticket_id : int
                ticket id of the ticket to retrieve,

        '''
        try:
            r = self.session.get(
                f'https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}.json')
            r.raise_for_status()
        except Exception as e:
            print(e)
            # TODO: Implement proper error handling for HTTPErrors
