from django.shortcuts import render
from django.http import HttpResponse
from gss.utils import group_required
from .utils import build_report, get_data, build_plots, get_date_bounds

#Генерируем и собираем pdf
@group_required('can_report')
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