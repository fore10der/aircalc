from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import render_to_string
import io

def render_to_pdf(template_src, context_dict):
    result = io.BytesIO()
    template = render_to_string(template_src, context_dict)
    pdf = pisa.pisaDocument(io.BytesIO(template.encode('UTF-8')), result)

    if not pdf.error:
        return HttpResponse(result.getvalue(), content_type='application/pdf')

    return None