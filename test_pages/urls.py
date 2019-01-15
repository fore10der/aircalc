from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.TestFileView.as_view()),
    path('1', views.html_to_pdf_directly),
    path('draw', views.draw)
]