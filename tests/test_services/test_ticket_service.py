from logging import raiseExceptions
from models.ticket import Ticket
import unittest
from unittest.mock import patch
from services.ticket_service import TicketService


class TestTicketService(unittest.TestCase):
    def test_many_tickets(self):
        ticket_list_obj = {'tickets': [
            {"id": 102, "subject": "velit eiusmod reprehenderit officia cupidatat"},
            {"id": 122, "subject": "velit eiusmod reprehenderit officia cupidatat"}],
            "next_page": "https://zccalanchuan.zendesk.com/api/v2/tickets.json?page=2&per_page=1",
            "previous_page": None,
            "count": 100}
        with patch('services.ticket_service.TicketService.load_all_tickets') as mock_ticket_list_obj:
            mock_ticket_list_obj.return_value.status_code = 200
            mock_ticket_list_obj.return_value = ticket_list_obj
        ticket_service = TicketService()
        response = ticket_service.load_all_tickets(
            page_number=1, tickets_per_page=25)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(response.json(), ticket_list_obj)

    def test_raise_for_status_exception_caught(self):
        with self.assertRaises(Exception):
            with patch('services.ticket_service.TicketService.r.raise_for_status') as mock_raise:
                mock_raise.return_value = raiseExceptions


if __name__ == '__main__':
    unittest.main()
# EMPTY
# {
#     "tickets": [],
#     "next_page": null,
#     "previous_page": null,
#     "count": 0
# }
