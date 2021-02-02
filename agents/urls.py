from django.urls import path
from .views import agents_list

app_name = 'agents'

urlpatterns = [
    path('', agents_list, name='agents_list'),
]
