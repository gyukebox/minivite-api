from django.test import TestCase
from .models import *


# Create your tests here.
class CreatePollTests(TestCase):
    """
    Creating polls test
    """
    def test_is_created(self):
        sample_poll = PollModel(title='이것은 테스트 투표')
        selections = [SelectionModel(poll=sample_poll, body='이것은 테스트 선택지 {}'.format(i)) for i in range(5)]
        sample_poll.save()
        [selection.save() for selection in selections]

        self.assertIsNot(PollModel.objects.get(title=sample_poll.title), None)


class UpdatePollTests(TestCase):
    pass
