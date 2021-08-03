import unittest
from unittest.mock import patch
from services.session_service import SessionService


class TestSessionService(unittest.TestCase):
    def test_create_new_session(self):
        session_obj = {'Content-Type': 'application/json',
                       'Authorization': 'Basic XXXXX'}
        with patch('services.session_service.requests.Session') as mock_session:
            mock_session.return_value = session_obj
        session_service = SessionService()
        session = session_service.create_session()
        self.assertEquals('application/json', session.headers['Content-Type'])
        self.assertTrue('Basic ' in session.headers['Authorization'])

    def test_no_duplicate_session(self):
        session_obj = {'Content-Type': 'application/json',
                       'Authorization': 'Basic XXXXX'}
        with patch('services.session_service.requests.Session') as mock_session:
            mock_session.return_value = session_obj
        session_service = SessionService()
        session_1 = session_service.create_session()
        session_2 = session_service.create_session()
        self.assertEquals(session_1, session_2)


if __name__ == '__main__':
    unittest.main()
