from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('',include('app_empresa.urls'))
]
