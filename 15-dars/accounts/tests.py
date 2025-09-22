from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


# class Testcase_login(TestCase):
#     def setUp(self):
#         self.username = "TestUser123"
#         self.password = "Admin111"
#         self.user = User.objects.create_user(username=self.username, password=self.password)
#     def test_login_required(self):
#         response = self.client.get(reverse("landing_page"))
#         self.assertContains(response, "Login Required")

#     def test_profile_detail(self):
#         self.username = "Shohjahon"
#         self.password = "1234"
#         self.first_name = "Shohjahon"
#         self.last_name = "Sherzodov"
#         self.email = "uzbuzb314@gmail.com"
#         self.user = User.objects.create_user(username=self.username, password=self.password, first_name=self.first_name, last_name=self.last_name, email=self.email)
#         self.client.login(username=self.username, password=self.password)
#         response = self.client.get(reverse("landing_page"))
#         self.assertContains(response, self.username)
#         self.assertContains(response, self.email)
#         self.assertContains(response, self.first_name)
#         self.assertContains(response, self.last_name)

class LogoutTestCase(TestCase):
    def setUp(self):
        self.username = 'TestUser'
        self.password = 'test123'
        self.user = User.objects.create_user(username=self.username, password=self.password)
    def test_logout(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(reverse("accounts:logout"), follow=True)

        self.assertContains(response, "Siz tizimdan muvaffaqiyatli chiqdingiz!")
        