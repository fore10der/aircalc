from django.views.generic.edit import FormMixin
from django.views.generic import ListView
from .models import UploadedFile
from .forms import UploadForm
from .utils import xlsx_parse
from django.http import JsonResponse
from django.urls import reverse
from django.db.transaction import on_commit
from celery.task.control import inspect


class UploadFileView(ListView):
    queryset = UploadedFile.objects.order_by('-upload_date')
    template_name = 'upload.html'
    context_object_name = 'uploads'

    def get_context_data(self, **kwargs):
        context = super(UploadFileView, self).get_context_data(**kwargs)
        context['is_ready'] = True # not bool(inspect().active()['celery@uploads'])
        return context
    
    def post(self, form):
        uploader_name = self.request.user.username
        file = self.request.FILES["file"]
        form = UploadForm(files=self.request.FILES)
        if form.is_valid():
            response = {'status': 'OK'}
            xlsx = UploadedFile.objects.create(file=file,uploader=uploader_name)
            on_commit(lambda: xlsx_parse.delay(xlsx.id))
        else:
            response = {'status': 'fail'}
        print(inspect().active())
        print(inspect().reserved())
        print(inspect().scheduled())
        return JsonResponse(response)


