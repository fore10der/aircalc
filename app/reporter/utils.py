import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import num2date, date2num
from django.http import HttpResponse
from django.template.loader import get_template
import io
import base64
from django.db.models import Sum
from units.models import UnitAction, Unit, UnitCreator
from aircarts.models import AircartFlightRecord, Aircart, AircartCompany
import datetime
from dateutil.rrule import rrule, MONTHLY
from dateutil.relativedelta import relativedelta
from xhtml2pdf import pisa
from gss.settings.base import MEDIA_ROOT
from .models import ReportedFile

import os

def fetch_resources(uri,rel):
    return os.path.join(MEDIA_ROOT, uri)

#Функция принимает начальные и конечные даты для составления отчета, id компаний и "окно" для под
def get_data(start_date_str, end_date_str, window_value = 3, companies_ids=None):
    start_date = datetime.datetime.strptime(start_date_str,'%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date_str,'%Y-%m-%d')
    #Определение начальных переменных
    units = Unit.objects.all()
    mouth_eps = relativedelta(months=window_value)
    dates = list(rrule(MONTHLY, dtstart=start_date, until=end_date))
    units_stats = list()
    companies_stats = dict()
    companies_stats["fh_stats"] = list()
    X_count = len(dates)
    requested_companies = AircartCompany.objects.all() if companies_ids is None else AircartCompany.objects.filter(id__in=companies_ids)
    requested_aircarts = Aircart.objects.filter(company__in=requested_companies)
    total_units = Unit.objects.all()
    total_manufacturers = UnitCreator.objects.all()
    total_fh = AircartFlightRecord.objects.filter(aircart__in=requested_aircarts)
    total_removals = UnitAction.objects.filter(date__range=[start_date-mouth_eps,end_date], action_type=0)
    total_failures = UnitAction.objects.filter(date__range=[start_date-mouth_eps,end_date], action_type=1)
    #Подсчет статистики за каждый месяц периода отчета по блокам
    for unit in units:
        removals_stat = np.zeros(X_count)
        failures_stat = np.zeros(X_count)
        for i in np.arange(X_count):
            removals = total_removals.filter(unit=unit, date__range=[dates[i]-mouth_eps,dates[i]]).count()
            failures = total_failures.filter(unit=unit, date__range=[dates[i]-mouth_eps,dates[i]]).count()
            fh = total_fh.filter(date__range=[dates[i]-mouth_eps,dates[i]]).aggregate(Sum("count"))['count__sum']
            removals = removals if removals else np.inf
            failures = failures if failures else np.inf
            fh = fh if fh else 0
            removals_stat[i] = fh/removals
            failures_stat[i] = fh/failures
        #Заполние статистики
        units_stats.append({
            "number": unit.number,
            "supplier": unit.manufacturer.name,
            "removals": removals_stat,
            "failures": failures_stat
        })
    #Подсчет и заполнение статистики для компаний
    for requested_company in requested_companies:
        value = total_fh.filter(aircart__in=requested_aircarts.filter(company=requested_company), date__range=[start_date,end_date]).aggregate(Sum("count"))['count__sum']
        value = value if value else 0
        companies_stats["fh_stats"].append({
            "board_number": requested_company.name,
            "value": value
        })
    companies_stats["total_fh"] = sum([fh_stat["value"] for fh_stat in companies_stats["fh_stats"]])
    #Функция возвращает статистику для компаний, блоков (для постройки графиков) и даты формирования отчета в виде массива
    return companies_stats, units_stats, dates

#Строим графики
def build_plots(unit_stats, dates):
    units_plots = []
    #Для каждого блока
    for unit_stat in unit_stats:
        #Чистим и определяем размеры графика
        plt.clf()
        plt.figure(figsize=(8,7))
        #строим графики по нумерным свойствам (failtures/removals)
        for unit_key, unit_values in unit_stat.items():
            if unit_key!='number' and unit_key!='supplier':
                plt.plot(dates,unit_values, label=unit_key)
        plt.title(unit_stat["number"])
        plt.legend()
        plt.gcf().autofmt_xdate()
        #Сохраняем в двоичный поток сформированный график
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=100)
        #Преобразуем график для рендера в html
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
        #Добавляем в список
        units_plots.append({
            "number": unit_stat["number"],
            "supplier": unit_stat["supplier"],
            "plot": image_base64
            }),
        buf.close()
    #Возвращаем список графиков с опорным содержимым
    return units_plots

#Загружаем pdf
def build_report(context,docinfo):
    #Из html
    template_path = 'pdf_report.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{0}.pdf"'.format(docinfo["filename"])
    # Находим и рендерим в переменную
    template = get_template(template_path)
    html = template.render(context)
    # Создаем с последующей выдачей юзверю
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=fetch_resources)
    # Проверяем ошибки
    print(pisaStatus.err)
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
       # TODO Repair
    # ReportedFile.objects.create(file=pisaStatus, \
    #     reporter=docinfo["creator"], \
    #     report_date_start=docinfo["report_date_start"], \
    #     report_date_end=docinfo["report_date_end"])
    return response

#Функция для форматирования даты для отображения в pdf (см заголовок левой таблицы)
def get_date_bounds(dates):
    return {
        "start": dates[0].strftime("%B %Y"),
        "end": dates[-1].strftime("%B %Y"),
        "interval": len(dates)
    }