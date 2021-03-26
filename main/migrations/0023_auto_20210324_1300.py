# Generated by Django 3.1.7 on 2021-03-24 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20210324_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blog_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.blog'),
        ),
    ]