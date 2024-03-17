from django.db import models
from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.



class About(models.Model):
    """
    Stores a single about me text
    """
    title = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='images/', default='images/nobody.jpg')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class YourModel(models.Model):
    image = CloudinaryField('image')
    # Add other fields as needed

class YourModel(models.Model):
    image = models.ImageField(upload_to='images/', default='images/default.jpg')