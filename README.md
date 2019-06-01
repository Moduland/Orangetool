<div align="center">
<a href="http://www.orangetool.ir"><img src="http://moduland.github.io/Orangetool/images/orangetool.jpg" height=240px width=320px></a>

</br>
<a href="https://zenodo.org/badge/latestdoi/80631089"><img src="https://zenodo.org/badge/80631089.svg" alt="DOI"></a>
<a href="https://badge.fury.io/py/orangetool"><img src="https://badge.fury.io/py/orangetool.svg"></a>
<a href="https://anaconda.org/sepandhaghighi/orangetool"><img src="https://anaconda.org/sepandhaghighi/orangetool/badges/version.svg"></a>
<a href="http://www.orangetool.ir"><img src="https://img.shields.io/website-up-down-green-red/http/shields.io.svg?label=website"></a>

</div>

----------

## Table of contents					
   * [Overview](https://github.com/Moduland/Orangetool#overview)
   * [Installation](https://github.com/Moduland/Orangetool#installation)
   * [Usage](https://github.com/Moduland/Orangetool#usage)
   		* [IP Functions](https://github.com/Moduland/Orangetool#ip-functions)
   		* [RAM Functions](https://github.com/Moduland/Orangetool#ram-functions)
   		* [Storage Functions](https://github.com/Moduland/Orangetool#storage-functions)	
   		* [Display Functions](https://github.com/Moduland/Orangetool#display-functions)
   		* [System Functions](https://github.com/Moduland/Orangetool#system-functions)
   * [Issues & Bug Reports](https://github.com/Moduland/Orangetool#issues--bug-reports)
   * [Supported Device List](https://github.com/Moduland/Orangetool/blob/master/Supported_Device_List.md)
   * [Dependencies](https://github.com/Moduland/Orangetool#dependencies)
   * [Contribution](https://github.com/Moduland/Orangetool/blob/master/.github/CONTRIBUTING.md)
   * [Cite](https://github.com/Moduland/Orangetool#cite)
   * [Authors](https://github.com/Moduland/Orangetool/blob/master/AUTHORS.md)
   * [License](https://github.com/Moduland/Orangetool/blob/master/LICENSE)
   * [Donate](https://github.com/Moduland/Orangetool#donate-to-our-project)
   * [Changelog](https://github.com/Moduland/Orangetool/blob/master/CHANGELOG.md)
   * [Code of Conduct](https://github.com/Moduland/Orangetool/blob/master/.github/CODE_OF_CONDUCT.md)

## Overview
	
Control functions for Single-Board computers				

Tested on [Lubuntu](http://lubuntu.me/)

<table>
	<tr> 
		<td align="center">Open Hub</td>
		<td align="center"><a href="https://www.openhub.net/p/orangetool"><img src="https://www.openhub.net/p/orangetool/widgets/project_thin_badge.gif"></a></td>	
	</tr>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/count/orangetool"><img src="http://pepy.tech/badge/orangetool"></a></td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/Moduland/Orangetool"><img src="https://img.shields.io/github/stars/Moduland/Orangetool.svg?style=social&label=Stars"></a></td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center">Travis</td>
		<td align="center"><a href="https://travis-ci.org/Moduland/Orangetool"><img src="https://travis-ci.org/Moduland/Orangetool.svg?branch=master"></a></td>
		<td align="center"><a href="https://travis-ci.org/Moduland/Orangetool"><img src="https://travis-ci.org/Moduland/Orangetool.svg?branch=dev"></a></td>
	</tr>
</table>


<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a href="https://www.codacy.com/app/sepand-haghighi/Orangetool?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Moduland/Orangetool&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/ad9374e6e7b24a63b34d6a4f419497ac"/></a></td>	
		<td align="center"><a href="https://www.codefactor.io/repository/github/moduland/orangetool"><img src="https://www.codefactor.io/repository/github/moduland/orangetool/badge" alt="CodeFactor" /></a></td>		
	</tr>
</table>

----------
	
By [Moduland Co](http://www.moduland.ir)		


## Installation
### Source Code
- Download [Version 0.35](https://github.com/moduland/Orangetool/archive/v0.35.zip) or [Latest Source ](https://github.com/Moduland/Orangetool/archive/dev.zip)
- `pip3 install -r requirements.txt` or `pip install -r requirements.txt` (Need root access)	
- `python3 setup.py install` or `python setup.py install`
### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip3 install orangetool==0.35` or `pip install orangetool==0.35` (Need root access)	
<div align="center">
<a href="https://asciinema.org/a/141548" target="_blank"><img src="https://asciinema.org/a/141548.png" /></a>
</div>

### Conda

- Check [Conda Managing Package](https://conda.io/docs/user-guide/tasks/manage-pkgs.html#installing-packages-from-anaconda-org)
- `conda install -c sepandhaghighi orangetool` (Need root access)

### Easy install

- Run `easy_install --upgrade orangetool` (Need root access)

## Usage
												
### IP Functions

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

#6- mac

mac_dic=orangetool.mac() # return dict of all system net devices mac addresses



```

### RAM Functions		

```python
 
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

### Storage Functions				

```python
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

### Display Functions				

```python
#1- hdmi_on

orangetool.hdmi_on() # turn on hdmi port

#2- hdmi_off

orangetool.hdmi_off() # turn off hdmi port

#3- hdmi_size

orangetool.hdmi_size(1280,720) # this function change hdmi display resolution

```

### System Functions				

```python
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



- All of the functions in error state return `Error` String
- `local_ip` and `global_ip` originally are available in ipz package [Link](http://github.com/sepandhaghighi/ipz)
- RAM functions in this version need psutil package
- Running `set_ip` function remotely will freeze your terminal so it's better to set `restart` parameter to True
- Running `halt`,`restart` & `sleep` functions remotely will freeze your terminal
- Some of funtions need root access so it's better to run ```sudo -s``` before use this tool



## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!							
or send an email to [info@moduland.ir](mailto:info@moduland.ir "info@moduland.ir"). 

## Dependencies

<table>
	<tr> 
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center"><a href="https://requires.io/github/Moduland/Orangetool/requirements/?branch=master"><img src="https://requires.io/github/Moduland/Orangetool/requirements.svg?branch=master"></a></td>
		<td align="center"><a href="https://requires.io/github/Moduland/Orangetool/requirements/?branch=dev"><img src="https://requires.io/github/Moduland/Orangetool/requirements.svg?branch=dev"></a></td>
	</tr>
</table>

		
## Cite
If you use orangetool in your research , please cite this ;-)

<blockquote>
<p>Sepand Haghighi. 2017. Moduland/Orangetool: Version 0.23. (July 2017). DOI:http://dx.doi.org/10.5281/zenodo.829797</p>
</blockquote>			

						
					
## Donate to our project									

If you feel like our project is important can you please support us?			
Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do.

<h3>Bitcoin :</h3>					

```1XGr9qbZjBpUQJJSB6WtgBQbDTgrhPLPA```
				

<h3>Payping (For Iranian citizens) :</h3>

<a href="http://www.payping.net/sepandhaghighi" target="__blank"><img src="http://www.qpage.ir/images/payping.png" height=100px width=100px></a>

## License
<div align="center">
<a href="https://github.com/Moduland/orangetool/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mashape/apistatus.svg"/></a>
<br/>
<a href="http://www.moduland.ir" target="_blank" title="Moduland Website"><img src="http://www.orangetool.ir/images/moduland.jpg" height="128px" width="128px" alt="Moduland Website"></a>

</div>



			

