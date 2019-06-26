import xlrd


def load_keywords(filename):
    keywords = []

    try:
        wb = xlrd.open_workbook(filename)
        sheet = wb.sheet_by_index(0) 
        sheet.cell_value(0, 0) 
  
        for i in range(sheet.nrows):
            key = sheet.cell_value(i, 0)
            if key == 'Keywords':
                continue
            keywords.append(key)
    except FileNotFoundError:
        print('No such file or directory: "{}" '.format(filename))

    return keywords
