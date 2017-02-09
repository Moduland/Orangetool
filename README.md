![Logo](http://www.shaghighi.ir/findip/Files/orangetool.gif)

----------

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Moduland/Orangetool/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Moduland/Orangetool/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/Moduland/Orangetool/badges/build.png?b=master)](https://scrutinizer-ci.com/g/Moduland/Orangetool/build-status/master)
[![Python](https://img.shields.io/badge/python-3.3%2C3.4%2C3.5%2C3.6-blue.svg)](http://www.python.org)		


----------
		



# Orangetool
	
Consist of some useful script for Orangepi/Raspberrypi boards (Under Development)
Tested on Lubuntu

----------
	
By [Moduland Co](http://www.moduland.ir)		


</hr>
</hr>
## Download ##

- [Download](https://github.com/Moduland/Orangetool/archive/master.zip) source from github

## IP Functions ##

```python
import orangetool

#1- local_ip

local_ip=orange_tool.local_ip() # this function return local ip of board as string

#2- global_ip

global_ip=orange_tool.global_ip() # this function return global ip of board as string

#3- internet 

status=orangetool.internet() #this function check internet connection and return True if internet connection is stable

```

## RAM Functions ##			

```python
 
#4- total ram

ram=orangetool.ram_total() #this function return total ram of the board

#5- free ram

ram=orangetool.ram_free() # this function return how much ram is available in the board

#6- ram percentage

ram=orangetool.ram_percent() # this function return available ram percentage

```

## Other Functions ##				

```python

#7- get_temp

temp=orangetool.get_temp() # this function return cpu temperature as string

#8- uptime

time=orangetool.uptime() # this function return uptime of system

```



- All of the functions in error state return `Error` String
- local_ip() and global_ip() originally are available in ipz package [Link](http://github.com/sepandhaghighi/ipz)
- RAM Functions in this version need psutil package

			

