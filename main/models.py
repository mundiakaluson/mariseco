from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=256, help_text='Title of the Article')
    image = models.ImageField(upload_to='blogs/', help_text='Image to Display')
    tag = models.CharField(default='General News', max_length=128, help_text='Tags vary according to content, e.g: Sports, Academics, Religion tags. Defaults to "General News"')
    headline = models.TextField(help_text='This will be displayed as the main purpose of the article')
    content = models.TextField(help_text='Content of the article, this is not limited.')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Article Publisher')
    created_at = models.DateField(help_text='Date of Publishement')

    def __str__(self):
        return self.title
    