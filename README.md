<div align="center">
<img src="http://moduland.github.io/Orangetool/images/orangetool.jpg" height=240px width=320px>

</br>
<a href="https://scrutinizer-ci.com/g/Moduland/Orangetool/?branch=master"><img src="https://scrutinizer-ci.com/g/Moduland/Orangetool/badges/quality-score.png?b=master"></a>
<a href="https://scrutinizer-ci.com/g/Moduland/Orangetool/build-status/master"><img src="https://scrutinizer-ci.com/g/Moduland/Orangetool/badges/build.png?b=master"></a>
<a href="http://www.python.org"><img src="https://img.shields.io/badge/python-3.3%2C3.4%2C3.5%2C3.6-blue.svg"></a>
<a href="https://badge.fury.io/py/orangetool"><img src="https://badge.fury.io/py/orangetool.svg"></a>
<a href="http://moduland.github.io/Orangetool/doc"><img src="https://img.shields.io/badge/doc-latest-orange.svg"></a>

</div>

----------


# Orangetool
	
Consist of some general and useful scripts that developed for Single-Board Computers (Under Development)					

Tested on Lubuntu 14.04 - Orange Pi-PC

----------
	
By [Moduland Co](http://www.moduland.ir)		

----------

- [IP Functions](#ip-functions)
- [RAM Functions](#ram-functions)
- [Storage Functions](#storage-functions)	
- [Display Functions](#display-functions)
- [System Functions](#system-functions)		
- [Other Functions](#other-functions)
</hr>
</hr>

## Download ##

- [Download](https://github.com/Moduland/Orangetool/archive/master.zip) source from github

## IP Functions

```python
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



```

## RAM Functions		

```python
 
#6- total ram

ram=orangetool.ram_total() #this function return total ram of the board

#7- free ram

ram=orangetool.ram_free() # this function return how much ram is available in the board

#8- ram percentage

ram=orangetool.ram_percent() # this function return used ram percentage

#9- freeup

orangetool.freeup() # To free pagecache, dentries and inodes and return freeuped amount

```

## Storage Functions				

```python
#10- mount_status

mount_details=orangetool.mount_status("sda1") # This function return mount addresses of input device

#11- storage_status

mount_details=orangetool.storage_status() # This function return all of the inserted storage and their status

#12- unmount

orangetool.unmount("/mnt/usb1") # This function unmount input device

#13- unmount_all


orangetool.unmount_all() #This function unmount all of the mounted devices

#14- mount

orangetool.mount("sda1","/mnt/usb1") # This function mount input device in input addresses

```

## Display Functions				

```python
#15- hdmi_on

orangetool.hdmi_on() # turn on hdmi port

#16- hdmi_off

orangetool.hdmi_off() # turn off hdmi port

#17- hdmi_size

orangetool.hdmi_size(1280,720) # this function change hdmi display resolution

```

## System Functions				

```python
#18- sleep

orangetool.sleep() # put system in sleep mode

#19- wakeup

orangetool.wakeup(day=1,hour=0,minute=1) # set rtc wakeuptime

```

## Other Functions			

```python

#20- get_temp

temp=orangetool.get_temp() # this function return cpu temperature as string

#21- uptime

time=orangetool.uptime() # this function return uptime of system

#22- idletime

time=orangetool.idletime() # this function return idle of system ( all cores)

#23- mac

mac_dic=orangetool.mac() # return dict of all system net devices mac addresses

#24- version

orangetool.version() # return orangetool version for test

```



- All of the functions in error state return `Error` String
- local_ip() and global_ip() originally are available in ipz package [Link](http://github.com/sepandhaghighi/ipz)
- RAM Functions in this version need psutil package
- Some of this funtions need root access so it's better to run ```sudo -s``` before use this tool



## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!							
or send an email to [info@moduland.ir](mailto:info@moduland.ir "info@moduland.ir"). 


## Contribution			

You can fork the repository, improve or fix some part of it and then send the pull requests back if you want to see them here. I really appreciate that. ❤️			

Remember to write a few tests for your code before sending pull requests. 


##License

<a href="https://github.com/Moduland/orangetool/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mashape/apistatus.svg"/></a>
			

