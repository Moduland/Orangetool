# -*- coding: utf-8 -*-
"""Orangetool utils."""
import random

def zero_insert(input_string):
    """
    Get a string as input if input is one digit add a zero.

    :param input_string: input digit az string
    :type input_string:str
    :return: modified output as str
    """
    if len(input_string) == 1:
        return "0" + input_string
    return input_string


def time_convert(input_string):
    """
    Convert input_string from sec to DD,HH,MM,SS Format.

    :param input_string: input time string  in sec
    :type input_string:str
    :return: converted time as string
    """
    input_sec = float(input_string)
    input_minute = input_sec // 60
    input_sec = int(input_sec - input_minute * 60)
    input_hour = input_minute // 60
    input_minute = int(input_minute - input_hour * 60)
    input_day = int(input_hour // 24)
    input_hour = int(input_hour - input_day * 24)
    return zero_insert(str(input_day)) + " days, " + zero_insert(str(input_hour)) + " hour, " + \
        zero_insert(str(input_minute)) + " minutes, " + zero_insert(str(input_sec)) + " seconds"


def random_generator(number):
    """
    Generate random number.

    :param number: random number digits
    :type number: int
    :return: random number as str
    """
    response = ""
    i = 0
    while(i < number):
        i += 1
        response += str(random.randint(0, 9))
    return response

def convert_bytes(num):
    """
    Convert num to idiomatic byte unit.

    :param num: the input number.
    :type num:int
    :return: str
    >>> convert_bytes(200)
    '200.0 bytes'
    >>> convert_bytes(6000)
    '5.9 KB'
    >>> convert_bytes(80000)
    '78.1 KB'
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
