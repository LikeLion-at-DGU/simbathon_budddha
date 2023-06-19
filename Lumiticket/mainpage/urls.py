from django.urls import path, include
from .views import *
from mainpage import views

app_name = "mainpage"
urlpatterns = [
    path('', intropage, name="intropage"),
    path('loadingpage/', loadingpage, name="loadingpage"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('mainpage/', mainpage, name="mainpage"),
    path('qnapage/', include('qnapage.urls', namespace='qnapage')),
    path('<int:id>', detail, name="detail"),
]