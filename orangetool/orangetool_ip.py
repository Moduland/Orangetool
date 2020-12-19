# -*- coding: utf-8 -*-
"""Orangetool IP functions."""
from .orangetool_system import restart as restart_func
from .orangetool_params import IP_PATTERN, GLOBAL_IP_API_1, GENERAL_ERROR_MESSAGE
import subprocess as sub
import socket
import os
import requests
import re
import platform


def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Check internet connections.

    :param  host: the host that check connection to
    :type host:str
    :param  port: port that check connection with
    :type port:int
    :param  timeout: times that check the connection
    :type timeout:int
    :return bool: True if Connection is Stable
    >>> internet() # if there is stable internet connection
    True
    >>> internet() # if there is no stable internet connection
    False
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        print(str(ex))
        return False


def local_ip(debug=False):
    """
    Return local ip of computer in windows by socket module and in unix with hostname command in shell.

    :param debug:flag for using debug Mode
    :type debug:bool
    :return: local ip as string
    """
    try:
        ip = socket.gethostbyname(socket.gethostname())
        if ip != "127.0.0.1":
            return ip
        if platform.system() != "Windows":
            command = sub.Popen(["hostname",
                                 "-I"],
                                stdout=sub.PIPE,
                                stderr=sub.PIPE,
                                stdin=sub.PIPE,
                                shell=False)
            response = list(command.communicate())
            if len(response[0]) > 0:
                return str(response[0])[2:-4]
            return GENERAL_ERROR_MESSAGE
        return GENERAL_ERROR_MESSAGE

    except Exception as e:
        if debug:
            print(str(e))
        return GENERAL_ERROR_MESSAGE


def global_ip(debug=False):
    """
    Return ip with by http://ipinfo.io/ip api.

    :param debug:flag for using debug mode
    :type debug:bool
    :return: global ip as string
    """
    try:
        new_session = requests.session()
        response = new_session.get(GLOBAL_IP_API_1)
        ip_list = re.findall(IP_PATTERN, response.text)
        new_session.close()
        return ip_list[0]
    except Exception as e:
        if debug:
            print(str(e))
        return GENERAL_ERROR_MESSAGE


def set_ip(ip, restart=False, device="eth0", debug=False):
    """
    Set static ip in interfaces file (need sudo).

    :param ip: static ip
    :type ip :str
    :param restart : restart flag
    :type restart : bool
    :param device: network device name
    :type device:str
    :param debug: flag for using debug mode
    :type debug:bool
    :return: True in successful
    """
    static_string = '''
    auto lo device
iface lo inet loopback
iface device inet static
        address ip
        netmask 255.255.255.0
        gateway 192.168.1.1
        dns-nameservers 8.8.8.8 8.8.4.4
    '''
    try:
        if not bool(re.match(IP_PATTERN, ip)) or ip.find(
                "192.168.") == -1 or device not in mac().keys():
            raise Exception("IP Formation Error")
        static_string = static_string.replace("ip", ip)
        static_string = static_string.replace("device", device)
        file = open("/etc/network/interfaces", "w")
        file.write(static_string)
        file.close()
        sub.Popen(["ifdown", device, "&&", "ifup", device],
                  stderr=sub.PIPE, stdin=sub.PIPE, stdout=sub.PIPE)
        if restart:
            restart_func()
        return True
    except Exception as e:
        if debug:
            print(str(e))
        return GENERAL_ERROR_MESSAGE


def ping(ip, packet_number=3, debug=False):
    """
    Ping ip and return True if this ip is available and False otherwise.

    :param ip: target ip
    :type ip :str
    :param packet_number: number of packet to size
    :type packet_number:int
    :param debug: flag for using debug mode
    :type debug:bool
    :return: a boolean value (True if ip is available and False otherwise)
    """
    try:
        if not re.match(IP_PATTERN, ip):
            raise Exception("IP Formation Error")
        output = str(list(sub.Popen(["ping",
                                     ip,
                                     "-c",
                                     str(packet_number)],
                                    stdout=sub.PIPE,
                                    stderr=sub.PIPE).communicate())[0])
        if output.find("Unreachable") == -1:
            return True
        return False
    except Exception as e:
        if debug:
            print(str(e))
        return GENERAL_ERROR_MESSAGE


def mac(debug=False):
    """
    Return mac addresses of net devices.

    :param debug: flag for using debug mode
    :type debug:bool
    :return: return mac addresses as dict with name as keys and mac addresses as values
    """
    try:
        net_dir = "/sys/class/net"
        mac_list = []
        dir_list = os.listdir(net_dir)
        for item in dir_list:
            mac_addr = open(net_dir + "/" + item + "/address", "r")
            mac_list.append(mac_addr.read()[:-1])
            mac_addr.close()
        return dict(zip(dir_list, mac_list))
    except Exception as e:
        if debug:
            print(str(e))
        return GENERAL_ERROR_MESSAGE
