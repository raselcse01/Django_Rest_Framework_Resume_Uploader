from django.db import models

# Create your models here.
STATIC_CHOICE =((
    ('Paril','Paril'),
    ('Charigram','Charigram'),
    ('Singair','Singair'),
))

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=STATIC_CHOICE, max_length=100)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to='pimages', blank=True)
    rdoc = models.FileField(upload_to='rdoc',blank=True)
