# -*- coding: utf-8 -*-
"""Orangetool modules."""

from .orangetool_display import hdmi_on, hdmi_off, hdmi_size
from .orangetool_ip import internet, local_ip, global_ip, set_ip, ping, mac
from .orangetool_system import check_update, get_temp, uptime, idletime, wakeup, version, sleep, hibernate, halt, restart
from .orangetool_ram import ram_total, ram_used, ram_free, ram_percent, freeup
from .orangetool_storage import mount_status, storage_status, unmount, unmount_all, mount, usb_on, usb_off
from .orangetool_params import ORANGETOOL_VERSION

__version__ = ORANGETOOL_VERSION
