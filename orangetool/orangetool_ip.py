# -*- coding: utf-8 -*-
"""Orangetool IP functions."""
from .orangetool_system import restart as restart_func
import subprocess as sub
import socket
import os
import requests
import re
import platform
ip_pattern = r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
api_1 = "http://ipinfo.io/ip"


def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Check internet connections.

    :param  host: the host that check connection to
    :param  port: port that check connection with
    :param  timeout: times that check the connection
    :type host:str
    :type port:int
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


def local_ip(DEBUG=False):
    """
    Return local ip of computer in windows by socket module and in unix with hostname command in shell.

    :param DEBUG:flag for using Debug Mode
    :type DEBUG:bool
    :return: local ip as string
    """
    try:
        ip = socket.gethostbyname(socket.gethostname())
        if ip != "127.0.0.1":
            return ip
        elif platform.system() != "Windows":
            command = sub.Popen(["hostname",
                                 "-I"],
                                stdout=sub.PIPE,
                                stderr=sub.PIPE,
                                stdin=sub.PIPE,
                                shell=False)
            response = list(command.communicate())
            if len(response[0]) > 0:
                return str(response[0])[2:-4]
            return "Error"
        return "Error"

    except Exception as e:
        if DEBUG:
            print(str(e))
        return "Error"


def global_ip(DEBUG=False):
    """
    Return ip with by http://ipinfo.io/ip api.

    :param DEBUG:flag for using Debug mode
    :type DEBUG:bool
    :return: global ip as string
    """
    try:
        new_session = requests.session()
        response = new_session.get(api_1)
        ip_list = re.findall(ip_pattern, response.text)
        new_session.close()
        return ip_list[0]
    except Exception as e:
        if DEBUG:
            print(str(e))
        return "Error"


def set_ip(ip, restart=False, device="eth0", DEBUG=False):
    """
    Set static ip in interfaces file (need sudo).

    :param restart : restart flag
    :type restart : bool
    :param device: network device name
    :type device:str
    :param ip: static ip
    :type ip :str
    :param DEBUG: flag for using Debug mode
    :type DEBUG:bool
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
        if bool(re.match(ip_pattern, ip)) == False or ip.find(
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
        if DEBUG:
            print(str(e))
        return "Error"


def ping(ip, packet_number=3, DEBUG=False):
    """
    Ping ip and return True if this ip is available and False otherwise.

    :param ip: target ip
    :param packet_number: number of packet to size
    :param DEBUG: flag for using Debug mode
    :type ip :str
    :type packet_number:int
    :type DEBUG:bool
    :return: a boolean value (True if ip is available and False otherwise)
    """
    try:
        if re.match(ip_pattern, ip) == False:
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
        if DEBUG:
            print(str(e))
        return "Error"


def mac(DEBUG=False):
    """
    Return mac addresses of net devices.

    :param DEBUG: flag for using Debug mode
    :type DEBUG:bool
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
        if DEBUG:
            print(str(e))
        return "Error"
