from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return self.title + " : " + str(self.price)
    

class Booking(models.Model):
    name = models.CharField(max_length=255)
    guests = models.IntegerField(default=1)
    date = models.DateField()
