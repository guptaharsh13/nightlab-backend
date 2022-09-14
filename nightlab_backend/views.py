from turtle import delay
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework .status import HTTP_200_OK
from .tasks import task


@api_view(http_method_names=("GET",))
def index(request):
    task.delay()
    return Response(data={"app": "nightlab-backend 🚀"}, status=HTTP_200_OK)
