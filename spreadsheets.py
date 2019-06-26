import xlrd
from xlwt import Workbook
from xlutils.copy import copy
from decouple import config


headers = ('Keywords', 'URL', 'Publication', 'Date')
workbook_name = config('OUTPUT_FILE', default='output.xls')


def init_outputfile(filename):
    wb = Workbook()
    sheet1 = wb.add_sheet('keywords 1')

    for i in range(len(headers)):
        sheet1.write(0, i, headers[i])

    wb.save(filename)


def save(keyword, results):
    rb = xlrd.open_workbook(workbook_name, formatting_info=True)
    sheet1 = rb.sheet_by_index(0)
    i = sheet1.nrows

    wb = copy(rb)
    sheet1 = wb.get_sheet(0)

    for r  in list(results['articles']):
        sheet1.write(i, 0, keyword)
        sheet1.write(i, 1, r['url'])
        sheet1.write(i, 2, r['title'])
        sheet1.write(i, 3, r['publishedAt'])

        i += 1


    wb.save(workbook_name)
