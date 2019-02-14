from django.shortcuts import render, HttpResponse
from pprint import pprint
import random
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
    
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
    
    
def template_example(request):
    my_list = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    empty_list = []
    datetime_now = datetime.now()
    return render(request, 'template_example.html', {'my_list' :my_list, 'my_sentence':my_sentence, 'messages' : messages,
    'empty_list' : empty_list, 'datetime_now':datetime_now})
    

    