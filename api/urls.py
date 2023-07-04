from django.urls import path, include
from .views import StudentCreate
from .views import StudentRetrieve
from .views import StudentUpdate
from .views import StudentDestroy


app_name = "api"

urlpatterns = [
    path('create',StudentCreate.as_view(), name="create"),
    path('<int:pk>',StudentRetrieve.as_view()),
    path('<int:pk>/update',StudentUpdate.as_view()),
    path('<int:pk>/delete',StudentDestroy.as_view()),
]