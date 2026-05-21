from os import name

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class rackets(models.Model):
    RACKET_TYPE_CHOICE ={
        ('Y','YONEX'),
        ('B','BOULT'),
        ('D','DEEP'),
        ('S','SAMSH'),
        
    }
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='DBL/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=RACKET_TYPE_CHOICE)
    description = models.TextField(max_length=500, default="")
    pricing = models.DecimalField(max_digits=7,decimal_places=2, default=1000.00)
    def __str__(self):
        return self.name
    
    #Racket revies for one to many relationship
class racket_reviews(models.Model):
    racket = models.ForeignKey(rackets,on_delete=models.CASCADE ,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    RATING_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5)
    def __str__(self):
        return f'{self.user.username} - review for {self.racket.name} - {self.rating} stars'
    
    #racket type for multipale brands many to many relationship
class racket_type(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, default="")
    rackets = models.ManyToManyField(rackets, related_name='types')
    def __str__(self):
        return self.name    

    #one to one relationship with racket serial number
class LaserSerial(models.Model):
    racket = models.OneToOneField(rackets, on_delete=models.CASCADE, related_name='serial')
    serial_code = models.CharField(max_length=30, unique=True)
    warranty_months = models.PositiveSmallIntegerField(default=12)

    def __str__(self):
        return f"Serial: {self.serial_code} ({self.racket.name})"