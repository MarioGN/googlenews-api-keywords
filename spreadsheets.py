import xlrd
from xlwt import Workbook
from xlutils.copy import copy


headers = ('Keywords', 'URL', 'Publication', 'Date')
workbook_name = 'output.xls'

def init_outputfile():
    wb = Workbook()
    sheet1 = wb.add_sheet('keywords 1')

    for i in range(len(headers)):
        sheet1.write(0, i, headers[i])

    wb.save(workbook_name)


def save_from_api(keyword, results):
    rb = xlrd.open_workbook(workbook_name, formatting_info=True)
    sheet1 = rb.sheet_by_index(0)
    i = sheet1.nrows

    wb = copy(rb)
    sheet1 = wb.get_sheet(0)

    for r  in list(results['articles']):
        sheet1.write(i, 0, keyword)
        sheet1.write(i, 1, r['title'])
        sheet1.write(i, 2, r['publishedAt'])
        sheet1.write(i, 3, r['url'])

        i += 1


    wb.save(workbook_name)


def save_from_lib(results):
    rb = xlrd.open_workbook(workbook_name, formatting_info=True)
    sheet1 = rb.sheet_by_index(0)
    i = sheet1.nrows

    wb = copy(rb)
    sheet1 = wb.get_sheet(0)
    
    for key, key_results in results.items():
        for r in key_results:
            sheet1.write(i, 0, key)
            sheet1.write(i, 1, r['title'])
            sheet1.write(i, 2, r['date'])
            sheet1.write(i, 3, r['link'])

            i += 1

    
    wb.save('output.xls')
