from datetime import date
from tabnanny import verbose
from django.db import models

# Create your models here.
class Contact(models.Model):    
    first_name = models.CharField(max_length=255, )
    last_name = models.CharField(max_length=255, )
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=25)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Contacts'
        ordering = ('-date_created',)


    def __str__(self):
        return self.email
