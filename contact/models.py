from django.db import models
import uuid

class Contact(models.Model):
    contact_number = models.CharField(max_length=16, null=False, editable=False)
    first_name = models.CharField(max_length=254, null=False, blank=False)
    last_name = models.CharField(max_length=254, null=False, blank=False)
    contact_email = models.EmailField(max_length=254, null=False, blank=False)
    contact_phone = models.CharField(max_length=20, null=False, blank=False)
    subject = models.CharField(max_length=254, null=False, blank=False)
    message = models.TextField(max_length=1000, null=False, blank=False)

    def _generate_contact_number(self):
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        if not self.contact_number:
            self.contact_number = self._generate_contact_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} with subject {self.subject}"