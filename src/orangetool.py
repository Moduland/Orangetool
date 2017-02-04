import subprocess as sub
import socket
import requests
import re
import platform
import psutil
ip_pattern=r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
api_1="http://ipinfo.io/ip"

def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Check Internet Connections.
    :param  host: the host that check connection to
    :param  port: port that check connection with
    :param  timeout: times that check the connnection
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
        error_log(str(ex))
        return False

def local_ip(DEBUG=False):
    '''
    return local ip of computer in windows by socket module and in unix with hostname command in shell
    :param DEBUG:Flag for using Debug Mode
    :type DEBUG:bool
    :return: local ip as string
    '''
    try:
        ip=socket.gethostbyname(socket.gethostname())
        if ip!="127.0.0.1":
            return ip
        elif platform.system()!="Windows":
            command=sub.Popen(["hostname","-I"],stdout=sub.PIPE,stderr=sub.PIPE,stdin=sub.PIPE,shell=False)
            response=list(command.communicate())
            if len(response[0])>0:
                return str(response[0])[2:-4]
            else:
                return "Error"
        else:
            return "Error"

    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"

def global_ip(DEBUG=False):
    '''
    return ip with by http://ipinfo.io/ip api
    :param DEBUG:Flag for using Debug mode
    :type DEBUG:bool
    :return: global ip as string
    '''
    try:
        new_session=requests.session()
        response=new_session.get(api_1)
        ip_list=re.findall(ip_pattern,response.text)
        new_session.close()
        return ip_list[0]
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"

def get_temp(Zone=0,DEBUG=False):
    '''
    This Function Wrote for Orangepi to read cpu temperature
    :param DEBUG : Flag for using Debug mode
    :param Zone : Thermal Zone Index
    :type DEBUG:bool
    :type Zone:int
    :return: Board Temp as string in celsius
    '''
    try:
        command=sub.Popen(["cat","/sys/class/thermal/thermal_zone"+str(Zone)+"/temp"],stderr=sub.PIPE,stdin=sub.PIPE,stdout=sub.PIPE)
        response=list(command.communicate())
        if len(response[0])!=0:
            return str(response[0])[2:-3]
        else:
            return "Error"
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"
def convert_bytes(num):
    """
    convert num to idiomatic byte unit
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
def ram_total():
    response=list(psutil.virtual_memory())
    return convert_bytes(response[0])
def ram_used():
    response=list(psutil.virtual_memory())
    return convert_bytes(response[3])
def ram_available():
    response=list(psutil.virtual_memory())
    return convert_bytes(response[1])
def ram_percent():
    response=list(psutil.virtual_memory())
    return convert_bytes(response[2])


