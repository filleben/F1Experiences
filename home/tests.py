from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from home.views import popular_races


class TestViews(TestCase):
    def test_popular_races(self):
        """
        Testing popular_races view
        """
        client = Client()
        response = client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_404_error_handler(self):
        """
        Testing 404_error_handler
        """
        response = self.client.get('something/really/weird/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '404.html')


class TestURLs(SimpleTestCase):
    def test_home_URL(self):
        """
        Testing home URL
        """
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, popular_races)
