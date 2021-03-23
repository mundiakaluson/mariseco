from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save


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

class Contact(models.Model):
    sender_name = models.CharField(max_length=256, help_text='This is the name of the sender.')
    sender_mail = models.EmailField()
    sender_subject = models.CharField(max_length=1024, help_text='Subject of the messsage')
    sender_message = models.TextField()
    sent_at = models.DateField(help_text='Date of Message')

    def __str__(self):
        return self.sender_name
    

class WebContent(models.Model):

    principles = models.TextField(help_text="This is the 'Principles' section on the first page.")
    location = models.TextField(help_text="Location of the school")
    mission = models.TextField(help_text="Mission of the school")

    form_one_stream = models.TextField(help_text="Form one Slogan")
    form_two_stream = models.TextField(help_text="Form two slogan")
    form_three_stream = models.TextField(help_text="Form three slogan")
    form_four_stream = models.TextField(help_text="Form four slogan")

    bom_message = models.TextField(help_text="Message from BOM to parents and students.")

class Comment(models.Model):

    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment by {} waiting for approval!'.format(self.name)
    
class Profile(models.Model):

    STAFF = (

        ('Admin', 'Admin'),
        ('Principal', 'Principal'),
        ('Deputy', 'Deputy'),
        ('Dean', 'Dean'),
        ('Academic Mistress', 'Academic Mistress'),
        ('Boarding Master', 'Boarding Master'),
        ('ICT', 'ICT'),
        ('Teacher', 'Teacher'),
    )

    user = models.OneToOneField(User, on_delete=CASCADE, related_name='user_profile', null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    staff_level = models.CharField(max_length=128, choices=STAFF, help_text='The level of the registered staff')

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
