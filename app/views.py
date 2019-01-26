from django.shortcuts import render
from django.http import HttpResponse
from .utils import build_pdf

block1_title= "Заголовок"

block2_table = [ { 'Customer' :  1, 'F_H' : 11, 'NURn' :  111, 'NFn' : 1111, 'NR' : 11111},
{ 'Customer' :  2, 'F_H' : 22, 'NURn' :  222, 'NFn' : 2222, 'NR' : 22222},
{ 'Customer' :  3, 'F_H' : 33, 'NURn' :  333, 'NFn' : 3333, 'NR' : 33333},
{ 'Customer' :  4, 'F_H' : 44, 'NURn' :  444, 'NFn' : 4444, 'NR' : 44444}]
    
block3_image = "image"

data = {
        "block1_title": block1_title,
        "block2_table": block2_table,
        "block3_image": block3_image
    }
    
def index(request):    
    return render(request, "report.html", context=data)

def getpdf(request):
    return build_pdf(data)