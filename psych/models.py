from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models import DateTimeField
from django.utils import timezone
# Create your models here.



class Articles(models.Model):
    Categories = [
    ('Addictions','Addictions'),
    ('Autism','Autism'),
    ('Anxiety','Anxiety Disorders'),
    ('Bipolar','Bipolar Disorder'),
    ('Depression','Depression'),
    ('PTSD','Post-Traumatic Stress Disoder (PTSD)'),
    ('Personality','Personality Disorders'),
    ('Sexual','Sexual Disorders'),
    ('General', 'General')
]

    title = models.CharField(max_length = 100)
    pic = CloudinaryField('image')
    author = models.CharField(max_length = 100)
    categories = models.CharField(max_length=12, choices=Categories, default = 'Addictions')
    content = models.TextField()

class Appointments(models.Model):
    Pyschologists = [
        ('Alice','Alice Gathoni'),
        ('Peterson', 'Peterson Omollo '),
        ('Joram', 'Joram Karanja'),
        ('Mary','Mary Manders'),
        ('Newton','Benard Newton'),
        ('Katherine','Katherine Muthoni'),
    ]

    Categories = [
    ('Addictions','Addictions'),
    ('Autism','Autism'),
    ('Anxiety','Anxiety Disorders'),
    ('Bipolar','Bipolar Disorder'),
    ('Depression','Depression'),
    ('PTSD','Post-Traumatic Stress Disoder (PTSD)'),
    ('Personality','Personality Disorders'),
    ('Sexual','Sexual Disorders'),
    ('General', 'General'),
    ('Undiagnosed', 'Undiagnosed'),
]

    client =  models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    psychologists = models.CharField(max_length = 12,choices = Pyschologists, default = 'Alice Gathoni')
    date = DateTimeField(default = timezone.now)
    condition = models.CharField(max_length = 12,choices = Categories, default = 'Undiagnosed')
    

    @classmethod
    def display_all_objects(cls):
        all_appointments=cls.objects.all()
        return all_appointments
