from django.views.generic import TemplateView

class AccessDeniedTemplate(TemplateView):
    template_name = 'error.html'