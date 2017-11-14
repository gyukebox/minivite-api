from django.db import models


class PollModel(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return 'Poll Title: {}'.format(self.title)


class SelectionModel(models.Model):
    poll = models.ForeignKey(PollModel, on_delete=models.CASCADE, default=None)
    body = models.CharField(max_length=50)
    num_people = models.IntegerField(default=0)

    def __str__(self):
        return 'Selection Title : {}, Poll Title: {}, {} people have voted'\
            .format(self.body, self.poll.title, self.num_people)


class ResultModel(models.Model):
    def __str__(self):
        return 'Result model'

    vote_title = models.CharField(max_length=100)
