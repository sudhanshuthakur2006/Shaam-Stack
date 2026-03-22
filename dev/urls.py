from django.urls import path
from .views import developer
urlpatterns = [
    path('',developer )
]