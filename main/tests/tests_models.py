from django.test import TestCase, Client
from main import models
from django.utils import timezone
from django.urls import reverse, resolve
from main.views import (
    contact
)

client = Client()

class TestModels(TestCase):

    def test_contact(self):

        self.contact_client = models.Contact.objects.create(
            sender_name = 'Jack',
            sender_mail = 'jack@gmail.com',
            sender_subject = 'test_contact', 
            sender_message = 'test_message',
            sent_at = timezone.now()
        )
        self.assertEquals(self.contact_client.__str__(), 'Jack')

    def test_contact_request(self):

        response = self.client.post(reverse('create'))
        self.assertEquals(response.status_code, 302)

