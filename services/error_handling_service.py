
from exceptions import TicketException
from requests.exceptions import RequestException
import sys


class ErrorHandlingService:

    def __init__(self):
        pass

    def load_ticket_handler(self, response):
        if response.status_code == 401:
            print(
                'Oops! Authorization failed. Please check your credentials and restart the program.')
            sys.exit(1)  # need to mock
        elif response.status_code == 404:
            print('Ticket not found. Please check ticket ID.')
            raise TicketException

        print('Unable to load tickets.')
        sys.exit(1)
