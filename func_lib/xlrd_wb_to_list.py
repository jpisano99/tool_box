import datetime
import xlrd


def xlrd_wb_to_list(wb, ws):
    #
    # This takes an xlrd worksheet object (wb & ws)
    # and converts it to a simple python list
    # It takes all XL_CELL_DATE objects
    # and changes to python datetime object
    #
    my_simple_list = []

    for my_row in range(ws.nrows):
        my_simple_row = []

        for my_col in range(ws.ncols):
            my_cell = ws.cell(my_row, my_col)

            if my_cell.ctype == xlrd.XL_CELL_DATE:
                tmp_val = datetime.datetime(*xlrd.xldate_as_tuple(my_cell.value, wb.datemode))
                my_simple_row.append(tmp_val)
            else:
                tmp_val = my_cell.value
                my_simple_row.append(tmp_val)

        my_simple_list.append(my_simple_row)

    return my_simple_list
