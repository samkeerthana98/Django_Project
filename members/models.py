from django.db import models

class Member(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    phone = models.BigIntegerField(null=True)
    joined_date = models.DateField(null=True)
def __str__(self):
    return f'{self.firstname} {self.lastname}'
