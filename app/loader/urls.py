from . import views
from django.urls import path, include
from gss.utils import group_required

urlpatterns = [
    path('', group_required('can_input')(views.TestFileView.as_view()), name="loader"),
    path('/test',group_required('can_input')(views.TestFileView.as_view()), name="loader"),
]