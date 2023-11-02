# from datetime import datetime
from datetime import timedelta

from django.contrib import admin
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text

    @admin.display(
        boolean=True, ordering="pub_date", description="Published recently??"
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text


class Users(models.Model):
    id_user = models.IntegerField()
    name = models.CharField(max_length=100)
    years = models.IntegerField(default=0)
    data = models.DateField()
    abort = models.BooleanField(default=False)
    question_ID = models.IntegerField(default=0)
    
    
    @admin.display(boolean=True, ordering="data", description="user recently??")
    def __str__(self) -> str:
        return self.name
