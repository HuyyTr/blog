from django.http import HttpResponse
from .tasks import add

# Create your views here.


def hello(resquest):
    add.delay(3, 2)
    return HttpResponse("Hello world")
