from .views import UploadedFileList, ReportedFileList
from django.urls import path

urlpatterns = [
    path("uploads/", UploadedFileList.as_view(), name="uploadsapi"),
    path("reports/", ReportedFileList.as_view(), name="reportsapi"),
]