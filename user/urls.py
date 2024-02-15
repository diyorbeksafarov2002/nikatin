from django.urls import path
from .views import *

urlpatterns = [
    path('/contact', ContactCreateView.as_view()),
    path('/contactlist',ContactListApiView.as_view()),
]