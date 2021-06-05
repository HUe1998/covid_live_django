from django.http import HttpResponse, JsonResponse
from urllib.request import urlopen
import json


def ChartView(request):
    url = 'https://api.covid19api.com/summary'
    data_json = json.loads(urlopen(url).read())
    countryList = []
    totalList = []
    for country in data_json['Countries']:
        countryList.append(country['Country'])
        totalList.append(country['TotalConfirmed'])
    return JsonResponse(data_json)
