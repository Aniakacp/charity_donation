from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

TYPE_CHOICES= (
    (1, 'foundation'),
    (2, 'non-governmental organization'),
    (3, 'local collection'),
)

class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    type= models.IntegerField(choices=TYPE_CHOICES, default='foundation')
    categories= models.ManyToManyField(Category)

class Donation(models.Model):
    quantity= models.IntegerField()
    categories= models.ManyToManyField(Category)
    institution= models.ForeignKey(Institution, on_delete=models.CASCADE)
    address= models.CharField(max_length=250)
    phone_number= models.SmallIntegerField()
    city= models.CharField(max_length=64)
    zip_code= models.CharField(max_length=64)  # what it should look like?
    pick_up_date= models.DateField()
    pick_up_time= models.DateField()
    pick_up_comment= models.CharField(max_length=150)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)