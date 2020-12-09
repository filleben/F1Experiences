from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from checkout.views import checkout, cache_checkout_data
from checkout.webhooks import webhook
from checkout.models import Order, OrderLineItem
from checkout.forms import OrderForm
from races.models import Race, Ticket
from django.utils import timezone
import datetime
from mock import patch


class TestURLs(SimpleTestCase):
    def test_checkout_URL(self):
        """
        Testing checkout URL
        """
        url = reverse('checkout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout)

    def test_cache_checkout_data_URL(self):
        """
        Testing cache_checkout_data URL
        """
        url = reverse('cache_checkout_data')
        print(resolve(url))
        self.assertEquals(resolve(url).func, cache_checkout_data)

    def test_webhook_URL(self):
        """
        Testing webhook URL
        """
        url = reverse('webhook')
        print(resolve(url))
        self.assertEquals(resolve(url).func, webhook)


class TestModels(TestCase):
    def test_order_model(self):
        """
        Testing Order model is passing values correctly
        """
        with patch.object(timezone, 'now', return_value=datetime.datetime(2020, 9, 12, 11, 00)) as mock_now:
            order = Order.objects.create(
                full_name='test_name',
                email='test@test.com',
                phone_number='test_phone',
                country='test_country',
                town_or_city='test_town_or_city',
                street_address1='test_street1',
                street_address2='test_street2',
                county='test_county',
                date=timezone.now(),
                order_total='10.00'
            )
            order.save()
            self.assertEquals(order.full_name, 'test_name')
            self.assertEquals(order.email, 'test@test.com')
            self.assertEquals(order.phone_number, 'test_phone')
            self.assertEquals(order.country, 'test_country')
            self.assertEquals(order.town_or_city, 'test_town_or_city')
            self.assertEquals(order.street_address1, 'test_street1')
            self.assertEquals(order.street_address2, 'test_street2')
            self.assertEquals(order.county, 'test_county')
            self.assertEquals(order.date, timezone.now())
            self.assertEquals(order.order_total, '10.00')

    def test_OrderLineItem_model(self):
        """
        Testing OrderLineItem model is passing values correctly
        """
        with patch.object(timezone, 'now', return_value=datetime.datetime(2020, 9, 12, 11, 00)) as mock_now:
            order = Order.objects.create(
                full_name='test_name',
                email='test@test.com',
                phone_number='test_phone',
                country='test_country',
                town_or_city='test_town_or_city',
                street_address1='test_street1',
                street_address2='test_street2',
                county='test_county',
                date=timezone.now(),
                order_total='10.00'
            )
            order.save()
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
            order_line_item = OrderLineItem.objects.create(
                order=order,
                ticket=ticket,
                quantity=1
            )
            self.assertEquals(order_line_item.order, order)
            self.assertEquals(order_line_item.ticket, ticket)
            self.assertEquals(order_line_item.quantity, 1)


class TestForms(TestCase):
    def test_order_form_valid(self):
        """
        Testing order_form is valid
        """
        form = OrderForm(data={
            'full_name': 'test_name',
            'email': 'test@test.com',
            'phone_number': 'test_phone',
            'street_address1': 'test_street1',
            'street_address2': 'test_street2',
            'town_or_city': 'test_town_or_city',
            'county': 'test_county',
            'country': 'GB',
        })
        self.assertTrue(form.is_valid())

    def test_order_form_invalid(self):
        """
        Testing order_form is invalid
        """
        form = OrderForm(data={
            'full_name': 'test_name',
            'email': 'test@test.com',
            'phone_number': 'test_phone',
            'street_address1': 'test_street1',
            'street_address2': 'test_street2',
            'town_or_city': 'test_town_or_city',
            'county': 'test_county',
            'country': 'fake_country',
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
