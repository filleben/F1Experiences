from django.db import models


class Race(models.Model):
    """
    Race Model
    """
    name = models.CharField(max_length=400)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    date = models.CharField(max_length=21)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    flag_url = models.URLField(max_length=1024, null=True, blank=True)
    flag = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=400)
    race_views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_date(self):
        return self.date


class Ticket(models.Model):
    """
    Ticket Model
    """
    race = models.ForeignKey('Race', null=True, blank=True,
                             on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
