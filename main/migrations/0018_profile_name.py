# Generated by Django 3.1.7 on 2021-03-21 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210321_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
