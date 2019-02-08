from django.views.generic import TemplateView

class AccessDeniedTemplate(TemplateView):
    template_name = 'error.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=403)