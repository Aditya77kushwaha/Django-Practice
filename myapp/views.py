from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel

# Create your views here.


def index(request):
    return HttpResponse('Hi there!')


def show(request):

    a = MyModel.objects.all()

    return render(request, "show.html", {"data": a})
