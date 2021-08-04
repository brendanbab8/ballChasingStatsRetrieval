'''
Functions used to add data to the spreadsheet
'''

import xlsxwriter as xlsx
import templates as tp

'''
[create_columns s] builds the labels for columns as specified on the
BallChasing site.
'''
def create_columns(book: xlsx.Workbook, sheet: xlsx.Workbook.worksheet_class):
  col = 0
  cell_format = book.add_format()
  cell_format.set_bold()
  cell_format.set_text_wrap()
  cell_format.set_align("center")
  for title in tp.columns:
    sheet.set_column(col, col, 30)
    sheet.write_string(0, col, title, cell_format=cell_format)
    col += 1