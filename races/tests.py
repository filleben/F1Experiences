from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from races.models import Race, Ticket
from races.views import (all_races, race_details, event_management,
                         ticket_management, edit_race, edit_ticket,
                         delete_race, delete_ticket, add_race, add_ticket
                         )
from races.forms import RaceForm, TicketForm


class TestViews(TestCase):
    def test_all_races(self):
        """
        Testing the all_races view
        """
        client = Client()
        response = client.get(reverse('races'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'races/races.html')

    def test_race_details(self):
        """
        Testing the race_details view, creates a race and ticket
        and sets the URL to the race ID
        """
        client = Client()
        race = Race.objects.create(
            name='test_race',
            friendly_name='test_friendly_name',
            date='test_date',
            image_url='test_image_URL',
            image='test.png',
            flag_url='test_flag_URL',
            flag='flag.png',
            location='test_location',
            race_views='0',
        )
        race_id = race.id

        ticket = Ticket.objects.create(
            name='test_ticket',
            description='test_description',
            price='0.00',
        )
        ticket_id = ticket

        response = client.get(reverse('race_detail',
                              args=[race_id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'races/race_details.html')


class TestURLs(SimpleTestCase):
    def test_all_races_URL(self):
        """
        Testing races URL
        """
        url = reverse('races')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_races)

    def test_race_details_URL(self):
        """
        Testing race details URL
        """
        url = reverse('race_detail', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, race_details)

    def test_event_management_url(self):
        """
        Testing event_management URL
        """
        url = reverse('event_management')
        print(resolve(url))
        self.assertEquals(resolve(url).func, event_management)

    def test_ticket_management_url(self):
        """
        Testing ticket_management URL
        """
        url = reverse('ticket_management')
        print(resolve(url))
        self.assertEquals(resolve(url).func, ticket_management)

    def test_edit_race_URL(self):
        """
        Testing edit_race URL
        """
        url = reverse('edit_race', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_race)

    def test_edit_ticket_URL(self):
        """
        Testing edit_race URL
        """
        url = reverse('edit_ticket', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_ticket)

    def test_delete_ticket_URL(self):
        """
        Testing delete_ticket URL
        """
        url = reverse('delete_ticket', args=[100])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_ticket)

    def test_delete_race_URL(self):
        """
        Testing delete_race URL
        """
        url = reverse('delete_race', args=[100])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_race)

    def test_add_race_url(self):
        """
        Testing add_race URL
        """
        url = reverse('add_race')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_race)

    def test_add_ticket_url(self):
        """
        Testing add_race URL
        """
        url = reverse('add_ticket')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_ticket)


class TestModels(TestCase):
    def test_race_model(self):
        """
        Testing Race model is passing values correctly
        """
        race = Race.objects.create(
            name='test_race',
            friendly_name='test_friendly_name',
            date='test_date',
            image_url='test_image_URL',
            image='test.png',
            flag_url='test_flag_URL',
            flag='flag.png',
            location='test_location',
            race_views='0',
        )
        race.save()
        self.assertEquals(race.name, 'test_race')
        self.assertEquals(race.friendly_name, 'test_friendly_name')
        self.assertEquals(race.date, 'test_date')
        self.assertEquals(race.image_url, 'test_image_URL')
        self.assertEquals(race.image, 'test.png')
        self.assertEquals(race.flag_url, 'test_flag_URL')
        self.assertEquals(race.flag, 'flag.png')
        self.assertEquals(race.location, 'test_location')
        self.assertEquals(race.race_views, '0')

    def test_ticket_model(self):
        """
        Testing Ticket model is passing values correctly
        and related to the Race model
        """
        race = Race.objects.create(
            name='test_race',
            friendly_name='test_friendly_name',
            date='test_date',
            image_url='test_image_URL',
            image='test.png',
            flag_url='test_flag_URL',
            flag='flag.png',
            location='test_location',
            race_views='0',
        )
        race.save()
        ticket = Ticket.objects.create(
            race=race,
            name='test_ticket',
            description='test_description',
            price='0.0'
        )
        ticket.save()
        self.assertEquals(ticket.race, race)


class TestForms(TestCase):
    def test_race_form_valid(self):
        """
        Testing contact_form is valid
        """
        form = RaceForm(data={
            'name': 'test_race',
            'friendly_name': 'test_friendly_name',
            'date': 'test_date',
            'image_url': 'www.test.com',
            'image': 'test.png',
            'flag_url': 'www.test.com',
            'flag': 'flag.png',
            'location': 'test_location',
            'race_views': '0',
        })
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid(self):
        """
        Testing race_form is invalid
        """
        form = RaceForm(data={
            'name': 'test_race',
            'friendly_name': 'test_friendly_name',
            'date': 'test_date',
            'image_url': 'test_image_URL',
            'image': 'test.png',
            'flag_url': 'test_flag_URL',
            'flag': 'flag.png',
            'location': 'test_location',
            'race_views': 'B',
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_ticket_form_valid(self):
        """
        Testing ticket_form is valid
        """
        form = TicketForm(data={
            'race': '',
            'name': 'test_ticket',
            'description': 'test_description',
            'price': '10.00'
        })
        self.assertTrue(form.is_valid())

    def test_ticket_form_invalid(self):
        """
        Testing ticket_form is invalid
        """
        form = TicketForm(data={
            'race': 'random_race',
            'name': 'test_ticket',
            'description': 'test_description',
            'price': '10.00'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
