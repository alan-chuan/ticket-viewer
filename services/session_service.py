import base64
import requests
import config


class SessionService:
    '''
    A class used to manage sessions

    Methods
    -------
    create_session():
        creates a session
    '''

    def __init__(self):
        self.subdomain = config.SUBDOMAIN
        self.username = config.EMAIL
        self.password = config.PASSWORD
        self.session = None

    def create_session(self):
        '''
        This method creates a session if one does not already exist
        '''
        # return existing session if it already exists
        if self.session is not None:
            return self.session
        # create session
        # encode credentials
        CREDENTIAL_STRING_BYTES = f'{self.username}:{self.password}'.encode(
            'ascii')
        BASE_64_STRING = base64.b64encode(
            CREDENTIAL_STRING_BYTES).decode('ascii')
        # instantiate service session
        self.session = requests.Session()
        # add headers to session
        self.session.headers = {'Content-Type': 'application/json',
                                'Authorization': 'Basic ' + BASE_64_STRING}
        return self.session
