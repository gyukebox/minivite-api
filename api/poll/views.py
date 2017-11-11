import json
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    print(request.body)
    return HttpResponse('hello')


def poll_create(request):
    # json 을 풀어서 리스트로 만들 수 있거든요
    import json
    poll_info = request.body

    new_model = PollModel()
    try:
        new_model.title = poll_info['title']
        for choice in poll_info['choices']:
            new_selection = SelectionModel()

    except IndexError:
        return HttpResponse(status=400)

    new_model.save()

    return HttpResponse(status=200)


def poll_update(request):
    """
    투표 결과 실시간 반영 뷰 함수
    :param request: JSON 형식의 업데이트 내역
    :return: 성공 시 http 200, 실패 시 원인에 따라 400 호은 500
    """
    to_update = json.loads(request.body, encoding='utf8')
    poll = PollModel.objects.get(title=to_update['pollTitle'])


    return HttpResponse(status=200)
