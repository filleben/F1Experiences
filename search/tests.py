from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from search.views import (event_search, ticket_management_search,
                          event_management_search
                          )


class TestViews(TestCase):
    def test_event_search_view(self):
        """
        Testing the event_search view
        """
        page = self.client.get("/races/", {'q': 'test'})
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "races/races.html")

    def test_ticket_management_search_view(self):
        """
        Testing the ticket_management_search view
        """
        page = self.client.get("/search/ticket_management/", {'q': 'test'})
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "races/ticket_management.html")

    def test_event_management_search_view(self):
        """
        Testing the event_management_search view
        """
        page = self.client.get("/search/event_management/", {'q': 'test'})
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "races/event_management.html")


class TestURLs(SimpleTestCase):
    def test_event_search_URL(self):
        """
        Testing event_search URL
        """
        url = reverse('event_search')
        print(resolve(url))
        self.assertEquals(resolve(url).func, event_search)

    def test_ticket_management_search_URL(self):
        """
        Testing ticket_management_search URL
        """
        url = reverse('ticket_management_search')
        print(resolve(url))
        self.assertEquals(resolve(url).func, ticket_management_search)

    def test_event_management_search_URL(self):
        """
        Testing event_management_search URL
        """
        url = reverse('event_management_search')
        print(resolve(url))
        self.assertEquals(resolve(url).func, event_management_search)
