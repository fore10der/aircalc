from django.views.generic.edit import FormMixin
from django.views.generic import ListView
from .models import UploadedFile
from .forms import UploadForm
from .utils import xlsx_parse
from django.http import JsonResponse
from django.urls import reverse
from django.db.transaction import on_commit

class UploadFileView(ListView):
    queryset = UploadedFile.objects.order_by('-upload_date')
    template_name = 'upload.html'
    context_object_name = 'uploads'
    
    def post(self, form):
        file = self.request.FILES["file"]
        form = UploadForm(files=self.request.FILES)
        if form.is_valid():
            response = {'status': 'OK'}
            xlsx = UploadedFile.objects.create(file=file,uploader=self.request.user.username)
            on_commit(lambda: xlsx_parse.delay(xlsx.id))
        else:
            response = {'status': 'fail'}
        return JsonResponse(response)


