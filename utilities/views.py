from django.shortcuts import render
from datetime import datetime, timedelta
import requests
import os
import json

# Create your views here.

def index(request):
    return render(request, 'utilities/index.html')
    
    
def bye(request):
    now = datetime.now()
    day = datetime(2020, 2, 28)
    bye_day = day - now
    return render(request, 'utilities/bye.html',{'bye_day': bye_day.days})
    
def graduation(request):
    now = datetime.now()
    day = datetime(2019, 5, 28)
    graduation_day = day - now
    return render(request, 'utilities/graduation.html',{'graduation_day': graduation_day.days} )
    
def imagepick(request):
    return render(request, 'utilities/imagepick.html')
    
def today(request):
    token = os.getenv("WHETHER_TOKEN")
    req = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Daejeon,kr&lang=kr&APPID="+token).json()
    whether = req["weather"][0]['description']
    temp = round(((req["main"]['temp'])- 273), 2)
    return render(request, 'utilities/today.html',{'whether' : whether,'temp':temp})
    
def ascii_new(request):
    fonts = ['short', 'utopia', 'rounded', 'acrobatic', 'alligator']
    return render(request, 'utilities/ascii_new.html', {'fonts': fonts})
    
def ascii_make(request):
    text = request.GET.get('text')
    font = request.GET.get('font')
    ascii_code = requests.get('http://artii.herokuapp.com/make?text='+text+'&font='+font).text
    return render(request, 'utilities/ascii_make.html',{'ascii_code':ascii_code})
    
def original(request):
    return render(request, 'utilities/original.html')
    
def translated(request):
    ko = request.GET.get('ko')
    
    naver_client_id = os.getenv("NAVER_CLIENT_ID")
    naver_client_secret = os.getenv("NAVER_CLIENT_SECRET")

    papago_url = "https://openapi.naver.com/v1/papago/n2mt"

    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }
    
    data = {
        "source": "ko",
        "target": "en",
        "text": ko
    }
    papago_response = requests.post(papago_url, headers=headers, data=data).json()

    reply_text = papago_response["message"]["result"]["translatedText"]
    
    return render(request, 'utilities/translated.html',{'reply_text':reply_text})
    
    
