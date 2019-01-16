from openpyxl import load_workbook
from datetime import date, datetime
from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import date2num, num2date
import io
import base64
from xhtml2pdf import pisa
from django.template.loader import get_template

def build_bars(data):
    context = []
    for table_key, table_values in data.items():
        for item_values in table_values:
            ax = plt.subplot(111)
            ax.bar(num2date(item_values['statistic'][:,0]), item_values['statistic'][:,1], width=30)
            ax.xaxis_date()
            plt.title(item_values["name"])
            buf = io.BytesIO()
            plt.savefig(buf, format='png', dpi=100)
            image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            context.append(image_base64)
            buf.close()
            print(context)
            break
        break
    return context

def build_pdf(true_context):
    template_path = 'pdf.html'
    context = true_context
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

def preprocess_xlsx(filename):
    result = {}
    # TODO review this structure (what is the purpose)
    ll = {'FH': ['name', 'company', 'statistic'],
        'Removals': ['name', 'company', 'statistic'],
        'Failures': ['name', 'company', 'statistic'],
        'Induced': ['name', 'company', 'statistic']}
    for key in wb.get_sheet_names():
        main_dict = []
        for i in np.arange(wb.get_sheet_by_name(key).min_row + 1, wb.get_sheet_by_name(key).max_row):
            buff_dict = {}
            stat_dict = np.matrix([[date2num(wb.get_sheet_by_name(key).cell(row=wb.get_sheet_by_name(key).min_row, column=j).value),
                                    wb.get_sheet_by_name(key).cell(row=i, column=j).value if wb.get_sheet_by_name(key).cell(row=i, column=j).value != None else 0
                                    ] for j in np.arange(wb.get_sheet_by_name(key).min_column + 2, wb.get_sheet_by_name(key).max_column)])
            # stat_dict = []
            # for j in range(wb.get_sheet_by_name(key).min_column + 2, wb.get_sheet_by_name(key).max_column):
            #     stat_dict.append(np.array([wb.get_sheet_by_name(key).cell(row=wb.get_sheet_by_name(key).min_row, column=j).value,
            #                       wb.get_sheet_by_name(key).cell(row=i, column=j).value if wb.get_sheet_by_name(key).cell(row=i, column=j).value != None else 0]))
            buff_dict[ll[key][0]] = wb.get_sheet_by_name(key).cell(row=i, column=1).value
            buff_dict[ll[key][1]] = wb.get_sheet_by_name(key).cell(row=i, column=2).value
            buff_dict[ll[key][2]] = np.array(stat_dict)
            main_dict.append(buff_dict)
            main[key] = main_dict
    
    return main
