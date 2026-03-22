from django.urls import path
from .views import ai_tools
urlpatterns = [
    path('',ai_tools )
]