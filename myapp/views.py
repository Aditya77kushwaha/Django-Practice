from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel, MyForm
from .forms import MyForm1

# Create your views here.


def index(request):
    return HttpResponse('Hi there!')


def show(request):
    a = MyModel.objects.all()
    return render(request, "show.html", {"data": a})


def form(request):
    my_form = MyForm(request.POST)
    if my_form.is_valid():
        if request.user != 'AnonymousUser':
            my_form.save()
    my_form = MyForm()
    return render(request, "form.html", {"data": my_form})


def form1(request):
    my_form = MyForm1(request.POST)
    return render(request, 'form1.html', {"data": my_form})
