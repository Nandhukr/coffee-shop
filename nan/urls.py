from django.urls import path
from nan import views
from django.urls import path
# from .views import search

urlpatterns = [
    path("home/",views.IndexView.as_view(),name="home"),
]