import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import num2date
from django.http import HttpResponse
from django.template.loader import get_template
from django.db.models import F, Sum
import io
import base64
from units.models import UnitAction
import datetime
from dateutil.rrule import rrule, MONTHLY
from dateutil.relativedelta import relativedelta




def draw_plot(start_date = datetime.datetime(2017,1,1), end_date = datetime.datetime(2018,12,1), unit_id = 1, window_value = 3):
    eps = (window_value - 1)//2 if window_value % 2 else window_value // 2
    mouth_eps = relativedelta(months=eps)
    dates = list(rrule(MONTHLY, dtstart=start_date, until=end_date))
    X_count = len(dates)
    total_removals = UnitAction.objects.filter(unit_id=unit_id, date__range=[start_date-mouth_eps,end_date + mouth_eps + relativedelta(months=1)], action_type=0)
    total_induced = UnitAction.objects.filter(unit_id=unit_id, date__range=[start_date-mouth_eps,end_date + mouth_eps + relativedelta(months=1)], action_type=1)
    removals = np.zeros(X_count)
    induced = np.zeros(X_count)
    for i in np.arange(X_count):
        removals[i] = total_removals.filter(unit_id=unit_id, date__range=[dates[i]-mouth_eps,dates[i] + mouth_eps + relativedelta(months=1)], action_type=0).count()
        induced[i] = total_induced.filter(unit_id=unit_id, date__range=[dates[i]-mouth_eps,dates[i] + mouth_eps + relativedelta(months=1)], action_type=1).count()
    print(removals)
    print(induced)

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