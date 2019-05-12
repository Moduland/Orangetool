# -*- coding: utf-8 -*-
"""Orangetool display functions."""


def hdmi_controller(command, DEBUG=False):
    """
    Control hdmi port.

    :param command: inpurt command
    :type command: bool
    :param DEBUG: flag for using Debug mode
    :type DEBUG: bool
    :return: bool
    """
    try:
        hdmi_control = open("/sys/class/graphics/fb0/blank", "w")
        if command:
            hdmi_control.write("0")
        else:
            hdmi_control.write("4")
        hdmi_control.close()
        return True
    except Exception as e:
        if DEBUG:
            print(str(e))
        return "Error"


def hdmi_on(DEBUG=False):
    """
    Turn on hdmi port (need sudo -s).

    :param DEBUG: flag for using Debug mode
    :type DEBUG:bool
    :return: bool
    """
    hdmi_controller(True, DEBUG)


def hdmi_off(DEBUG=False):
    """
    Turn off hdmi port (need sudo -s).

    :param DEBUG: flag for using Debug mode
    :type DEBUG:bool
    :return: bool
    """
    hdmi_controller(False, DEBUG)


def hdmi_size(v=None, h=None, DEBUG=False):
    """
    Change hdmi display resolution (need sudo -s) (if call without any argument return current resolution).

    :param v: vertical line
    :param h: horizental line
    :param DEBUG: flag for using Debug mode
    :type v : int
    :type h:int
    :type DEBUG:bool
    :return: bool
    """
    try:
        if (not isinstance(v, int)) or (not isinstance(h, int)):
            hdmi_control = open("/sys/class/graphics/fb0/virtual_size", "r")
            resolution = hdmi_control.read()[:-1].replace(",", "x")
            hdmi_control.close()
            return resolution
        hdmi_control = open("/sys/class/graphics/fb0/virtual_size", "w")
        hdmi_control.write(str(v) + "," + str(h))
        hdmi_control.close()
        return True
    except Exception as e:
        if DEBUG:
            print(str(e))
        return "Error"
