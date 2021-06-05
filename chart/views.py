from django.http import HttpResponse, JsonResponse
from urllib.request import urlopen
import json
from django.shortcuts import render


def ChartView(request):
    url = 'https://api.covid19api.com/summary'
    data_json = (json.loads(urlopen(url).read()))['Countries']
    countryList = []
    totalList = []
    for country in data_json:
        countryList.append(country['Country'])
        totalList.append(country['TotalConfirmed'])

    context = {
        'countryList': countryList,
        'totalList': totalList,
    }

    return render(request, 'chart.html', context)
