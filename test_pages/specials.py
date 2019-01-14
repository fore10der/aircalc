from openpyxl import load_workbook
from datetime import date, datetime
from actions.models import FH, Failture, Removal, Included
from aircarts.models import Aircart
from companies.models import Company

def is_saved(record):
    print(Company.objects.filter(name=record['company']))

def preprocess_xlsx_v2(file):
    wb = load_workbook(filename=file)

    sheet = wb.active

    main = {}

    ll = {'FH': ['name', 'company', 'statistic'],
        'Removals': ['name', 'company', 'statistic'],
        'Failures': ['name', 'company', 'statistic'],
        'Induced': ['name', 'company', 'statistic']}
    for key in wb.get_sheet_names():
        main_dict = []
        for i in range(wb.get_sheet_by_name(key).min_row + 1, wb.get_sheet_by_name(key).max_row):
            buff_dict = {}
            stat_dict = []
            for j in range(wb.get_sheet_by_name(key).min_column + 2, wb.get_sheet_by_name(key).max_column):
                stat_dict.append({'date':wb.get_sheet_by_name(key).cell(row=wb.get_sheet_by_name(key).min_row, column=j).value,
                                'count':wb.get_sheet_by_name(key).cell(row=i, column=j).value})
            buff_dict[ll[key][0]] = wb.get_sheet_by_name(key).cell(row=i, column=1).value
            buff_dict[ll[key][1]] = wb.get_sheet_by_name(key).cell(row=i, column=2).value
            buff_dict[ll[key][2]] = stat_dict
            main_dict.append(buff_dict)
            main[key] = main_dict
    
    return main

# def fill_db(data):
#     for key, actions in data.items():
#         if (key == 'FH'):
#             fill_actions(actions,FH)
#         elif (key == 'Removals'):
#             fill_actions(actions,Removal)
#         elif (key == 'Failures'):
#             fill_actions(actions,Failture)
#         elif (key == 'Induced'):
#             fill_actions(actions,Included)
# def fill_actions(actions, DB):
#     for action in actions:
#         if (is_saved(action)):
#             Aircart.save(name=action['name'],company=action['company'])

