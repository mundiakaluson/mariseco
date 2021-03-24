from django.contrib import admin
from main import models

class BlogAdmin(admin.ModelAdmin):

    list_display = ('title', 'tag', 'user', 'created_at')
    list_filter = ('tag', 'created_at')

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

    actions = ['approve_comments', 'dissaprove_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

    def dissaprove_comments(self, request, queryset):
        queryset.update(active=False)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('staff_level', 'name')
    list_filter = ('staff_level', 'name')

admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.WebContent, WebContentAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Profile, ProfileAdmin)
admin.site.site_header = "Mariakani Secondary School Admin Panel"
admin.site.index_title = "Mariseco Admin"
