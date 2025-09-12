from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class LoginTestCase(TestCase):
    def user_verification(self):
        self.user = User.objects.create_user(
            username="Shohjahon",
            password="1234"
        )

    def test_login_success(self):
        response = self.client.post(reverse("login"), {
            "username": "Shohjahon",
            "password": "1234"
        })
        self.assertEqual(response.status_code, 302)

    def test_login_fail(self):
        response = self.client.post(reverse("login"), {
            "username": "Shohjahon",
            "password": "2134"
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password")
