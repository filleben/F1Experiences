from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from cart.views import view_cart, add_to_cart, remove_item


class TestViews(TestCase):
    def test_view_cart(self):
        """
        Testing view_cart view
        """
        client = Client()
        response = client.get(reverse('view_cart'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')


class TestURLs(SimpleTestCase):
    def test_cart_URL(self):
        """
        Testing cart URL
        """
        url = reverse('view_cart')
        print(resolve(url))
        self.assertEquals(resolve(url).func, view_cart)

    def test_add_to_cart_URL(self):
        """
        Testing add_to_cart URL
        """
        url = reverse('add_to_cart', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_to_cart)

    def test_remove_item_URL(self):
        """
        Testing remove_item URL
        """
        url = reverse('remove_item', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, remove_item)
