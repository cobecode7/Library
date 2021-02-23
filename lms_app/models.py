from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):

    status_book = [
        ('availble','anailble'),
        ('rental','rental'),
        ('sold','sold')
    ]

    title = models.CharField(max_length=50)
    auther = models.CharField(max_length=250, blank=True, null=True)
    photo_book = models.ImageField(upload_to='photos' , blank=True, null=True)
    photo_auther = models.ImageField(upload_to='photos' , blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    retal_price_day = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    retal_period = models.IntegerField(blank=True, null=True)
    total_rental = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_book, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title