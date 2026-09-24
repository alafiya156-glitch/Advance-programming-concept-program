# date_module.py

import datetime


def current_date():
    return datetime.date.today()


def current_time():
    return datetime.datetime.now().time()