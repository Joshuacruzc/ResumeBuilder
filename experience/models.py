from django.contrib.auth import get_user_model
from django.db import models


class Experience(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    host = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    role = models.CharField(max_length=64)

    def __str__(self):
        return self.role + ' at ' + self.host


class ExperienceStatement(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    statement = models.CharField(max_length=64)


class Tag(models.Model):
    name = models.CharField(max_length=64)
    experiences = models.ManyToManyField(Experience)

    def __str__(self):
        return self.name
