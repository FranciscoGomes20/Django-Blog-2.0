from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=254, blank=True)
    post_cover = models.ImageField(upload_to = 'images/post-cover/', blank=True, default='\../media/images/cafe.jpg')
    image_text = models.ImageField(upload_to = 'images/post-img/', blank=True, null=True)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def published(self):
        self.published_date = timezone.now()
        self.save()

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email_address  = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=11)
    message = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
