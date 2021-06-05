from django.urls import path
from .views import ChartView

urlpatterns = [
    path('', ChartView, name='chart'),
]
