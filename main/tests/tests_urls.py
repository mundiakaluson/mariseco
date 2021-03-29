from django.test import SimpleTestCase, Client, TestCase
from django.urls import reverse, resolve
from main.views import (
    index, blog, article_success,
    covid_stats, contact, success,
    login, logout, profile, 
    edit_profile, update_profile, register, 
    approval, create, article_success, 
    delete, delete_or_deactivate_success, deactivate,
    all_staff, control_panel, update_web_content,
    manage_blogs, events
)

client = Client()

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)

    def test_blog_url_is_resolved(self):
        url = reverse('blog')
        self.assertEquals(resolve(url).func, blog)

    def test_article_success_url_is_resolved(self):
        url = reverse('article_success')
        self.assertEquals(resolve(url).func, article_success)
    
    def test_covid_stats_url_is_resolved(self):
        url = reverse('covid_stats')
        self.assertEquals(resolve(url).func, covid_stats)
    
    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)
    
    def test_success_url_is_resolved(self):
        url = reverse('success')
        self.assertEquals(resolve(url).func, success)
    
    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_edit_profile_url_is_resolved(self):
        url = reverse('edit_profile')
        self.assertEquals(resolve(url).func, edit_profile)

    def test_update_profile_url_is_resolved(self):
        url = reverse('update_profile')
        self.assertEquals(resolve(url).func, update_profile)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_approval_url_is_resolved(self):
        url = reverse('approval')
        self.assertEquals(resolve(url).func, approval)

    def test_create_url_is_resolved(self):
        url = reverse('create')
        self.assertEquals(resolve(url).func, create)

    def test_article_success_url_is_resolved(self):
        url = reverse('article_success')
        self.assertEquals(resolve(url).func, article_success)

    def test_delete_url_is_resolved(self):
        response = self.client.get(reverse('delete', args={'username': 'test'}))
        self.assertEqual(response.status_code, 302)

    def test_delete_or_deactivate_success_url_is_resolved(self):
        url = reverse('delete_or_deactivate_success')
        self.assertEquals(resolve(url).func, delete_or_deactivate_success)

    def test_deactivate_url_is_resolved(self):
        response = self.client.get(reverse('deactivate', args={'username': 'test'}))
        self.assertEqual(response.status_code, 302)

    def test_all_staff_url_is_resolved(self):
        url = reverse('all_staff')
        self.assertEquals(resolve(url).func, all_staff)

    def test_control_panel_url_is_resolved(self):
        url = reverse('control_panel')
        self.assertEquals(resolve(url).func, control_panel)
    
    def test_update_web_content_url_is_resolved(self):
        url = reverse('update_web_content')
        self.assertEquals(resolve(url).func, update_web_content)
    
    def test_manage_blogs_url_is_resolved(self):
        url = reverse('manage_blogs')
        self.assertEquals(resolve(url).func, manage_blogs)

    def test_events_url_is_resolved(self):
        url = reverse('events')
        self.assertEquals(resolve(url).func, events)