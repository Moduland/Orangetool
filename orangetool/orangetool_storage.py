import subprocess as sub
import os
import string
import random

def mount_status(device_name,DEBUG=False):
    '''
    This function return addresses of mounted memory devices in dev by device name
    :param DEBUG: Flag for using Debug mode
    :type DEBUG:bool
    :return: list of memory devices
    '''
    try:
        file = open("/proc/mounts")
        output=file.readlines()
        memory_list=[]
        for item in output:
            temp=item.split(" ")
            if temp[0].find(device_name)!=-1:
                memory_list.append(temp[1])
        if len(memory_list)==0:
            return "u"
        else:
            return memory_list
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"

def storage_status(DEBUG=False):
    '''
    This function return all of the inserted memory and their status
    :param DEBUG: Flag for using Debug mode
    :type DEBUG:bool
    :return: All of the inserted memory and their status as dictionary ( device name as keys and mount status (mounted_addresses as list and u --> unmounted) as values
    '''
    try:
        folder_items=os.listdir("/dev/")
        memory_items=[]
        memory_status=[]
        for i in string.ascii_lowercase:
            if "sd"+i+"1" in folder_items:
                memory_items.append("sd"+i+"1")
        for item in memory_items:
            memory_status.append(mount_status(item))
        return dict(zip(memory_items,memory_status))
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"

def unmount(ADDRESS,DEBUG=False):
    '''
    This function unmount memory devices by addresses
    :param ADDRESS: address of that device mount on
    :type ADDRESS:str
    :param DEBUG: Flag for using Debug mode
    :type DEBUG:bool
    :return: True if device unmount correctly and False other wise
    '''
    try:
        command = sub.Popen(["umount",ADDRESS], stdout=sub.PIPE, stderr=sub.PIPE)
        output=list(command.communicate())
        if len(output[0])==0 and len(output[1])==0:
            return True
        else:
            return False
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"

def unmount_all(DEBUG=False):
    '''
    This function unmount all of the mounted devices
    :param DEBUG: Flag for using Debug mode
    :type DEBUG:bool
    :return: return True if all of the mounted devices unmount correctly
    '''
    try:
        storage_output=storage_status()
        storage_keys=list(storage_output.keys())
        storage_values=list(storage_output.values())
        for i,item in enumerate(storage_values):
            if storage_values[i]!="u":
                print(item)
                for j in item:
                    unmount(j)
        return True
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"
def random_generator(number):
    response=""
    i=0
    while(i<number):
        i+=1
        response+=str(random.randint(0,10))
    return response
def mount(device_name,mount_address=None,DEBUG=False):
    '''
    :param device_name: name of device for mounted example = sda1
    :param mount_address: address for mounting device example = /mnt/usb , default value is None in this case function generate random number for mount folder name
    :param DEBUG: Flag for using Debug mode
    :type device_name:str
    :type mount_address:str
    :type DEBUG:bool
    :return: True if device mount correctly and False other wise
    '''
    try:
        if mount_status(device_name)!="u":
            raise Exception("Device already mount")
        if mount_address==None:
            mount_address="/mnt/"+random_generator(5)
            command=sub.Popen(["mkdir",mount_address], stdout=sub.PIPE, stderr=sub.PIPE)
        command = sub.Popen(["mount","/dev/"+device_name,mount_address], stdout=sub.PIPE, stderr=sub.PIPE)
        output=list(command.communicate())
        if len(output[0])==0 and len(output[1])==0:
            return True
        else:
            return False
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"



























