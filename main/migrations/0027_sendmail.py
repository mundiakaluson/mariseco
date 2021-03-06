# Generated by Django 3.1.7 on 2021-03-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20210324_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=512, null=True)),
                ('message', models.TextField()),
                ('sender', models.CharField(blank=True, max_length=265, null=True)),
                ('reciever', models.CharField(blank=True, max_length=256, null=True)),
                ('delivery_status', models.BooleanField(default=False)),
            ],
        ),
    ]
