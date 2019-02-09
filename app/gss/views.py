from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect

class AccessDeniedTemplate(TemplateView):
    template_name = 'error.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=403)

def redirect(request):
    if request.user.groups.filter(name='can_report').exists():
        return HttpResponseRedirect(reverse('reporter'))
    else:
        return HttpResponseRedirect(reverse('loader'))