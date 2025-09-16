from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class LoginTestCase(TestCase):
    def config(self):
        self.user = User.objects.create_user(
            username="Shohjahon",
            password="1234"
        )
    def test_login_success(self):
        reply = self.client.post(reverse("accounts:login"), {
            "username": "Shohjahon",
            "password": "1234"
        })
        self.assertEqual(reply.status_code, 302)
    def test_login_fail(self):
        reply = self.client.post(reverse("accounts:login"), {
            "username": "Shohjahon",
            "password": "2134"
        })

        self.assertEqual(reply.status_code, 200)


