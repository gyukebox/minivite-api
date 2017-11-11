import json
from django.http import HttpResponse
from .models import *


def poll_update(request):
    """
    투표 결과 실시간 반영 뷰 함수
    :param request: JSON 형식의 업데이트 내역
    :return: 성공 시 http 200, 실패 시 원인에 따라 400 호은 500
    """
    to_update = json.loads(request.body, encoding='utf8')
    poll = PollModel.objects.get(title=to_update['pollTitle'])
    selection_lists = SelectionModel.objects.filter(poll_id=poll.id)
    for list in selection_lists:
        pass

    return HttpResponse(status=200)
