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
    
def ping(request):
    return render(request, 'ping.html')
    
def pong(request):
    data = request.GET.get('data')
    return render(request, 'pong.html', {'data':data})
    
    
def user_new(request):
    return render(request, 'user_new.html')
   
    
def user_create(request):
    nickname = request.POST.get('nickname')
    pwd = request.POST.get('pwd')
    return render(request, 'user_create.html' , {'nickname': nickname, 'pwd': pwd} )
    
    

    