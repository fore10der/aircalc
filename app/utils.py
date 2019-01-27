import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
import os

def build_pdf(true_context):
    template_path = 'report.html'
    context = true_context
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(html, dest=response, encoding='UTF-8')
    # if error then show some funy view
    print(pisaStatus.error)
    if not pisaStatus.error:
       return HttpResponse('We had some errors <pre>' + html +'</pre>')
    return response