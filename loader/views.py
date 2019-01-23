from django.views.generic.edit import FormView
from .forms import TestFileForm
from .utils import preprocess_xlsx, store_to_db #draw_plot, build_bars, build_pdf,
from django.http import HttpResponse
from django.shortcuts import render

class TestFileView(FormView):
    template_name = 'upload.html'
    form_class = TestFileForm
    success_url = '/'
    
    def form_valid(self, form):
        data = preprocess_xlsx(self.request.FILES['file_input'])
        print(data)
        store_to_db(data)
