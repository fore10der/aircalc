from openpyxl import load_workbook
from datetime import date, datetime
from actions.models import FH, Failture, Removal, Included
from aircarts.models import Aircart
from companies.models import Company

def is_saved(record):
    print(Company.objects.filter(name=record['company']))

def preprocess_xlsx(filename):
    result = {}
    # TODO review this structure (what is the purpose)
    ll = {'FH': ['name', 'company', 'statistic'],
        'Removals': ['name', 'company', 'statistic'],
        'Failures': ['name', 'company', 'statistic'],
        'Induced': ['name', 'company', 'statistic']}
    wb = load_workbook(filename=filename, read_only=True)
    for sheet in wb:
        title = sheet.title
        sheet_data = []
        min_row = sheet.min_row
        max_row = sheet.max_row
        min_column = sheet.min_column
        max_column = sheet.max_column
        # TODO rewiew ranges below
        for i in range(min_row + 1, max_row):
            # TODO review variable naming
            stat = []
            for j in range(min_column + 2, max_column):
                stat.append({
                        'date' : sheet.cell(row=min_row, column=j).value,
                        'count' : sheet.cell(row=i, column=j).value,
                })
            keys = ll[title]
            sheet_data.append({
                keys[0] : sheet.cell(row=i, column=1).value,
                keys[1] : sheet.cell(row=i, column=2).value,
                keys[2] : stat,
            })
        result[title] = sheet_data
    return result