from django.db import models

# Create your models here.

class Race(models.Model):
    name = models.CharField(max_length=400)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    
    def get_date(self):
        return self.date

class Ticket(models.Model):
    race = models.ForeignKey('Race', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name