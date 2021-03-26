# Generated by Django 3.1.7 on 2021-03-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_remove_comment_blog_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='published',
            field=models.BooleanField(default=False, help_text='When checked, the article is live and readable to the audience.'),
        ),
    ]