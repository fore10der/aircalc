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
    
    def post(self, form):
        file = self.request.FILES['file_input']
        data = preprocess_xlsx(file)
        store_to_db(data)
        UploadedFile.objects.create(file=file,uploader=self.request.user.username)
        return self.form_valid(form)
        
    def form_valid(self, form):
        return super().form_valid(form)