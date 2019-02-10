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
from gss.settings.base import STATICFILES_DIRS
import os

def fetch_resources(uri,rel):
    return os.path.join(STATICFILES_DIRS[0], uri)

#Функция принимает начальные и конечные даты для составления отчета, id компаний и "окно" для под
def get_data(start_date = datetime.datetime(2017,1,1), end_date = datetime.datetime(2018,12,1), companies_ids=[1,2,3], window_value = 3):
    #Формирование id всех блоков из БД
    units_ids = list(Unit.objects.all().values_list('id', flat=True))
    #Объявление окна
    mouth_eps = relativedelta(months=window_value)
    #Формирование оси X для графика - месяцев в промежутке от start_date до end_date
    dates = list(rrule(MONTHLY, dtstart=start_date, until=end_date))
    #Формирование листа статистики для блоков
    units_stats = list()
    #Формирование словаря статистики для компаний, который содержит
    #Список компаний с FH по всем их самолетам и суммарный FH по всем самолетам для всех компаний
    companies_stats = dict()
    companies_stats["fh_stats"] = list()
    #Кол-во тиков для последующей оптимизации с помощью массивов numpy
    X_count = len(dates)
    #Несколько запросов к бд для последующего формирования датасетов
    #Запрошенные компании
    requested_companies = AircartCompany.objects.filter(id__in=companies_ids)
    #Самолеты запрошенных компаний
    requested_aircarts = Aircart.objects.filter(company__in=requested_companies)
    #Все (?) блоки из бд
    total_units = Unit.objects.all()
    #Все производители блоков
    total_manufacturers = UnitCreator.objects.all()
    #Все факты занесения статистики об времени полета для выбранных самолетов
    total_fh = AircartFlightRecord.objects.filter(aircart__in=requested_aircarts)
    #Все факты занесения статистики об removals/failures за весь период с учетом окна
    total_removals = UnitAction.objects.filter(date__range=[start_date-mouth_eps,end_date], action_type=0)
    total_failures = UnitAction.objects.filter(date__range=[start_date-mouth_eps,end_date], action_type=1)
    #Для каждого блока
    for unit_id in units_ids:
        #Выбираем из бд
        unit = total_units.get(id=unit_id)
        #определяем начальные значения вектора removals/failtures
        removals_stat = np.zeros(X_count)
        failures_stat = np.zeros(X_count)
        #Заполняем вектора
        for i in np.arange(X_count):
            removals = total_removals.filter(unit=unit_id, date__range=[dates[i]-mouth_eps,dates[i]]).count()
            failures = total_failures.filter(unit=unit_id, date__range=[dates[i]-mouth_eps,dates[i]]).count()
            fh = total_fh.filter(date__range=[dates[i]-mouth_eps,dates[i]]).aggregate(Sum("count"))['count__sum']
            removals = removals if removals!=0 else np.inf
            failures = failures if failures!=0 else np.inf
            #Основная формула
            removals_stat[i] = fh/removals
            failures_stat[i] = fh/failures
        #Заполняем статистику блоков
        units_stats.append({
            "number": unit.number,
            "supplier": unit.manufacturer.name,
            "removals": removals_stat,
            "failures": failures_stat
        })
    #Заполняем таблицу компаний суммарным fh для каждого самолетов компании
    for requested_company in requested_companies:
        companies_stats["fh_stats"].append({
            "board_number": requested_company.name,
            "value": total_fh.filter(aircart__in=requested_aircarts.filter(company=requested_company), date__range=[start_date,end_date]).aggregate(Sum("count"))['count__sum']
        })
    #Считаем суммарное fh для всех самолетов всех компаний
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
def build_report(context):
    #Из html
    template_path = 'pdf_report.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
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
    return response

#Функция для форматирования даты для отображения в pdf (см заголовок левой таблицы)
def get_date_bounds(dates):
    return {
        "start": dates[0].strftime("%B %Y"),
        "end": dates[-1].strftime("%B %Y"),
        "interval": len(dates)
    }