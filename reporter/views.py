from django.shortcuts import render
from django.http import HttpResponse
from .utils import build_pdf, get_data, build_plots

def getpdf(request):
    _data, dates = get_data()
    preprocessed_data = build_plots(_data,dates)
    return build_pdf(preprocessed_data)