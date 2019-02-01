import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import num2date, date2num
from django.http import HttpResponse
from django.template.loader import get_template
import io
import base64
from django.db.models import Sum
from units.models import UnitAction, Unit, UnitCreator
from aircarts.models import PlaneFlightHours, Plane, PlaneCompany
import datetime
from dateutil.rrule import rrule, MONTHLY
from dateutil.relativedelta import relativedelta
from xhtml2pdf import pisa

#Функция принимает начальные и конечные даты для составления отчета, id компаний и "окно" для под
def get_data(start_date = datetime.datetime(2017,1,1), end_date = datetime.datetime(2018,12,1), companies_ids=[1,2,3], window_value = 3):
    #Формирование id всех блоков из БД
    units_ids = list(Unit.objects.all().values_list('id', flat=True))
    #Объявление окна
    mouth_eps = relativedelta(months=window_value)
    
    dates = list(rrule(MONTHLY, dtstart=start_date, until=end_date))
    units_stats = list()
    companies_stats = dict()
    companies_stats["fh_stats"] = list()
    X_count = len(dates)
    requested_companies = PlaneCompany.objects.filter(id__in=companies_ids)
    requested_planes = Plane.objects.filter(company_id__in=requested_companies)
    total_units = Unit.objects.all()
    total_manufacturers = UnitCreator.objects.all()
    total_fh = PlaneFlightHours.objects.filter(plane_id__in=requested_planes)
    total_removals = UnitAction.objects.filter(date__range=[start_date-mouth_eps,end_date], action_type=0)
    total_failures = UnitAction.objects.filter(date__range=[start_date-mouth_eps,end_date], action_type=1)
    for unit_id in units_ids:
        unit = total_units.get(id=unit_id)
        removals_stat = np.zeros(X_count)
        failures_stat = np.zeros(X_count)
        for i in np.arange(X_count):
            removals = total_removals.filter(unit_id=unit_id, date__range=[dates[i]-mouth_eps,dates[i]]).count()
            failures = total_failures.filter(unit_id=unit_id, date__range=[dates[i]-mouth_eps,dates[i]]).count()
            fh = total_fh.filter(date__range=[dates[i]-mouth_eps,dates[i]]).aggregate(Sum("count"))['count__sum']
            removals = removals if removals!=0 else np.inf
            failures = failures if failures!=0 else np.inf
            removals_stat[i] = fh/removals
            failures_stat[i] = fh/failures
        units_stats.append({
            "number": unit.unit_number,
            "supplier": unit.manufacturer_id.name,
            "removals": removals_stat,
            "failures": failures_stat
        })
    print(units_stats)
    for requested_company in requested_companies:
        companies_stats["fh_stats"].append({
            "board_number": requested_company.name,
            "value": total_fh.filter(plane_id__in=requested_planes.filter(company_id=requested_company), date__range=[start_date,end_date]).aggregate(Sum("count"))['count__sum']
        })
    companies_stats["total_fh"] = sum([fh_stat["value"] for fh_stat in companies_stats["fh_stats"]])
    return companies_stats, units_stats, dates

#Строим графики и формируем датасет для pdf
def build_plots(unit_stats, dates):
    units_plots = []
    for unit_stat in unit_stats:
        plt.clf()
        plt.figure(figsize=(8,7))
        for unit_key, unit_values in unit_stat.items():
            if unit_key!='number' and unit_key!='supplier':
                plt.plot(dates,unit_values, label=unit_key)
        plt.title(unit_stat["number"])
        plt.legend()
        plt.gcf().autofmt_xdate()
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=100)
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
        units_plots.append({
            "number": unit_stat["number"],
            "supplier": unit_stat["supplier"],
            "plot": image_base64
            }),
        buf.close()
    return units_plots

def build_report(context):
    template_path = 'report.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    print(pisaStatus.err)
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def get_date_bounds(dates):
    return {
        "start": dates[0].strftime("%B %Y"),
        "end": dates[-1].strftime("%B %Y"),
        "interval": len(dates)
    }