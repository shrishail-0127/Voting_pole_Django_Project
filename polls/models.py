from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=100)
    pub_date = models.DateTimeField("Date Published")


    def was_published_recently(self):
        now = timezone.now()
        return self.pub_date >= now - datetime.timedelta(days=1)


    def __str__(self):
        return self.question
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text
