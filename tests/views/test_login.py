from gss.settings.base import LOGIN_URL

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.test import TestCase

class LoginPageTests(TestCase):
    def setUpTestData():
        Group.objects.get_or_create(name='can_input')
        Group.objects.get_or_create(name='can_report')
        User.objects.create_superuser(username='root',
                                 email='test@dude.com',
                                 password='root')
        User.objects.create_user(username='dummy_1',
                                 email='test@dude.com',
                                 password='dummy_1')
        User.objects.create_user(username='dummy_2',
                                 email='test@dude.com',
                                 password='dummy_2')
        Group.objects.get(name='can_input').user_set.add(User.objects.get(username='dummy_2'))
        Group.objects.get(name='can_report').user_set.add(User.objects.get(username='dummy_1'))
    def test_anon_request(self):
        self.assertRedirects(self.client.get('/upload/'),LOGIN_URL)
        self.assertRedirects(self.client.get('/report/'),LOGIN_URL)
        self.assertRedirects(self.client.get('/'),LOGIN_URL)
        self.assertRedirects(self.client.get('/error/'),LOGIN_URL)
        self.assertRedirects(self.client.get('/blahblahblah/'),LOGIN_URL)
    
    def test_authed_superuser_request(self):
        self.client.login(username='root', password='root')
        self.assertEqual(self.client.get('/upload/').status_code,200)
        self.assertEqual(self.client.get('/report/').status_code,200)
        self.assertEqual(self.client.get('/').status_code,200)
        self.assertEqual(self.client.get('/error/').status_code,403)
        self.assertEqual(self.client.get('/blahblahblah/').status_code,404)
    
    def test_authed_can_report_user_request(self):
        self.client.login(username='dummy_1', password='dummy_1')
        self.assertEqual(self.client.get('/upload/').status_code,302)
        self.assertEqual(self.client.get('/report/').status_code,200)
        self.assertEqual(self.client.get('/').status_code,200)
        self.assertEqual(self.client.get('/error/').status_code,403)
        self.assertEqual(self.client.get('/blahblahblah/').status_code,404)

    def test_authed_can_input_user_request(self):
        self.client.login(username='dummy_2', password='dummy_2')
        self.assertEqual(self.client.get('/upload/').status_code,200)
        self.assertEqual(self.client.get('/report/').status_code,302)
        self.assertEqual(self.client.get('/').status_code,200)
        self.assertEqual(self.client.get('/error/').status_code,403)
        self.assertEqual(self.client.get('/blahblahblah/').status_code,404)



