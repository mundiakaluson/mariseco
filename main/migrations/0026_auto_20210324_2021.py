# Generated by Django 3.1.7 on 2021-03-24 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_blog_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='user',
            new_name='author',
        ),
    ]
