from django.urls import path
from .views import create

app_name = "student"
urlpatterns = [
    path('', create, name="create")

]