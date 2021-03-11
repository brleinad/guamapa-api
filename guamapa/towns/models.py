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
    gender = models.CharField(blank=True, max_length=1, choices=GENDER_CHOICES)
    # TODO should it be main_activity or something else?
    activity = models.CharField(blank=True, max_length=200)
    ethnicity = models.CharField(blank=True, max_length=200)
    education = models.CharField(blank=True, max_length=200)
    other_info = models.TextField(blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    #TODO: should it be something else than appointment?
    appointment_date = models.DateField(null=True, blank=True)
    term_duration = models.DurationField(null=True, blank=True)
    #telefono


    town = models.OneToOneField(Town, on_delete=models.CASCADE, blank=True, null=True)

class SurveyQuestion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    question = models.TextField(blank=True)
    # question = models.CharField(max_length=200)

class SurveyAnswer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    answer = models.TextField(blank=True)
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)


class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=200)
    location = models.PointField(null=True, blank=True)

class PointOfInterest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=200)
    location = models.PointField(null=True, blank=True)
    description = models.TextField(blank=True)
