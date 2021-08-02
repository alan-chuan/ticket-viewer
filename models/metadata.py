
class Metadata:
    '''
    This class represents the metadata from a Ticket API call
    '''

    def __init__(self, current_page, previous_page, count):
        self.current_page = current_page
        self.previous_page = previous_page
        self.count = count
