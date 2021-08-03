import textwrap


class Ticket:
    '''
    This class represents a ticket
    '''

    def __init__(self, id, subject, description, created_at, submitter_id):
        self.id = id
        self.subject = subject
        self.description = description
        self.created_at = created_at
        self.submitter_id = submitter_id

    def get_summary(self):
        '''
        This method returns a summary of a ticket
        '''
        date, time = self.created_at.split('T')
        hour, minute, seconds = time.split(':')
        return f'Ticket ID: {self.id} [Subject: {self.subject}, Created on {date} at {hour}:{minute} by {self.submitter_id}]'

    def get_detailed(self):
        '''
        This method returns detailed information of a ticket
        '''
        return f'\nTicket ID: {self.id}\n\nSubject: {self.subject}\n\nDescription:\n{textwrap.fill(self.description, width=80)}\n'
