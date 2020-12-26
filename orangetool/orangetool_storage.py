# -*- coding: utf-8 -*-
"""Orangetool storage functions."""
import subprocess as sub
import os
import string
from .orangetool_params import GENERAL_ERROR_MESSAGE, ROOT_ERROR_MESSAGE
from .orangetool_utils import random_generator


def mount_status(device_name, debug=False):
    """
    Return addresses of mounted memory devices in dev by device name.

    :param device_name: name of device
    :type device_name: str
    :param debug: flag for using debug mode
    :type debug:bool
    :return: list of memory devices
    """
    try:
        file = open("/proc/mounts")
        output = file.readlines()
        memory_list = []
        for item in output:
            temp = item.split(" ")
            if temp[0].find(device_name) != -1:
                memory_list.append(temp[1])
        if len(memory_list) == 0:
            return "u"
        return memory_list
    except Exception as e:
        if debug:
            print(str(e))
        return GENERAL_ERROR_MESSAGE


def storage_status(debug=False):
    """
    Return all of the inserted memory and their status.

    :param debug: flag for using debug mode
    :type debug:bool
    :return: all of the inserted memory and their status as dictionary ( device name as keys and mount status (mounted_addresses as list and u --> unmounted) as values
    """
    try:
        folder_items = os.listdir("/dev/")
        memory_items = []
        memory_status = []
        for i in string.ascii_lowercase:
            if "sd" + i + "1" in folder_items:
                memory_items.append("sd" + i + "1")
        for item in memory_items:
            memory_status.append(mount_status(item))
        return dict(zip(memory_items, memory_status))
    except Exception as e:
        if debug:
            print(str(e))
        return GENERAL_ERROR_MESSAGE


def unmount(address, debug=False):
    """
    Unmount memory devices by addresses.

    :param address: address of that device mount on
    :type address:str
    :param debug: flag for using debug mode
    :type debug:bool
    :return: True if device unmount correctly and False other wise
    """
    try:
        command = sub.Popen(["umount", address],
                            stdout=sub.PIPE, stderr=sub.PIPE)
        output = list(command.communicate())
        if len(output[0]) == 0 and len(output[1]) == 0:
            return True
        return False
    except Exception as e:
        if debug:
            print(str(e))
        return GENERAL_ERROR_MESSAGE


def unmount_all(debug=False):
    """
    Unmount all of the mounted devices.

    :param debug: flag for using debug mode
    :type debug:bool
    :return: return True if all of the mounted devices unmount correctly
    """
    try:
        storage_output = storage_status()
        storage_keys = list(storage_output.keys())
        storage_values = list(storage_output.values())
        for i, item in enumerate(storage_values):
            if storage_values[i] != "u":
                print(item)
                for j in item:
                    unmount(j)
        return True
    except Exception as e:
        if debug:
            print(str(e))
        return GENERAL_ERROR_MESSAGE

def mount(device_name, mount_address=None, debug=False):
    """
    Mount memory devices by addresses.

    :param device_name: name of device for mounted example = sda1
    :type device_name:str
    :param mount_address: address for mounting device example = /mnt/usb , default value is None in this case function generate random number for mount folder name
    :type mount_address:str
    :param debug: flag for using debug mode
    :type debug:bool
    :return: True if device mount correctly and False other wise
    """
    try:
        if mount_status(device_name) != "u":
            raise Exception("Device already mount")
        if mount_address is None:
            mount_address = "/mnt/" + random_generator(5)
            command = sub.Popen(["mkdir", mount_address],
                                stdout=sub.PIPE, stderr=sub.PIPE)
        command = sub.Popen(["mount",
                             "/dev/" + device_name,
                             mount_address],
                            stdout=sub.PIPE,
                            stderr=sub.PIPE)
        output = list(command.communicate())
        if len(output[0]) == 0 and len(output[1]) == 0:
            return True
        return False
    except Exception as e:
        if debug:
            print(str(e))
        return GENERAL_ERROR_MESSAGE


def usb_control(code, debug=False):
    """
    Control different usb options.

    :param code: permission code
    :type code: str
    :param debug: flag for using debug mode
    :type debug: bool
    :return: None
    """
    try:
        command = sub.Popen(
            ["chmod", "-R", code, "/media/"],
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


def usb_on(debug=False):
    """
    Shortcut for enable usb (need sudo).

    :param debug: flag for using debug mode
    :type debug:bool
    :return: None
    """
    usb_control("777", debug)


def usb_off(debug=False):
    """
    Shortcut for disable usb (need sudo).

    :param debug: flag for using debug mode
    :type debug:bool
    :return: None
    """
    usb_control("000", debug)
