
class Metadata:
    '''
    This class represents the metadata from a Ticket API call
    '''

    def __init__(self, next_page, previous_page, count):
        self.next_page = next_page
        self.previous_page = previous_page
        self.count = count
