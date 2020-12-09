from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import profile, order_history
from accounts.forms import UserProfileForm


class TestURLs(SimpleTestCase):
    def test_profile_URL(self):
        """
        Testing profile URL
        """
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)

    def test_order_history_URL(self):
        """
        Testing order_history URL
        """
        url = reverse('order_history', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, order_history)


class TestForms(TestCase):
    def test_user_profile_form_valid(self):
        """
        Testing user_profile form is valid
        """
        form = UserProfileForm(data={
            'default_phone_number': 'test_phone_number',
            'default_town_or_city': 'test_town_or_city',
            'default_street_address1': 'test_street1',
            'default_street_address2': 'test_street2',
            'default_county': 'test_county',
            'default_country': 'GB',
        })
        self.assertTrue(form.is_valid())

    def test_user_profile_form_invalid(self):
        """
        Testing user_profile form is invalid
        """
        form = UserProfileForm(data={
            'default_phone_number': 'test_phone_number',
            'default_town_or_city': 'test_town_or_city',
            'default_street_address1': 'test_street1',
            'default_street_address2': 'test_street2',
            'default_county': 'test_county',
            'default_country': 'test_country',
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
