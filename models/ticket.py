class Ticket:
    '''
    This class represents a ticket
    '''

    def __init__(self, id, subject, description):
        self.id = id
        self.subject = subject
        self.description = description

    def get_ticket_details(self, display_mode):
        if display_mode == 'summary':
            return f'Ticket ID: {self.id}, Subject: {self.subject}'
        elif display_mode == 'detailed':
            return f'Ticket ID: {self.id}\nSubject: {self.subject}\nDescription: {self.description}'
