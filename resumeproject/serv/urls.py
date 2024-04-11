from django.urls import path
from serv import views

urlpatterns=[
    path('service/',views.service,name='service')
]