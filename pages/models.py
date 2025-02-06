from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    location_link = models.URLField()  # New field for Google Maps link

    def __str__(self):
        return self.name
