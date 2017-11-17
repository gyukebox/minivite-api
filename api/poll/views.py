from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


class IndexView(APIView):
    """
    View class for index page
    """
    @staticmethod
    def get(request, format=None):
        """
        GET method. Lists all created polls
        :param request: Http request
        :param format: Either json or html. Returns response as given format. Default is json.
        :return: JSON data of all polls.
        """
        polls = PollModel.objects.all()
        serializer = PollListSerializer(polls, many=True)
        return Response(serializer.data)


class CreateView(APIView):
    """
    View class for creating poll
    """
    @staticmethod
    def post(request, format=None):
        """
        POST method. Creates a new poll by given request. Returns http response as type application/json
        :param request: JSON containing poll title and selections
        :param format: Either json or html. Returns response as given format. Default is json.
        :return: http 201 if created successfully, 400 if creation failed.
        """
        body = request.data

        try:
            poll = PollModel(title=body['title'])
            poll.save()
        except KeyError:
            response = dict(error='KeyError')
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        response = dict(poll=body['title'], selections=list(), count=0)

        try:
            for choice in body['choices']:
                selection = SelectionModel(poll=poll, body=choice)
                selection.save()
                response['selections'].append(choice)
                response['count'] += 1
            return Response(response, status=status.HTTP_201_CREATED)

        except KeyError:
            response = dict(error='KeyError')
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UpdateView(APIView):
    """
    View class for updating poll
    """
    @staticmethod
    def post(request, format=None):
        """
        POST method. Updates poll status and returns http response as type application/json
        :param request: JSON data, including poll title and to-be-modified selections
        :param format: Either json or html. Returns response as given format. Default is json.
        :return: Http 202 if valid, Http 400 if invalid request.
        """
        body = request.data
        try:
            poll = PollModel.objects.get(title=body['poll'])
        except PollModel.DoesNotExist:
            response = dict(error='Poll does not exist')
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        response = dict(poll=body['poll'], updated=list())

        try:
            for choice in body['choices']:
                selection = SelectionModel.objects.filter(poll=poll).filter(body=choice['name']).get()
                if choice['selected'] is True:
                    selection.num_people += 1
                    response['updated'].append({'name': choice['name'], 'update': 'increased'})
                elif selection.num_people > 0:
                    selection.num_people -= 1
                    response['updated'].append({'name': choice['name'], 'update': 'decreased'})
                selection.save()
            return Response(response, status=status.HTTP_202_ACCEPTED)

        except SelectionModel.DoesNotExist:
            response = dict(error='Selection does not exist')
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ResultView(APIView):
    """
    View class for returning poll result
    """
    @staticmethod
    def get(request, format=None):
        """
        Returns result of all poll
        :param request: http request
        :param format: Either json or html. Returns response as given format. Default is json.
        :return: JSON data, containing result of all polls
        """
        polls = PollModel.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request, format=None):
        """
        Returns result of given poll title
        :param request: JSON data, including poll title
        :param format: Either json or html. Returns response as given format. Default is json.
        :return: JSON data, containing result of given poll
        """
        print(request.data)
        try:
            poll = PollModel.objects.get(title=request.data['title'])
            serializer = PollSerializer(instance=poll)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            serializer = PollSerializer(data=request.data)
            serializer.is_valid()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
