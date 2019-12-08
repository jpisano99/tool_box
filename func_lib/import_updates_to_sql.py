from my_app.func_lib.open_wb import open_wb
from my_app.settings import app_cfg
from my_app.func_lib.push_list_to_csv import push_list_to_csv
from my_app.func_lib.db_tools import create_tables
from my_app.func_lib.xlrd_wb_to_csv import xlrd_wb_to_csv
from my_app.func_lib.load_infile import load_infile
import datetime


def import_updates_to_sql():
    create_tables()
    now = datetime.datetime.now()

    #
    # Import Delivery
    #
    wb, ws = open_wb(app_cfg['XLS_AS_DELIVERY_STATUS'])
    my_csv = xlrd_wb_to_csv(wb, ws)

    my_new_list = []
    for my_row in my_csv:
        my_row.insert(0, '')
        my_new_list.append(my_row)

    push_list_to_csv(my_new_list, 'csv_services.csv')
    load_infile('services', 'csv_services.csv')

    #
    # Import Subscriptions
    #
    wb, ws = open_wb(app_cfg['XLS_SUBSCRIPTIONS'])
    my_csv = xlrd_wb_to_csv(wb, ws)

    my_new_list = []
    for my_row in my_csv:
        my_row.insert(0, '')
        my_new_list.append(my_row)

    push_list_to_csv(my_new_list, 'csv_subscriptions.csv')
    load_infile('subscriptions', 'csv_subscriptions.csv')

    #
    # Import Bookings
    #
    wb, ws = open_wb(app_cfg['XLS_BOOKINGS'])
    my_csv = xlrd_wb_to_csv(wb, ws)

    my_new_list = []
    last_col = len(my_csv[0])

    for my_row in my_csv:
        # Add some useful columns
        my_row.insert(0, '')
        my_row.insert(last_col+1, 'hash')
        my_row.insert(last_col+2, now)

        my_new_list.append(my_row)

    push_list_to_csv(my_new_list, 'csv_bookings.csv')
    load_infile('bookings', 'csv_bookings.csv')

    return


if __name__ == "__main__" and __package__ is None:
    import_updates_to_sql()