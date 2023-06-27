from django.urls import path
from .views import home
from .views import create
from .views import read


app_name = "student"
urlpatterns = [
    path('', home, name="home"),
    path('create', create, name="create"),
    path('read', read, name="read")


]