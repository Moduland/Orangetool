![Logo](http://www.shaghighi.ir/findip/Files/orangetool.gif)

----------

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Moduland/Orangetool/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Moduland/Orangetool/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/Moduland/Orangetool/badges/build.png?b=master)](https://scrutinizer-ci.com/g/Moduland/Orangetool/build-status/master)
[![Python](https://img.shields.io/badge/python-3.3%2C3.4%2C3.5%2C3.6-blue.svg)](http://www.python.org)		


----------
		



# Orangetool
	
Consist of some useful script for Orangepi/Raspberrypi boards 

----------
	
By [Moduland Co](http://www.moduland.ir)		


</hr>
</hr>
## Download ##

- [Download](https://github.com/Moduland/Orangetool/archive/master.zip) source from github

## Functions ##

```python
import orangetool

#1- local_ip

local_ip=orange_tool.local_ip() # this function return local ip of board

#2- global_ip

global_ip=orange_tool.global_ip() # this function return global ip of board

#3- get_temp

temp=orangetool.get_temp() # this function return cpu temperature

#4- internet 

status=orangetool.internet() #this function check internet connection and return True if internet connection is stable


```

All of the functions in error state return `Error` String

			

