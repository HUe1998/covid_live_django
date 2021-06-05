from django.http import HttpResponse, HttpRequest


def ChartView(request):
    url = 'https://api.covid19api.com/summary'
    return HttpResponse('Hello World!')
