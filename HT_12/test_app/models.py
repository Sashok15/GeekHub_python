import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Message(models.Model):
    message_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.message_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment
