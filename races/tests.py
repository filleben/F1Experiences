from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from races.models import Race, Ticket
from races.views import all_races, race_details

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
        Testing Ticket model is passing values correctly and related to the Race model
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