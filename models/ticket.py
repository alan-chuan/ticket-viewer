class Ticket:
    '''
    This class represents a ticket
    '''
    id: int = None
    subject: str = None
    description: str = None

    def __init__(self, id: int, subject: str, description: str):
        self.id = id
        self.subject = subject
        self.description = description

    def get_summary(self):
        return f'Ticket ID: {self.id}, Subject: {self.subject}'

    def get_detailed(self):
        return f'Ticket ID: {self.id}\nSubject: {self.subject}\nDescription: {self.description}'
