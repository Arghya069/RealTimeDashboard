from django.urls import path, re_path
from . import consumers
from .views import *

urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('chec',chec,name="chec"),
]
