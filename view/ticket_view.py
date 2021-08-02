from services.ticket_service import TicketService
from services.user_input_validation_service import UserInputValidationService


class TicketView:
    validation_service: UserInputValidationService
    ticket_service: TicketService = None
    ticket_list: list = None

    def __init__(self):
        # handle ticket loading service (multiple tickets)
        self.ticket_service = TicketService()
        self.ticket_list = self.ticket_service.get_ticket_list(
            page_number=1, tickets_per_page=25)
        self.validation_service = UserInputValidationService()

    def display_tickets(self):
        for ticket in self.ticket_list:
            print(ticket.get_summary())

    def display_single_ticket(self, ticket_id):
        print(self.ticket_service.get_single_ticket(ticket_id)
              )
