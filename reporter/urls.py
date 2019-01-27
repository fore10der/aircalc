from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.download_pdf),
]