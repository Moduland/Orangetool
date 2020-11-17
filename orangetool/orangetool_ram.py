# -*- coding: utf-8 -*-
"""Orangetool RAM functions."""
import psutil


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


def ram_total(convert=True):
    """
    Return total ram of board.

    :param convert: flag for convert mode (using of convert_byte function)
    :type convert:bool
    :return: total ram of board as string
    """
    response = list(psutil.virtual_memory())
    if convert:
        return convert_bytes(int(response[0]))
    return str(response[0])


def ram_used(convert=True):
    """
    Return how much ram is using.

    :param convert: flag for convert mode (using of convert_byte function)
    :type convert:bool
    :return: how much ram is using as string
    """
    response = list(psutil.virtual_memory())
    if convert:
        return convert_bytes(int(response[3]))
    return str(response[3])


def ram_free(convert=True):
    """
    Return how much ram is available.

    :param convert: flag for convert mode (using of convert_byte function)
    :type convert : bool
    :return: how much ram is available
    """
    response = list(psutil.virtual_memory())
    if convert:
        return convert_bytes(int(response[1]))
    return str(response[1])


def ram_percent():
    """
    Return available ram percentage.

    :return: availabe ram percentage as string with %
    """
    response = list(psutil.virtual_memory())
    return str(response[2]) + " %"


def freeup(debug=False):
    """
    To free pagecache, dentries and inodes.

    :param debug: flag for using debug mode
    :type debug:bool
    :return: Amount of freeuped ram as string and converted by convert_bytes()
    """
    try:
        RAM_before = int(ram_free(convert=False))
        caches_control = open("/proc/sys/vm/drop_caches", "w")
        caches_control.write("3")
        caches_control.close()
        RAM_after = int(ram_free(convert=False))
        freeuped_ram = RAM_after - RAM_before
        if freeuped_ram > 0:
            return convert_bytes(freeuped_ram)
        return convert_bytes(0)
    except Exception as e:
        if debug:
            print(str(e))
        return "Error"
