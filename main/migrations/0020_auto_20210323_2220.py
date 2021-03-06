# Generated by Django 3.1.7 on 2021-03-23 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_profile_account_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='staff_level',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Principal', 'Principal'), ('Deputy', 'Deputy'), ('Dean', 'Dean'), ('Academic Mistress', 'Academic Mistress'), ('Boarding Master', 'Boarding Master'), ('ICT', 'ICT'), ('Teacher', 'Teacher')], help_text='The level of the registered staff', max_length=128),
        ),
    ]
