from django.views.generic.edit import FormMixin
from django.views.generic import ListView
from .models import ReportedFile
from .forms import ReportedForm
from gss.utils import group_required
from .utils import create_pdf
from django.http import JsonResponse


class ReportFileView(FormMixin,ListView):
    queryset = ReportedFile.objects.order_by('-generate_date')
    template_name = 'report.html'
    context_object_name = 'reports'
    model = ReportedFile
    form_class = ReportedForm

    def post(self, form):
        request_info = self.request.POST.dict()
        request_info['creator_name'] = self.request.user.username
        request_info['creator_id'] = self.request.user.id
        create_pdf.delay(**request_info)
        return JsonResponse(self.request.POST)