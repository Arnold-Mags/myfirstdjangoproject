from django.shortcuts import render
from django.http import HttpResponse
from .models import SystemUser

# Create your views here.

def index(request):
    user_list = SystemUser.objects.all()
    context = {
        'user_list': user_list
    }
    return render(request, 'systemuser/index.html', context)

