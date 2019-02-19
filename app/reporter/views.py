from django.views.generic.edit import FormMixin
from django.views.generic import ListView
from .models import ReportedFile
from .forms import ReportedForm
from gss.utils import group_required
from .utils import build_report, get_data, build_plots, get_date_bounds

class ReportFileView(FormMixin,ListView):
    queryset = ReportedFile.objects.order_by('-generate_date')
    template_name = 'report.html'
    context_object_name = 'reports'
    model = ReportedFile
    form_class = ReportedForm

    def get_context_data(self, **kwargs):
        context = super(ReportFileView, self).get_context_data(**kwargs)
        context['is_ready'] = not bool(inspect().active()['celery@uploads'])
        return context

    def post(self, form):
        companies_stats, units_stats, dates = get_data(self.request.POST["report_date_start"],self.request.POST["report_date_end"])
        unit_plots = build_plots(units_stats,dates)
        date_bounds = get_date_bounds(dates)
        return build_report({"companies_stats": companies_stats,
        "units_stats": unit_plots,
        "report_bounds": date_bounds},
        {
            "filename": self.request.POST["report_name"],
            "report_date_start": self.request.POST["report_date_start"],
            "report_date_end": self.request.POST["report_date_end"],
            "creator": self.request.user.username
        })

#Генерируем и собираем pdf
def getpdf(request):
    #Собираем статистику
    companies_stats, units_stats, dates = get_data()
    #Рисуем графики
    unit_plots = build_plots(units_stats,dates)
    #Получаем ограничения дат
    date_bounds = get_date_bounds(dates)
    #Возвращаем запрос на скачивание
    return build_report({"companies_stats": companies_stats,
        "units_stats": unit_plots,
        "report_bounds": date_bounds})