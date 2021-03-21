# Generated by Django 3.1.7 on 2021-03-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210321_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='profile',
            name='account_status',
            field=models.BooleanField(default=True, help_text='The current status of the account. Default set to True.'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='staff_level',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Principal', 'Principa'), ('Deputy', 'Deputy'), ('Dean', 'Dean'), ('Academic Mistress', 'Academic Mistress'), ('Boarding Master', 'Boarding Master'), ('ICT', 'ICT'), ('Teacher', 'Teacher')], help_text='The level of the registered staff', max_length=128),
        ),
    ]
