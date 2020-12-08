from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from contact.models import Contact
from contact.views import contact


class TestViews(TestCase):
    def test_contact_views(self):
        """
        Testing both contact and contact_success views,
        creates contact form then redirects to contact_success page.
        Also test contact_success URL
        """
        client = Client()
        contact = Contact.objects.create(
            first_name='test_first',
            last_name='test_last',
            contact_email='test_email',
            contact_phone='test_phone',
            subject='test_subject',
            message='test_message',
        )
        contact_number = contact.contact_number

        response = client.get(reverse('contact_success',
                              args=[contact_number]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_success.html')


class TestURLs(SimpleTestCase):
    def test_contact_URL(self):
        """
        Testing contact URL
        """
        url = reverse('contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact)
