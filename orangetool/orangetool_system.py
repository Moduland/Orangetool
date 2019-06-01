# -*- coding: utf-8 -*-
"""Orangetool system functions."""
import subprocess as sub
import time
import requests
from art import tprint
ip_pattern = r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
api_1 = "http://ipinfo.io/ip"
VERSION = "0.35"
UPDATE_URL = "http://www.orangetool.ir/version"


def check_update(DEBUG=False):
    """
    Check orangetool site for new version.

    :param DEBUG: flag for using Debug mode
    :type DEBUG:bool
    :return: True if new version is available
    """
    try:
        new_version = requests.get(UPDATE_URL).text
        if float(new_version) > float(VERSION):
            print("New Version (" + new_version + ") Of Orangetool Is Available")
            return True
        print("Update!")
        return False
    except Exception as e:
        if DEBUG:
            print(str(e))
        return "Error"


def get_temp(Zone=0, DEBUG=False):
    """
    Read cpu temperature.

    :param DEBUG : flag for using Debug mode
    :param Zone : thermal Zone Index
    :type DEBUG:bool
    :type Zone:int
    :return: board temp as string in celsius
    """
    try:
        command = open("/sys/class/thermal/thermal_zone" + str(Zone) + "/temp")
        # command=sub.Popen(["cat","/sys/class/thermal/thermal_zone"+str(Zone)+"/temp"],stderr=sub.PIPE,stdin=sub.PIPE,stdout=sub.PIPE)
        # response=list(command.communicate())
        response = command.read()
        return response[:-1]
        # if len(response[0])!=0:
        # return str(response[0])[2:-3]
        # else:
        # return "Error"
    except Exception as e:
        if DEBUG:
            print(str(e))
        return "Error"


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
    Convert input_string from uptime from sec to DD,HH,MM,SS Format.

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


def uptime(DEBUG=False):
    """
    Return system uptime.

    :param DEBUG: flag for using Debug mode
    :type DEBUG:bool
    :return: system uptime as string
    """
    try:
        command = open("/proc/uptime")
        response = command.read()
        return time_convert(response[:-1].split(" ")[0])
    except Exception as e:
        if DEBUG:
            print(str(e))
        return "Error"


def idletime(DEBUG=False):
    """
    Return system idletime.

    :param DEBUG: flag for using Debug mode
    :type DEBUG:bool
    :return: system idle as string
    """
    try:
        command = open("/proc/uptime")
        response = command.read()
        return time_convert(response[:-1].split(" ")[1])
    except Exception as e:
        if DEBUG:
            print(str(e))
        return "Error"


def version():
    """
    Return orangetool version.

    :return: return orangetool-version number as string
    """
    tprint("orangetool", font="bulbhead")
    tprint("v"+VERSION,font="bulbhead")


def wakeup(day=0, hour=0, minute=0, DEBUG=False):
    """
    Set wakeup time for kernel RTC (need sudo).

    :param day: days for wakeup
    :param hour: hout for wakeup
    :param minute: minute for wakeup
    :param DEBUG: flag for using Debug mode
    :type day:int
    :type hour:int
    :type minute:int
    :type DEBUG:bool
    :return: bool
    """
    try:
        total_time = day * 24 * 60 + hour * 60 + minute
        epoch = time.time() + total_time * 60
        file = open("/sys/class/rtc/rtc0/wakealarm", "w")
        file.write("0")
        file.close()
        file = open("/sys/class/rtc/rtc0/wakealarm", "w")
        file.write(str(epoch))
        file.close()
        return True
    except Exception as e:
        if DEBUG:
            print(str(e))
        return "Error"


def power_control(command, DEBUG=False):
    """
    Control different power options.

    :param command: input command
    :type command: str
    :param DEBUG: flag for using Debug mode
    :type DEBUG: bool
    :return: None
    """
    try:
        command = sub.Popen(
            command,
            stderr=sub.PIPE,
            stdout=sub.PIPE,
            stdin=sub.PIPE)
        response = list(command.communicate())
        if len(response[1]) > 0:
            raise Exception('Root Error')
    except Exception as e:
        if DEBUG:
            print(str(e))
        return "Error"


def sleep(DEBUG=False):
    """
    Shortcut for sleep command (need sudo).

    :param DEBUG: flag for using Debug mode
    :type DEBUG:bool
    :return: None
    """
    power_control("pm-suspend", DEBUG)


def halt(DEBUG=False):
    """
    Shortcut for poweroff (need sudo).

    :param DEBUG: flag for using Debug mode
    :type DEBUG:bool
    :return: None
    """
    power_control("poweroff", DEBUG)


def restart(DEBUG=False):
    """
    Shortcut for reboot (need sudo).

    :param DEBUG: flag for using Debug mode
    :type DEBUG:bool
    :return: None
    """
    power_control("reboot", DEBUG)
