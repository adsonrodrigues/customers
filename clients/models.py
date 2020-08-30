from django.db import models
from django.contrib.gis.db import models
import uuid


class Profile(models.Model):
    gender_choices = [
        ('Female', 'Female'),
        ('Male', 'Male')
    ]

    id = models.CharField(primary_key=True, max_length=255, blank=False, null=False, unique=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=250, blank=False, null=False)
    last_name = models.CharField(max_length=250, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    gender = models.CharField(max_length=10, choices=gender_choices, blank=False, null=False)
    company = models.CharField(max_length=150, blank=False, null=False)
    city = models.CharField(max_length=150, blank=False, null=False)
    latitude = models.CharField(max_length=100, blank=False, null=False)
    longitude = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
