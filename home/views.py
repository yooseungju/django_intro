from django.shortcuts import render, HttpResponse
from pprint import pprint
import random

# Create your views here.

def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    return HttpResponse('Welcome to Django !')
    
    
def dinner(request):
    menus = ['히토메보레', '스바라시라멘', '마시기통차', '칼스냉스', '버거킹', '도미노피자', '맥도날드']
    pick = random.choice(menus)
    return render(request, 'dinner.html', {'menus':menus, 'pick':pick})
    
def hello(request, name):
    return render(request, 'hello.html' , {'name' : name})
    
def cube(request, number):
    cube_num = int(number)**3
    return render(request, 'cube.html' , {'cube_num':cube_num})
    
    
