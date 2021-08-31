from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

# Create your tests here.

class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='yusuf',
            email='yusuf.jalboush@gmail.com',
            password='0790944123'
        )
        self.snack = Snack.objects.create(
            title='pizza',
            purshaser=self.user,
            description='Flat bread with meat, vegetable and/or cheese toppings. Pizza is often eaten as pizza by the slice, "mini pizza" or "pizza baguette" and is often sold by the slice or by weight'
        )

    ##################################################################################################

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "pizza")

    ##################################################################################################

    def test_thing_content(self):
        self.assertEqual(self.snack.title, 'pizza')
        self.assertEqual(str(self.snack.purshaser), 'yusuf')
        self.assertEqual(self.snack.description, 'Flat bread with meat, vegetable and/or cheese toppings. Pizza is often eaten as pizza by the slice, "mini pizza" or "pizza baguette" and is often sold by the slice or by weight')

    ##################################################################################################

    def test_snack_list_view(self):
        expected = 200
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, expected)
        self.assertContains(response, "pizza")
        self.assertTemplateUsed(response, "snack_list.html")

    ##################################################################################################

    def test_snack_details_view(self):
        expected = 200
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/999/")
        self.assertEqual(response.status_code, expected)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "pizza")
        self.assertTemplateUsed(response, "snack_detail.html")

    ##################################################################################################

    def test_snack_create_view(self):
        expected = 200
        actual = self.client.post(reverse('create_snack'),{'title': 'pizza', ' purshaser': self.user,'description': 'Flat bread with meat',})
        self.assertEqual(expected, actual.status_code)
        self.assertContains(actual, 'Flat bread with meat')
        self.assertContains(actual, 'yusuf')

    ##################################################################################################

    def test_snack_update_view(self):
        expected = 200
        actual = self.client.post(reverse('update_snack', args='1')).status_code
        self.assertEqual(expected, actual)

    ##################################################################################################

    def test_snack_delete_view(self):
        expected = 200
        actual = self.client.get(reverse('delete_snack', args='1')).status_code
        self.assertEqual(expected, actual)

    ##################################################################################################