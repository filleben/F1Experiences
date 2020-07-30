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