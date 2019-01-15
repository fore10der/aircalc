from django.views.generic.edit import FormView
from .forms import TestFileForm
from .specials import preprocess_xlsx, build_bars, draw as _draw, build_pdf#, fill_db
from django.http import HttpResponse
from django.shortcuts import render

class TestFileView(FormView):
    template_name = 'upload.html'
    form_class = TestFileForm
    success_url = '/'
    
    def form_valid(self, form):
        data = preprocess_xlsx(self.request.FILES['file_input'])
        bar_images = build_bars(data)
        true_context = {"images": bar_images}
        return build_pdf(true_context)

from xhtml2pdf import pisa
from django.template.loader import get_template

def html_to_pdf_directly(request):
    template_path = 'pdf.html'
    context = _draw()
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def draw(request):
    return render(request,'ass.html',_draw())