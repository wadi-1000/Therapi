from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from hood.models import Neighbourhood
# Create your models here.
class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    pic = CloudinaryField(default = 'default.jpeg')
    bio = models.TextField( default="Please Update Bio")
    id_number = models.IntegerField(default = 0, unique = True)
    hood=models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,null=True)
    number = models.IntegerField(default =0)
    email = models.EmailField(default = "Enter your valid email address", unique =True)

    def __str__(self):
        return '{} {}'.format(self.image.url, self.bio)


    def save_profile(self):
        self.save()