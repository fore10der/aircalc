from django.views.generic.edit import FormView
from .forms import TestFileForm
from .specials import preprocess_xlsx, build_bars, build_pdf, store_to_db
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
        # bar_images = build_bars(data)
        # true_context = {"images": bar_images}
        # #return render(self.request,'pdf.html',true_context)
        # return build_pdf(true_context)