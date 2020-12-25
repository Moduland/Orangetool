# -*- coding: utf-8 -*-
"""Orangetool system functions."""
import subprocess as sub
from .orangetool_params import ORANGETOOL_VERSION, UPDATE_URL, GENERAL_ERROR_MESSAGE, ROOT_ERROR_MESSAGE
from .orangetool_utils import time_convert
import time
import requests
from art import tprint


def check_update(debug=False):
    """
    Check orangetool site for new version.

    :param debug: flag for using debug mode
    :type debug:bool
    :return: True if new version is available
    """
    try:
        new_version = requests.get(UPDATE_URL).text
        if float(new_version) > float(ORANGETOOL_VERSION):
            print("New Version (" + new_version + ") Of Orangetool Is Available")
            return True
        print("Update!")
        return False
    except Exception as e:
        if debug:
            print(str(e))
        return GENERAL_ERROR_MESSAGE


def get_temp(zone=0, debug=False):
    """
    Read cpu temperature.

    :param zone : thermal zone index
    :type zone:int
    :param debug : flag for using debug mode
    :type debug:bool
    :return: board temp as string in celsius
    """
    try:
        command = open("/sys/class/thermal/thermal_zone" + str(zone) + "/temp")
        # command=sub.Popen(["cat","/sys/class/thermal/thermal_zone"+str(zone)+"/temp"],stderr=sub.PIPE,stdin=sub.PIPE,stdout=sub.PIPE)
        # response=list(command.communicate())
        response = command.read()
        return response[:-1]
        # if len(response[0])!=0:
        # return str(response[0])[2:-3]
        # else:
        # return GENERAL_ERROR_MESSAGE
    except Exception as e:
        if debug:
            print(str(e))
        return GENERAL_ERROR_MESSAGE

def time_control(mode="uptime",debug=False):
    """
    Return system time.

    :param mode: time mode (uptime / idle)
    :type mode: str
    :param debug: flag for using debug mode
    :type debug:bool
    :return: system time as string
    """
    index = 0
    if mode  in ["idle","idletime"]:
        index = 1
    try:
        command = open("/proc/uptime")
        response = command.read()
        return time_convert(response[:-1].split(" ")[index])
    except Exception as e:
        if debug:
            print(str(e))
        return GENERAL_ERROR_MESSAGE

def uptime(debug=False):
    """
    Return system uptime.

    :param debug: flag for using debug mode
    :type debug:bool
    :return: system uptime as string
    """
    return time_control(mode="uptime",debug=debug)


def idletime(debug=False):
    """
    Return system idletime.

    :param debug: flag for using debug mode
    :type debug:bool
    :return: system idle as string
    """
    return time_control(mode="idle", debug=debug)


def version():
    """
    Return orangetool version.

    :return: return orangetool-version number as string
    """
    tprint("orangetool", font="bulbhead")
    tprint("v" + ORANGETOOL_VERSION, font="bulbhead")


def wakeup(day=0, hour=0, minute=0, debug=False):
    """
    Set wakeup time for kernel RTC (need sudo).

    :param day: days for wakeup
    :type day:int
    :param hour: hour for wakeup
    :type hour:int
    :param minute: minute for wakeup
    :type minute:int
    :param debug: flag for using debug mode
    :type debug:bool
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
        if debug:
            print(str(e))
        return GENERAL_ERROR_MESSAGE


def power_control(command, debug=False):
    """
    Control different power options.

    :param command: input command
    :type command: str
    :param debug: flag for using debug mode
    :type debug: bool
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
            raise Exception(ROOT_ERROR_MESSAGE)
    except Exception as e:
        if debug:
            print(str(e))
        return GENERAL_ERROR_MESSAGE


def sleep(debug=False):
    """
    Shortcut for sleep command (need sudo).

    :param debug: flag for using debug mode
    :type debug:bool
    :return: None
    """
    power_control("pm-suspend", debug)


def hibernate(debug=False):
    """
    Shortcut for hibernate command (need sudo).

    :param debug: flag for using debug mode
    :type debug:bool
    :return: None
    """
    power_control("pm-hibernate", debug)


def halt(debug=False):
    """
    Shortcut for poweroff (need sudo).

    :param debug: flag for using debug mode
    :type debug:bool
    :return: None
    """
    power_control("poweroff", debug)


def restart(debug=False):
    """
    Shortcut for reboot (need sudo).

    :param debug: flag for using debug mode
    :type debug:bool
    :return: None
    """
    power_control("reboot", debug)
