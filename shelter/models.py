# from _typeshed import Self
from django.db import models

# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=122)
    email =models.EmailField(max_length=100, null=True, blank=True)
    phone =models.CharField(max_length=12, null=True, blank=True)
    desc =models.TextField()
    date =models.DateField()

    def __str__(self):
        return self.name
    