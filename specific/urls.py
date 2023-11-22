from specific.views import *
from django.urls import path

app_name='something'

urlpatterns=[
    path('sone/',sone,name='sone'),
    path('stwo/',stwo,name='stwo'),
]