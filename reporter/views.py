from django.http import HttpResponse
from .utils import draw_plot

def download_pdf(request):
    draw_plot()
    return HttpResponse("ass we can")