from django.test import TestCase, Client
from django.urls import reverse
from races.models import Race, Ticket

class TestViews(TestCase):
    """
    Testing the all_races view
    """
    def test_all_races(self):
        client = Client()
        response = client.get(reverse('races'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'races/races.html')

    def test_race_details(self):
        """
        Testing the race_details view, creates a race and ticket and sets the URL to the race ID
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
        id = race.id

        ticket = Ticket.objects.create(
            name='test_ticket',
            description='test_description',
            price='0.00',
        )

        response = client.get(reverse('race_detail', args=[id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'races/race_details.html')