#!/usr/bin/python3

import sys
import timeit
from config import cfg
from icecream import ic
from Parser import Parser
from Formatter import Formatter


class Error(Exception):
    """Base class for other exceptions"""
    pass


class ToFewArguments(Error):
    """Raised when the input value is too small"""

    def __init__(self, message="Not enough args, all arguments are required"):
        self.message = message
        super().__init__(self.message)


class ToManyArguments(Error):
    def __init__(self, message="To many args, required only 'url, number, width, save_links, show_time'"):
        self.message = message
        super().__init__(self.message)


sys.argv.pop(0)
sys.argv.pop(0)
params = sys.argv
cof_params = len(params)

if cof_params < 5:
    raise ToFewArguments
elif cof_params > 5:
    raise ToManyArguments

url, number, width, save_links, show_time = params

if show_time == 'true':
    start_time = timeit.default_timer()

parser = Parser(url, number, width, save_links)
parsed_data = parser.parse()

formatter = Formatter(parsed_data, width)
formatter.get_pure_text()
formatter.write_to_file(cfg.DATA_FILE_PATH)

if show_time == 'true':
    print('Затраченное время в секундах: ')
    ic(timeit.default_timer() - start_time)

# Результат - файл в директории /data/data.txt
