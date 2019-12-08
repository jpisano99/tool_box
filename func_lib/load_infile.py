import os
from my_app import db
from my_app.settings import app_cfg


def load_infile(table_name, csv_input, run_dir=app_cfg['UPDATES_SUB_DIR']):
    path_to_my_app = os.path.join(app_cfg['HOME'], app_cfg['MOUNT_POINT'], app_cfg['MY_APP_DIR'])
    path_to_run_dir = (os.path.join(path_to_my_app, run_dir))
    path_to_file = os.path.join(path_to_run_dir, csv_input)
    print()
    print('LOADING A LOCAL CSV FILE IN DIRECTORY >>>>>>>>>> ', path_to_run_dir)
    print('LOADING CSV FILE >>>>>>>>>> ', csv_input)
    print()

    # We need to change the path separator for load data local infile to work
    path_to_file = path_to_file.replace("\\", '/')

    sql = "load data local infile '" + path_to_file +\
          "' into table " + table_name +\
          " fields terminated by ','" +\
          " enclosed by '\"'" +\
          " escaped by ''" +\
          " lines terminated by '\\r\\n'"
    print('Executed:', sql)
    db.engine.execute(sql)

    sql = 'SELECT COUNT(*) FROM ' + table_name + ';'
    sql_results = db.engine.execute(sql).fetchall()
    print("Loaded:", sql_results[0][0], ' rows')


if __name__ == "__main__" and __package__ is None:
    load_infile('bookings', "my_csv.csv")