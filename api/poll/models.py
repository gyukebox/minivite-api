from django.db import models


# Create your models here.
class PollModel(models.Model):
    title = models.CharField(max_length=100)


class SelectionModel(models.Model):
    poll = models.ForeignKey(PollModel, on_delete=models.CASCADE, default=None)
    body = models.CharField(max_length=50)
    count = models.IntegerField(default=0)


class ResultModel(models.Model):
    def __str__(self):
        return 'Result model'

    vote_title = models.CharField(max_length=100)