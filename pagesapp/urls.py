from django.urls import path
from .views import HomePageView, AboutPageView, EgaPageView, EgainfoPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('ega/', EgaPageView.as_view(), name='ega'),
    path('', HomePageView.as_view(),name='home'),
    path('ega/info', EgainfoPageView.as_view(), name='egainfo'),
]