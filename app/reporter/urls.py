from . import views
from django.urls import path, include
from gss.utils import group_required

urlpatterns = [
    path('', views.ReportFileView.as_view(), name='reporter'),
]