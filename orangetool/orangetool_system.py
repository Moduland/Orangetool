import subprocess as sub
import time
import requests
logo='''
________                                      __                .__
\_____  \____________    ____    ____   _____/  |_  ____   ____ |  |
 /   |   \_  __ \__  \  /    \  / ___\_/ __ \   __\/  _ \ /  _ \|  |
/    |    \  | \// __ \|   |  \/ /_/  >  ___/|  | (  <_> |  <_> )  |__
\_______  /__|  (____  /___|  /\___  / \___  >__|  \____/ \____/|____/
        \/           \/     \//_____/      \/
'''
ip_pattern=r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
api_1="http://ipinfo.io/ip"
VERSION="0.23"
UPDATE_URL="http://www.orangetool.ir/version"
def check_update(DEBUG=False):
    '''
    This function check orangetool site for newversion
    :param DEBUG: Flag for using Debug mode
    :type DEBUG:bool
    :return: True if new version is available
    '''
    try:
        new_version=requests.get(UPDATE_URL).text
        if float(new_version)>float(VERSION):
            print("New Version ("+new_version+") Of Orangetool Is Available")
            return True
        else:
            print("Update!")
            return False
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
        command=open("/sys/class/thermal/thermal_zone"+str(Zone)+"/temp")
        #command=sub.Popen(["cat","/sys/class/thermal/thermal_zone"+str(Zone)+"/temp"],stderr=sub.PIPE,stdin=sub.PIPE,stdout=sub.PIPE)
        #response=list(command.communicate())
        response=command.read()
        return response[:-1]
        #if len(response[0])!=0:
            #return str(response[0])[2:-3]
        #else:
            #return "Error"
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"

def zero_insert(input_string):
    '''
    This function get a string as input if input is one digit add a zero
    :param input_string: input digit az string
    :type input_string:str
    :return: modified output as str
    '''
    if len(input_string)==1:
        return "0"+input_string
    return input_string

def time_convert(input_string):
    '''
    This function convert input_string from uptime from sec to DD,HH,MM,SS Format
    :param input_string: input time string  in sec
    :type input_string:str
    :return: converted time as string
    '''
    input_sec=float(input_string)
    input_minute=input_sec//60
    input_sec=int(input_sec-input_minute*60)
    input_hour=input_minute//60
    input_minute=int(input_minute-input_hour*60)
    input_day=int(input_hour//24)
    input_hour=int(input_hour-input_day*24)
    return zero_insert(str(input_day))+" days, "+zero_insert(str(input_hour))+" hour, "+zero_insert(str(input_minute))+" minutes, "+zero_insert(str(input_sec))+" seconds"

def uptime(DEBUG=False):
    '''
    This function return system uptime
    :param DEBUG: Flag for using Debug mode
    :type DEBUG:bool
    :return: system uptime as string
    '''
    try:
        command=open("/proc/uptime")
        response=command.read()
        return time_convert(response[:-1].split(" ")[0])
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"
def idletime(DEBUG=False):
    '''
    This function return system idletime
    :param DEBUG: Flag for using Debug mode
    :type DEBUG:bool
    :return: system idle as string
    '''
    try:
        command=open("/proc/uptime")
        response=command.read()
        return time_convert(response[:-1].split(" ")[1])
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"

def version():
    '''
    This function return orangetool version (for test)
    :return: return orangetool-version number as string
    '''
    print(logo)
    return "orangetool-v"+VERSION


def wakeup(day=0,hour=0,minute=0,DEBUG=False):
    '''
    This function set wakeup time for kernel RTC (need sudo)
    :param day: days for wakeup
    :param hour: hout for wakeup
    :param minute: minute for wakeup
    :param DEBUG: Flag for using Debug mode
    :type day:int
    :type hour:int
    :type minute:int
    :type DEBUG:bool
    :return: bool
    '''
    try:
        total_time=day*24*60+hour*60+minute
        epoch=time.time()+total_time*60
        file=open("/sys/class/rtc/rtc0/wakealarm","w")
        file.write("0")
        file.close()
        file = open("/sys/class/rtc/rtc0/wakealarm", "w")
        file.write(str(epoch))
        file.close()
        return True
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"
def sleep(DEBUG=False):
    '''
    This function is a shortcut for sleep (need sudo)
    :param DEBUG: Flag for using Debug mode
    :type DEBUG:bool
    :return: None
    '''
    try:
        command=sub.Popen("pm-suspend",stderr=sub.PIPE,stdout=sub.PIPE,stdin=sub.PIPE)
        response=list(command.communicate())
        if len(response[1])>0:
            raise Exception('Root Error')
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"

def halt(DEBUG=False):
    '''
    his function is a shortcut for poweroff (need sudo)
    :param DEBUG: Flag for using Debug mode
    :type DEBUG:bool
    :return: None
    '''
    try:
        command = sub.Popen("poweroff", stderr=sub.PIPE, stdout=sub.PIPE, stdin=sub.PIPE)
        response = list(command.communicate())
        if len(response[1]) > 0:
            raise Exception('Root Error')
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"

def restart(DEBUG=False):
    '''
        his function is a shortcut for reboot (need sudo)
        :param DEBUG: Flag for using Debug mode
        :type DEBUG:bool
        :return: None
        '''
    try:
        command = sub.Popen("reboot", stderr=sub.PIPE, stdout=sub.PIPE, stdin=sub.PIPE)
        response = list(command.communicate())
        if len(response[1]) > 0:
            raise Exception('Root Error')
    except Exception as e:
        if DEBUG == True:
            print(str(e))
        return "Error"





























