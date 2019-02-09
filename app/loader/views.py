from django.views.generic.edit import FormMixin
from django.views.generic import ListView
from .forms import TestFileForm
from .models import UploadedFile
from .utils import preprocess_xlsx, store_to_db
from django.shortcuts import render

class UploadFileView(FormMixin,ListView):
    queryset = UploadedFile.objects.order_by('-upload_date')
    template_name = 'upload.html'
    context_object_name = 'uploads'
    form_class = TestFileForm
    success_url = '/'
    
    def form_valid(self, form):
        data = preprocess_xlsx(self.request.FILES['file_input'])
        store_to_db(data)
