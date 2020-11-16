# -*- coding: utf-8 -*-
"""Orangetool display functions."""


def hdmi_controller(command, debug=False):
    """
    Control hdmi port.

    :param command: inpurt command
    :type command: bool
    :param debug: flag for using Debug mode
    :type debug: bool
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
        if debug:
            print(str(e))
        return "Error"


def hdmi_on(debug=False):
    """
    Turn on hdmi port (need sudo -s).

    :param debug: flag for using Debug mode
    :type debug:bool
    :return: bool
    """
    hdmi_controller(True, debug)


def hdmi_off(debug=False):
    """
    Turn off hdmi port (need sudo -s).

    :param debug: flag for using Debug mode
    :type debug:bool
    :return: bool
    """
    hdmi_controller(False, debug)


def hdmi_size(v=None, h=None, debug=False):
    """
    Change hdmi display resolution (need sudo -s) (if call without any argument return current resolution).

    :param v: vertical line
    :param h: horizental line
    :param debug: flag for using Debug mode
    :type v : int
    :type h:int
    :type debug:bool
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
        if debug:
            print(str(e))
        return "Error"
