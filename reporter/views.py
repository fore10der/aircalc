from django.shortcuts import render
from django.http import HttpResponse
from .utils import build_report, get_data, build_plots, get_date_bounds

def getpdf(request):
    companies_stats, units_stats, dates = get_data()
    unit_plots = build_plots(units_stats,dates)
    date_bounds = get_date_bounds(dates)
    return build_report({"companies_stats": companies_stats,
        "units_stats": unit_plots,
        "report_bounds": date_bounds})