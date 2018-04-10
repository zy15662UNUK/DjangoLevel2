from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264,unique=True)
    last_name = models.CharField(max_length=264,unique=True)
    email = models.CharField(max_length=264)
    # Limit the input value length, unique=True make the Topic unique
    def __str__(self):
        return self.first_name + ' '+self.last_name
