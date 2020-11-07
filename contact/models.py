from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=254, null=False, blank=False)
    last_name = models.CharField(max_length=254, null=False, blank=False)
    contact_email = models.EmailField(max_length=254, null=False, blank=False)
    contact_phone = models.CharField(max_length=20, null=False, blank=False)
    subject = models.CharField(max_length=254, null=False, blank=False)
    message = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"