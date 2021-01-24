# from django.db import models
from django.contrib.gis.db import models
import uuid


class Town(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=200)
    location = models.PointField(null=True, blank=True)
    elevation = models.PositiveIntegerField(null=True, blank=True)
    population = models.PositiveIntegerField(null=True, blank=True)
    category = models.CharField(blank=True, max_length=64)



class AssistantMayor(models.Model):

    GENDER_CHOICES = [
        ('M', 'Masculine'),
        ('F', 'Feminine'),
        ('O', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    occupation = models.CharField(blank=True, max_length=200)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(blank=True, max_length=1, choices=GENDER_CHOICES)
    activity = models.CharField(blank=True, max_length=200)
    other = models.TextField(blank=True)
    ethnicity = models.CharField(blank=True, max_length=200)
    education = models.CharField(blank=True, max_length=200)
    appointment_date = models.DateField(blank=True)
    term_duration = models.DurationField(blank=True)

