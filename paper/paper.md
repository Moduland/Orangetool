---
title: 'Orangetool: General And Useful Scripts For Single-Board Computers'
tags:
  - orangepi
  - script
  - single_board_computers
  - unix
  - library
authors:
 - name: Sepand Haghighi
   orcid: 0000-0001-9450-2375
   affiliation: 1
affiliations:
 - name: Moduland Co
   index: 1
date: 16 July 2017
---
						

# Summary

Orangetool is a python library that consist of some general and useful scripts , developed for single-board computers like raspberry pi , orange pi and ...
these scripts provides simple and fast way to control system in programming.

Website : www.orangetool.ir

```
import orangetool

#1- local_ip

local_ip=orangetool.local_ip() # this function return local ip of board as string

#2- global_ip

global_ip=orangetool.global_ip() # this function return global ip of board as string

#3- internet 

status=orangetool.internet() #this function check internet connection and return True if internet connection is stable

#4- ping

ip_status=orangetool.ping(ip_address) #this function check ip and return True if this ip is available in network and False otherwise

#5- set_ip

set_ip("192.168.1.46","eth0")  #this function set static ip for system

#6- mac

mac_dic=orangetool.mac() # return dict of all system net devices mac addresses



```

## RAM Functions		

```
 
#1- total ram

ram=orangetool.ram_total() #this function return total ram of the board

#2- free ram

ram=orangetool.ram_free() # this function return how much ram is available in the board

#3- ram percentage

ram=orangetool.ram_percent() # this function return used ram percentage

#4- used percentage

ram=orangetool.ram_used() # this function return used ram 

#5- freeup

orangetool.freeup() # To free pagecache, dentries and inodes and return freeuped amount

```

## Storage Functions				

```
#1- mount_status

mount_details=orangetool.mount_status("sda1") # This function return mount addresses of input device

#2- storage_status

mount_details=orangetool.storage_status() # This function return all of the inserted storage and their status

#3- unmount

orangetool.unmount("/mnt/usb1") # This function unmount input device

#4- unmount_all


orangetool.unmount_all() #This function unmount all of the mounted devices

#5- mount

orangetool.mount("sda1","/mnt/usb1") # This function mount input device in input addresses

```

## Display Functions				

```
#1- hdmi_on

orangetool.hdmi_on() # turn on hdmi port

#2- hdmi_off

orangetool.hdmi_off() # turn off hdmi port

#3- hdmi_size

orangetool.hdmi_size(1280,720) # this function change hdmi display resolution

```

## System Functions				

```
#1- sleep

orangetool.sleep() # put system in sleep mode

#2- halt

orangetool.halt() # poweroff system

#3- restart

orangetool.restart() # restart system

#4- wakeup

orangetool.wakeup(day=1,hour=0,minute=1) # set rtc wakeuptime

#5- get_temp

temp=orangetool.get_temp() # this function return cpu temperature as string

#6- uptime

time=orangetool.uptime() # this function return uptime of system

#7- idletime

time=orangetool.idletime() # this function return idle of system ( all cores)


#8- version

orangetool.version() # return orangetool version for test

#9- check_update

orangetool.check_update # Return True if new version is available

```


# References
