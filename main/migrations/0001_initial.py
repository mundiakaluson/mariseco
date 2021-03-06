# Generated by Django 3.1.7 on 2021-03-01 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the Article', max_length=256)),
                ('image', models.ImageField(help_text='Image to Display', upload_to='blogs/')),
                ('headline', models.TextField(help_text='This will be displayed as the main purpose of the article')),
                ('content', models.TextField(help_text='Content of the article, this is not limited.')),
                ('created_at', models.DateField(help_text='Date of Publishement')),
                ('user', models.ForeignKey(help_text='Article Publisher', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
