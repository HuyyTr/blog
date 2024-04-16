from django.urls import path, include
from . import views

app_name = 'ai_app'

urlpatterns = [
    path('', views.hello),
]
