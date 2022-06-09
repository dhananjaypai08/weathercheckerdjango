from django.shortcuts import render
from decouple import config
import requests
import json

# Create your views here.

def home(request):
    city_data = {}
    city_data['signal'] = -1
    if request.method=='POST':
        key = config('API_KEY')
        city = request.POST.get('city')
        if not city:
            flg = 0
        else:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid='
            url += key
            response = requests.get(url)
            if not response:
                flg = 1
            else:
                data = response.json()
                flg = 2
                print(data)
                city_data['details'] = {}
                for role, val in data.items():
                    if type(val)==list:
                            val = val[0]
                            for k,v in val.items():
                                city_data['details'][role+'_'+k] = v
                    elif type(val)==dict:
                        for k,v in val.items():
                            print(city_data)
                            city_data['details'][role+'_'+k] = v
                    else:
                        city_data['details'][role] = val
                print(city_data)
        city_data['signal'] = flg
    return render(request, 'index.html', city_data)