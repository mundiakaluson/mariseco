from django.contrib import admin
from main import models

class BlogAdmin(admin.ModelAdmin):

    list_display = ('title', 'tag', 'user', 'created_at')
    list_filter = ('tag', 'created_at')

class ContactAdmin(admin.ModelAdmin):

    list_display = ('sender_name', 'sender_mail', 'sender_subject')
    list_filter = ('sender_subject', 'sent_at')
    readonly_fields = ('sender_name', 'sender_mail', 'sender_subject', 'sender_message', 'sent_at')

admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.Blog, BlogAdmin)
admin.site.site_header = "Mariakani Secondary School Admin Panel"
admin.site.index_title = "Mariseco Admin"
