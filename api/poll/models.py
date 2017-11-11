from django.db import models


# Create your models here.
class SelectionModel(models.Model):
    body = models.CharField(max_length=50)
    is_selected = models.BooleanField(default=False)


class PollModel(models.Model):
    title = models.CharField(max_length=100)
    selections = models.ForeignKey(SelectionModel, on_delete=models.CASCADE)


class ResultModel(models.Model):
    def __str__(self):
        return 'Result model'

    vote_title = models.CharField(max_length=100)