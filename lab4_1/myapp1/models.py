from django.db import models

# Create your models here.


class ContactList(models.Model):
    User_id = models.IntegerField()
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    profession = models.CharField(max_length=256)
    profession2 = models.CharField(max_length=256)
    Phone_Number = models.IntegerField()
    email = models.CharField(max_length=256)
