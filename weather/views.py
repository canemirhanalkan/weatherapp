from django.shortcuts import render
import requests
import datetime
import locale

# Create your views here.

def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'İstanbul'

    key = '12f9563b5d56a94d23d5c83b004ed158'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid':key, 'units':'metric', 'lang':'tr'}
    r = requests.get(url = URL, params=PARAMS)
    res = r.json()
    
    description = res['weather'][0]['description'].upper()
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']

    locale.setlocale(locale.LC_ALL,"")
    day = datetime.date.today().strftime("%A")

    return render(request, 'weather/index.html', {
        'description':description,
        'icon':icon,
        'temp':temp,
        'day':day,
        'city':city,
    })