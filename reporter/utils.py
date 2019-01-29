import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import num2date, date2num
from django.http import HttpResponse
from django.template.loader import get_template
import io
import base64
from units.models import UnitAction, Unit
import datetime
from dateutil.rrule import rrule, MONTHLY
from dateutil.relativedelta import relativedelta
from xhtml2pdf import pisa

#Заглушка для таблицы
table = [ { 'Customer' :  1, 'F_H' : 11, 'NURn' :  111, 'NFn' : 1111, 'NR' : 11111},
{ 'Customer' :  2, 'F_H' : 22, 'NURn' :  222, 'NFn' : 2222, 'NR' : 22222},
{ 'Customer' :  3, 'F_H' : 33, 'NURn' :  333, 'NFn' : 3333, 'NR' : 33333},
{ 'Customer' :  4, 'F_H' : 44, 'NURn' :  444, 'NFn' : 4444, 'NR' : 44444}]

#Берем снятия/поломки в промежутке от 1-1-2017 ~ 2018-12-1 для всех блоков из бд с окном 3 месяца
def get_data(start_date = datetime.datetime(2017,1,1), end_date = datetime.datetime(2018,12,1), window_value = 3):
    units_ids = list(Unit.objects.all().values_list('id', flat=True))
    eps = (window_value - 1)//2 if window_value % 2 else window_value // 2
    mouth_eps = relativedelta(months=eps)
    dates = list(rrule(MONTHLY, dtstart=start_date, until=end_date))
    units_stats = list()
    X_count = len(dates)
    total_units = Unit.objects.all()
    total_removals = UnitAction.objects.filter(date__range=[start_date-mouth_eps,end_date + mouth_eps + relativedelta(months=1)], action_type=0)
    total_induced = UnitAction.objects.filter(date__range=[start_date-mouth_eps,end_date + mouth_eps + relativedelta(months=1)], action_type=1)
    for unit_id in units_ids:
        unit_number = total_units.get(id=unit_id).unit_number
        removals = np.zeros(X_count)
        induced = np.zeros(X_count)
        for i in np.arange(X_count):
            removals[i] = total_removals.filter(unit_id=unit_id, date__range=[dates[i]-mouth_eps,dates[i] + mouth_eps + relativedelta(months=1)], action_type=0).count()
            induced[i] = total_induced.filter(unit_id=unit_id, date__range=[dates[i]-mouth_eps,dates[i] + mouth_eps + relativedelta(months=1)], action_type=1).count()
        units_stats.append({
            "unit_number": unit_number,
            "removals": removals,
            "induceed": induced
        })
    return units_stats, dates

#Строим графики и формируем датасет для pdf
def build_plots(data, dates):
    units = []
    for unit_info in data:
        plt.clf()
        plt.figure(figsize=(8,7))
        for unit_key, unit_values in unit_info.items():
            if unit_key!='unit_number':
                plt.plot(dates,unit_values, label=unit_key)
        plt.title(unit_info["unit_number"])
        plt.legend()
        plt.gcf().autofmt_xdate()
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=100)
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
        units.append({
            "title": unit_info["unit_number"],
            "plot": image_base64,
            #TO DO: удалить заглушку данных с таблицы
            "table": table
            }),
        buf.close()
    return units

def build_pdf(true_context):
    template_path = 'report.html'
    context = {"units": true_context}
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