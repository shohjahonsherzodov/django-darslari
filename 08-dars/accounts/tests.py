from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class RegisterTestCase(TestCase):
    def test_accounts_is_created(self):
        self.client.post(
            reverse("accounts:register"),
            data = {
                "username":"shohjahon",
                "first_name":"Shohjahon",
                "last_name":"Sherzodov",
                "email":"uzbuzb314@gmail.com",
                'password':"1234"
            }
        )
        user = User.objects.get(username="shohjahon")

        self.assertEqual(user.first_name, "Shohjahon")
        self.assertEqual(user.last_name, "Sherzodov")
        self.assertEqual(user.email, "uzbuzb314@gmail.com")
        self.assertNotEqual(user.password, "1234")
        self.assertTrue(user.check_password("1234"))

    def test_response_required(self):
        response = self.client.post(
            reverse("accounts:register"),
            data = {
                "first_name" : "Shohjahon",
                "email" : "uzbuzb314@gmail.com"
            }
        )
        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertFormError((response, "form", "username", "This field is required."))

    def test_invalid_email(self):
        self.client.post(
                reverse("accounts:register"),
                data = {
                    "username":"shohjahon",
                    "first_name" : "Shohjahon",
                    "last_name" : "Sherzodov",
                    "email" : "uzbuzb314@gmail.com",
                    "password" : "1234",
                }
            )

        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
