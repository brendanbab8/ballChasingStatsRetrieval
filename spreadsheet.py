'''
Functions used to add data to the spreadsheet
'''

from typing import Tuple
import xlsxwriter as xlsx
import templates as tp

'''
[create_columns b s] builds the labels for columns as specified on the
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


'''
[create_rows s r i] builds row [r] in the spreadsheet [s] at row [i].
'''


def create_row(sheet: xlsx.Workbook.worksheet_class, row: Tuple[str, str, any],
               index: int):
    sheet.write_string(index, 0, row[0])
    sheet.write_string(index, 1, row[1])
    data = row[2]
    sheet.write_number(index, 2, data["games"])
    sheet.write_number(index, 3, data["wins"])
    sheet.write_number(index, 4, data["win_percentage"])
    sheet.write_number(index, 5, data["play_duration"])

    core(sheet, index, data["core"])
    boost(sheet, index, data["boost"])
    movement(sheet, index, data["movement"])
    position(sheet, index, data["positioning"])
    demo(sheet, index, data["demo"])


'''
[core s r c cr] builds rows for data in [cr] in spreadsheet [s], using row [r] 
and starting at column [c].
'''


def core(sheet: xlsx.Workbook.worksheet_class, row: int, core: any):
    sheet.write_number(row, 6, core["shots"])
    sheet.write_number(row, 7, core["shots_against"])
    sheet.write_number(row, 8, core["goals"])
    sheet.write_number(row, 9, core["goals_against"])
    sheet.write_number(row, 10, core["saves"])
    sheet.write_number(row, 11, core["assists"])
    sheet.write_number(row, 12, core["score"])
    sheet.write_number(row, 13, core["mvp"])
    sheet.write_number(row, 14, core["shooting_percentage"])


'''
[boost s r c b] builds rows for data in [b] in spreadsheet [s], using row [r] 
and starting at column [c].
'''


def boost(sheet: xlsx.Workbook.worksheet_class, row: int, boost: any):
    pass


'''
[movement s r c m] builds rows for data in [m] in spreadsheet [s], using row 
[r] and starting at column [c].
'''


def movement(sheet: xlsx.Workbook.worksheet_class, row: int, move: any):
    pass


'''
[position s r c p] builds rows for data in [p] in spreadsheet [s], using row 
[r] and starting at column [c].
'''


def position(sheet: xlsx.Workbook.worksheet_class, row: int, position: any):
    pass


'''
[demo s r c d] builds rows for data in [d] in spreadsheet [s], using row [r] 
and starting at column [c].
'''


def demo(sheet: xlsx.Workbook.worksheet_class, row: int, demo: any):
    pass
