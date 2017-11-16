import json
from django.http import HttpResponse, JsonResponse
from .models import *

def poll_create(request):
    poll_creInfo = request.body.decode("utf-8"))
    poll_info = json.loads(poll_creInfo,encoding='utf8')
    try:
        new_PollModel = PollModel()
        new_PollModel.title = poll_info['Title']
        new_PollModel.save()

        for choice in poll_info['Choices']:
            newSelectionModel = SelectionModel()
            newSelectionModel.poll = new_PollModel
            newSelectionModel.body = choice
            newSelectionModel.save()
    except Exception as e:
        print(e)
        return HttpResponse(status=500)
    return HttpResponse(status=200)

def poll_create(request):
    return HttpResponse(status=200)


def poll_update(request):
    """
    투표 결과 실시간 반영 뷰 함수
    :param request: JSON 형식의 업데이트 내역
    :return: 성공 시 http 200, 실패 시 원인에 따라 400 호은 500
    """
    query = request.body.decode('utf-8')

    if request.method == 'POST':
        try:
            to_update = json.loads(query, encoding='utf8')
            poll = PollModel.objects.get(title=to_update['pollTitle'])

            for choice in to_update['choices']:
                selection = SelectionModel.objects.filter(poll_id=poll.id).filter(body=choice['name']).get()

                if choice['selected'] is True:
                    selection.num_people += 1
                else:
                    if selection.num_people > 0:
                        selection.num_people -= 1
                selection.save()

            # TODO make as JSON Response
            return HttpResponse(status=200)
        except Exception as e:
            print(e)
            return HttpResponse(status=500)
    else:
        return HttpResponse(status=400)


def get_poll_result(request):
    poll_info = request.body.decode('utf-8')
    # poll_info = '{"Body": {"Title": "lunch"}}'
    print(poll_info)

    if not poll_info:
        print("result request is null")
        return HttpResponse(status=400)

    title_json = json.loads(poll_info, encoding='utf8')
    print(title_json)

    title = title_json["Body"]["Title"]
    print(title)

    getPollModel = PollModel.objects.filter(title=title)[0]
    print(title, getPollModel.title)

    outValues = SelectionModel.objects.filter(poll=getPollModel).values('body', 'num_people')
    print(outValues)

    ret = { "body" : { "pollTitle" : getPollModel.title, "result" : list(outValues) } }
    print(ret)

    return JsonResponse(ret, json_dumps_params = {'ensure_ascii': True})

