from django.shortcuts import render
import json
import urllib.request
from datetime import datetime

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        mydata = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='
                                        +city+'&appid=faf950186bd59ec92277f0d02de6530f').read()
        
        json_data = json.loads(mydata)

        data = {
            'country_code':str(json_data['sys']['country']),
            'coordinate': 'Latitude:'+' '+str(json_data['coord']['lon'])+' '+
                         'Longitude:'+' '+str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp']-273.15),
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
        }
    else:
        city=''
        data={}

    return render(request, 'index.html', {'city':city, 'data':data})

# +' '+'°C'