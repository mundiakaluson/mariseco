from django.contrib import admin
from main import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.core.mail import send_mail

class BlogAdmin(admin.ModelAdmin):

    list_display = ('title', 'tag', 'author', 'created_at', 'published')
    list_filter = ('tag', 'created_at')

    actions = ['published', 'unpublish']

    def published(self, request, queryset):
        queryset.update(published=True)

    def unpublish(self, request, queryset):
        queryset.update(published=False)

class ContactAdmin(admin.ModelAdmin):

    list_display = ('sender_name', 'sender_mail', 'sender_subject')
    list_filter = ('sender_subject', 'sent_at')
    readonly_fields = ('sender_name', 'sender_mail', 'sender_subject', 'sender_message', 'sent_at')

class WebContentAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'blog', 'created_on', 'comment', 'active')
    list_filter = ('created_on', 'active')
    search_fields = ('name', 'email')
    readonly_fields = ('name', 'email', 'created_on', 'blog')

    actions = ['approve_comments', 'dissaprove_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

    def dissaprove_comments(self, request, queryset):
        queryset.update(active=False)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('staff_level', 'name')
    list_filter = ('staff_level', 'name')

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser')
    actions = ['approve_registration', 'disapprove_registration', 'make_admin']
    
    def approve_registration(modeladmin, request, queryset):
        send_mail(
            'MARISECO STAFF REGISTRATION APPROVAL',
            '''Hello there!,
            Please head to our website and confirm that your account is now approved.
            Welcome to the Mariseco Staff Community!
            ''',
            'no-reply@mariseco.com',
            [request.user.email],
            fail_silently=False,
        )
        queryset.update(is_active=True)
    
    def disapprove_registration(modeladmin, news, queryset):
        queryset.update(is_active=False)
        queryset.update(is_superuser=False)
        queryset.update(is_staff=False)

    def make_admin(modeladmin, news, queryset):
        queryset.update(is_active=True)
        queryset.update(is_superuser=True)
        queryset.update(is_staff=True)

admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.WebContent, WebContentAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Profile, ProfileAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.site_header = "Mariakani Secondary School Admin Panel"
admin.site.index_title = "Mariseco Admin"
