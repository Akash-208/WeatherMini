from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
import requests
import json
import datetime

def index(request):   
    city = request.POST.get('gettingCity' ,'Dehradun')
    url = f"http://api.weatherapi.com/v1/current.json?key=4610a7419ed741bb867152834232304&q={city}"

    r = requests.get(url)
    now = datetime.datetime.now()
    day = now.strftime('%A')
    weather_dict = json.loads(r.text)
    params = {
        "Day":day,
        "City":city,
        "Region":weather_dict['location']['region'],
        "Temperature":weather_dict['current']['temp_c'],
        'humidity':weather_dict['current']['humidity'],
        'wind':weather_dict['current']['wind_kph'],
        'feel':weather_dict['current']['feelslike_c'],
        'GustKph':weather_dict['current']['gust_kph'],
    } 

    return render(request,"index.html",params)

