from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User

# Create your views here.


def index(request, success):
    return render(request, "home/index.html",)


def submit(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    try:
        gender = request.POST['gender']
    except:
        gender = 'O'

    age = request.POST['age']
    if type(age) != type(int):
        age = 1

    try:
        comment = request.POST['comment']
    except:
        comment = ''

    User(
        name=name,
        email=email,
        phone=phone,
        gender=gender,
        age=age,
        comment=comment
    ).save()

    return HttpResponseRedirect('/')
