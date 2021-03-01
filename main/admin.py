from django.contrib import admin
from main import models

class BlogAdmin(admin.ModelAdmin):

    list_display = ('title', 'tag', 'user', 'created_at')
    list_filter = ('tag', 'created_at')

admin.site.register(models.Blog, BlogAdmin)
admin.site.site_header = "Mariakani Secondary School Admin Panel"
admin.site.index_title = "Mariseco Admin"
