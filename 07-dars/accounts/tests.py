from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class RegisterTest(TestCase):

    def test_user_account_is_created(self):
        self.client.post(
            reverse("accounts:register"),
            data = {
                "username" : "Shokhjahon2011_blog",
                "first_name" : "Shohjahon",
                "last_name" : "Sherzodov",
                "email" : "uzbuzb314@gmail.com",
                "password" : "1234"
            }
        )

    account = User.objects.get(username="Shokhjahon2011_blog")

    self.assertEqual(user.first_name, "Shohjahon")
    self.asserEqual(user.last_name, "Sherzodov")
    self.assertEqual(user.email, "uzbuzb314@gmail.com")
    self.assertNotEqual(user.password, "1234")
    self.assertTrue(user.check_password("1234"))

    def test_required_fields(self):
        response = self.client.post(
            reverse("accounts:register")
            data = {
                "first_name" : "Shohjahon",
                "email" : "uzbuzb314@gmail.com"
            }
        )

        user_count = User.objects.count()
        self.assertEqual(user_count,0)
        self.assertFormError(response,"form","username","This field is required.")
        self.assertFormError(response,"form","password","This field is required.")


    def test_invalid_email(self):
        response=self.client.post(
            reverse("users:register"),
            data={
                "username":"ITCreative",
                "first_name":"Husan",
                "last_name":"Suyunov",
                "email":"itcreativegmail.com",
                "password":"0071" 
            }
        )
        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
        print(response.status_code)
        print(response.content)
        self.assertFormError(response,"form","email","Enter a valid email address.")


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
