#!/usr/bin/python

import wnck, gtk, subprocess

def nudeWindow(screen, win):
    subprocess.check_output(["xprop", "-id", str(win.get_xid()), "-f", 
                             "_MOTIF_WM_HINTS", "32c", "-set", "_MOTIF_WM_HINTS",
                             '0x2, 0x0, 0x2, 0x0, 0x0'])
s = wnck.screen_get_default()
s.connect('window-opened', nudeWindow)
gtk.main()
