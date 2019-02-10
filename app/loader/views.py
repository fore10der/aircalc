from django.views.generic.edit import FormMixin
from django.views.generic import ListView
from .forms import TestFileForm
from .models import UploadedFile
from .utils import preprocess_xlsx, store_to_db
from django.shortcuts import render
from django.http import HttpRequest
from django.urls import reverse


class UploadFileView(FormMixin,ListView):
    queryset = UploadedFile.objects.order_by('-upload_date')
    template_name = 'upload.html'
    context_object_name = 'uploads'
    form_class = TestFileForm
    success_url = '/'
    
    def post(self, form):
        data = preprocess_xlsx(self.request.FILES['file_input'])
        store_to_db(data)
        UploadedFile.objects.create(file=self.request.FILES['file_input'],uploader=self.request.user.username)
        return HttpRequest(reverse('loader'))