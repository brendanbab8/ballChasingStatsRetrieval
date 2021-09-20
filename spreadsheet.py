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
    sheet.write_number(row, 15, boost["bpm"])
    sheet.write_number(row, 16, boost["bcpm"])
    sheet.write_number(row, 17, boost["avg_amount"])
    sheet.write_number(row, 18, boost["amount_collected"])
    sheet.write_number(row, 19, boost["amount_stolen"])
    sheet.write_number(row, 20, boost["amount_collected_big"])
    sheet.write_number(row, 21, boost["amount_stolen_big"])
    sheet.write_number(row, 22, boost["amount_collected_small"])
    sheet.write_number(row, 23, boost["amount_stolen_small"])
    sheet.write_number(row, 24, boost["count_collected_big"])
    sheet.write_number(row, 25, boost["count_stolen_big"])
    sheet.write_number(row, 26, boost["count_collected_small"])
    sheet.write_number(row, 27, boost["count_stolen_small"])
    sheet.write_number(row, 28, boost["time_zero_boost"])
    sheet.write_number(row, 29, boost["percent_zero_boost"])
    sheet.write_number(row, 30, boost["time_full_boost"])
    sheet.write_number(row, 31, boost["percent_full_boost"])
    sheet.write_number(row, 32, boost["amount_overfill"])
    sheet.write_number(row, 33, boost["amount_overfill_stolen"])
    sheet.write_number(row, 34, boost["amount_used_while_supersonic"])
    sheet.write_number(row, 35, boost["time_boost_0_25"])
    sheet.write_number(row, 36, boost["time_boost_25_50"])
    sheet.write_number(row, 37, boost["time_boost_50_75"])
    sheet.write_number(row, 38, boost["time_boost_75_100"])
    sheet.write_number(row, 39, boost["percent_boost_0_25"])
    sheet.write_number(row, 40, boost["percent_boost_25_50"])
    sheet.write_number(row, 41, boost["percent_boost_50_75"])
    sheet.write_number(row, 42, boost["percent_boost_75_100"])


'''
[movement s r c m] builds rows for data in [m] in spreadsheet [s], using row 
[r] and starting at column [c].
'''


def movement(sheet: xlsx.Workbook.worksheet_class, row: int, move: any):
    sheet.write_number(row, 43, move["avg_speed"])
    sheet.write_number(row, 44, move["total_distance"])
    sheet.write_number(row, 45, move["time_supersonic_speed"])
    sheet.write_number(row, 46, move["time_boost_speed"])
    sheet.write_number(row, 47, move["time_slow_speed"])
    sheet.write_number(row, 48, move["time_ground"])
    sheet.write_number(row, 49, move["time_low_air"])
    sheet.write_number(row, 50, move["time_high_air"])
    sheet.write_number(row, 51, move["time_powerslide"])
    sheet.write_number(row, 52, move["count_powerslide"])
    sheet.write_number(row, 53, move["avg_powerslide_duration"])
    sheet.write_number(row, 54, move["avg_speed_percentage"])
    sheet.write_number(row, 55, move["percent_slow_speed"])
    sheet.write_number(row, 56, move["percent_boost_speed"])
    sheet.write_number(row, 57, move["percent_supersonic_speed"])
    sheet.write_number(row, 58, move["percent_ground"])
    sheet.write_number(row, 59, move["percent_low_air"])
    sheet.write_number(row, 60, move["percent_high_air"])


'''
[position s r c p] builds rows for data in [p] in spreadsheet [s], using row 
[r] and starting at column [c].
'''


def position(sheet: xlsx.Workbook.worksheet_class, row: int, position: any):
    sheet.write_number(row, 61, position["avg_distance_to_ball"])
    sheet.write_number(row, 62, position["avg_distance_to_ball_possession"])
    sheet.write_number(row, 63, position["avg_distance_to_ball_no_possession"])
    sheet.write_number(row, 64, position["time_defensive_third"])
    sheet.write_number(row, 65, position["time_neutral_third"])
    sheet.write_number(row, 66, position["time_offensive_third"])
    sheet.write_number(row, 67, position["time_defensive_half"])
    sheet.write_number(row, 68, position["time_offensive_half"])
    sheet.write_number(row, 69, position["time_behind_ball"])
    sheet.write_number(row, 70, position["time_infront_ball"])
    sheet.write_number(row, 71, position["time_most_back"])
    sheet.write_number(row, 72, position["time_most_forward"])
    sheet.write_number(row, 73, position["goals_against_while_last_defender"])
    sheet.write_number(row, 74, position["time_closest_to_ball"])
    sheet.write_number(row, 75, position["time_farthest_from_ball"])
    sheet.write_number(row, 76, position["percent_defensive_third"])
    sheet.write_number(row, 77, position["percent_offensive_third"])
    sheet.write_number(row, 78, position["percent_neutral_third"])
    sheet.write_number(row, 79, position["percent_defensive_half"])
    sheet.write_number(row, 80, position["percent_offensive_half"])
    sheet.write_number(row, 81, position["percent_behind_ball"])
    sheet.write_number(row, 82, position["percent_infront_ball"])


'''
[demo s r c d] builds rows for data in [d] in spreadsheet [s], using row [r] 
and starting at column [c].
'''


def demo(sheet: xlsx.Workbook.worksheet_class, row: int, demo: any):
    sheet.write_number(row, 83, demo["inflicted"])
    sheet.write_number(row, 84, demo["taken"])
