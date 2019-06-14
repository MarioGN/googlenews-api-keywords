import xlwt 
from xlwt import Workbook 


def save(results):
    wb = Workbook()

    sheet1 = wb.add_sheet('Sheet 1')

    i = 0
    for key, key_results in results.items():
        for r in key_results:
            sheet1.write(i, 0, key)
            sheet1.write(i, 1, r['title'])
            sheet1.write(i, 2, r['date'])
            sheet1.write(i, 3, r['link'])

            i += 1

    
    wb.save('output.xls')
