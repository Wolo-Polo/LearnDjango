from django.db import models

# Create your models here.

from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=300)
    datetime_create = models.DateTimeField("Date time created")

    def __str__(self):
        return "<Question: " + self.question + ">"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "<Question: " + self.answer + ">"

