from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    # here you can add any custom field if necessary
    bio = models.TextField(null=True, blank=True)
    test = models.TextField(null=True, blank=True)
    '''
     null 
       definition : the column will store records as NULL if no input is given
       usage : applies to the database layer 
       default: False
     blank 
       definition : if you want to allow empty values when submitting the form 
       usage : if you want to allow empty values when submitting the form 

    '''
