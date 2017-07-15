def hdmi_on(DEBUG=False):
    '''
    This function turn on hdmi port (need sudo -s)
    :param DEBUG: Flag for using Debug mode
    :type DEBUG:bool
    :return: bool
    '''
    try:
        hdmi_control=open("/sys/class/graphics/fb0/blank","w")
        hdmi_control.write("0")
        hdmi_control.close()
        return True
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"

def hdmi_off(DEBUG=False):
    '''
       This function turn off hdmi port (need sudo -s)
       :param DEBUG: Flag for using Debug mode
       :type DEBUG:bool
       :return: bool
       '''
    try:
        hdmi_control=open("/sys/class/graphics/fb0/blank","w")
        hdmi_control.write("4")
        hdmi_control.close()
        return True
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"
def hdmi_size(v=None,h=None,DEBUG=False):
    '''
    This function change hdmi display resolution (need sudo -s) (if call without any argument return current resolution)
    :param v: vertical line
    :param h: horizental line
    :param DEBUG: Flag for using Debug mode
    :type v : int
    :type h:int
    :type DEBUG:bool
    :return: bool
    '''
    try:
        if (not isinstance(v,int)) or (not isinstance(h,int)):
            hdmi_control = open("/sys/class/graphics/fb0/virtual_size", "r")
            resolution=hdmi_control.read()[:-1].replace(",","x")
            hdmi_control.close()
            return resolution
        hdmi_control = open("/sys/class/graphics/fb0/virtual_size", "w")
        hdmi_control.write(str(v)+","+str(h))
        hdmi_control.close()
        return True
    except Exception as e:
        if DEBUG==True:
            print(str(e))
        return "Error"
