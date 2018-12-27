#!/usr/bin/python

# -------------------------------------------------------------------------------------
#                  PYTHON UTILITY FILE FOR DECRYPTING STEGGED FILES
#                BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Load any required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import sys

argvments = len(sys.argv)

if argvments >= 2:
    filesname = sys.argv[1]

bannertst = "display"
if argvments >= 3:
    bannertst = sys.argv[2]

# -------------------------------------------------------------------------------------
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Show a universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

if bannertst == "nodisplay":
    print ""
else:
    print "  ____ ___  _     ___  _   _ ____    __  __    _    ____  _  __ "
    print " / ___/ _ \| |   / _ \| | | |  _ \  |  \/  |  / \  / ___|| |/ / " 
    print "| |  | | | | |  | | | | | | | |_) | | |\/| | / _ \ \___ \| ' /  "
    print "| |__| |_| | |__| |_| | |_| |  _ <  | |  | |/ ___ \ ___) | . \  "
    print " \____\___/|_____\___/ \___/|_| \_\ |_|  |_/_/   \_\____/|_|\_\ "
    print "                                                                "
    print "     BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)      "
    print "\n"

# -------------------------------------------------------------------------------------
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Decolourize the specified file.   
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

testdir = os.path.exists('./rgb')

if testdir == False:
    os.mkdir('./rgb')
else:
    print "System Message    : Please remove directory ./rgb to continue..."
    raw_input("System Message    : Press any key to continue..\n")
    exit(True)

#print "System Message    : Colour mask makes RGB + Black transparent within the image..."

os.system("convert-im6.q16 " + filesname + " -transparent red ./rgb/red-" + filesname)
os.system("convert-im6.q16 " + filesname + " -transparent green ./rgb/green-" + filesname)
os.system("convert-im6.q16 " + filesname + " -transparent blue ./rgb/blue-" + filesname)
os.system("convert-im6.q16 " + filesname + " -transparent yellow ./rgb/yellow-" + filesname)
os.system("convert-im6.q16 " + filesname + " -transparent magenta ./rgb/magenta-" + filesname)
os.system("convert-im6.q16 " + filesname + " -transparent cyan ./rgb/cyan-" + filesname)
os.system("convert-im6.q16 " + filesname + " -transparent white ./rgb/white-" + filesname)
os.system("convert-im6.q16 " + filesname + " -transparent black ./rgb/black-" + filesname)

red = os.path.getsize('./rgb/red-' + filesname)
green = os.path.getsize('./rgb/green-' + filesname)
blue = os.path.getsize('./rgb/blue-' + filesname)
yellow = os.path.getsize('./rgb/yellow-' + filesname)
magenta = os.path.getsize('./rgb/magenta-' + filesname)
cyan = os.path.getsize('./rgb/cyan-' + filesname)
white = os.path.getsize('./rgb/white-' + filesname)
black = os.path.getsize('./rgb/black-' + filesname)

average = (red + green + blue + yellow + magenta + cyan + white + black) / 8

if red > average:
    print "System Message    : Is this the image your looking for....?"
    os.system("display ./rgb/red-" + filesname)
elif green > average:
    print "System Message    : Is this the image your looking for....?"
    os.system("display ./rgb/green-" + filesname)
elif blue > average:
    print "System Message    : Is this the image your looking for....?"
    os.system("display ./rgb/blue-" + filesname)
elif yellow > average:
    print "System Message    : Is this the image your looking for....?"
    os.system("display ./rgb/yellow-" + filesname)
elif magenta > average:
    print "System Message    : Is this the image your looking for....?"
    os.system("display ./rgb/magenta-" + filesname)
elif cyan > average:
    print "System Message    : Is this the image your looking for....?"
    os.system("display ./rgb/cyan-" + filesname)
else: 
    if black > average:
        print "System Message    : Is this the image your looking for....?"
        os.system("display ./rgb/black-" + filesname)

print "System Message    : All images have been exported to directory ./rgb..." 
raw_input("System Message    : Press any key to continue...\n")

#Eof
