from django.test import TestCase, Client
from main import models
from django.utils import timezone
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from main.views import (
    contact, events
)

client = Client()

class TestModels(TestCase):

    def test_contact(self):

        self.contact_client = models.Contact.objects.create(
            sender_name = 'Test',
            sender_mail = 'test@gmail.com',
            sender_subject = 'test_contact', 
            sender_message = 'test_message',
            sent_at = timezone.now()
        )
        self.assertEquals(self.contact_client.__str__(), 'Test')

    def test_contact_request(self):

        response = self.client.post(reverse('create'))
        self.assertEquals(response.status_code, 302)

    def test_authenticated_user(self):

        user = User.objects.create_user('test', 'test@gmail.com', 'passcode')
        login_user = self.client.force_login(user=user)
