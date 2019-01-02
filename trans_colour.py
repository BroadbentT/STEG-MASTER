#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#                  PYTHON UTILITY FILE FOR DECRYPTING STEGGED FILES
#                BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub           
# Version : 2.0                                                                
# Details : Load any required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import sys

argvment = len(sys.argv)

if argvment >= 2:
    filename = sys.argv[1]

banner = "display"
if argvment >= 3:
    banner = sys.argv[2]

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub           
# Version : 2.0
# Details : Show a universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

if banner == "nodisplay":
    print ""
else:
    print " _____ ____      _    _   _ ____     ____ ___  _     ___  _   _ ____   "
    print "|_   _|  _ \    / \  | \ | / ___|   / ___/ _ \| |   / _ \| | | |  _ \  "
    print "  | | | |_) |  / _ \ |  \| \___ \  | |  | | | | |  | | | | | | | |_) | "
    print "  | | |  _ <  / ___ \| |\  |___) | | |__| |_| | |__| |_| | |_| |  _ <  "
    print "  |_| |_| \_\/_/   \_\_| \_|____/   \____\___/|_____\___/ \___/|_| \_\ "
    print "                                                                       "
    print "        BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)          "
    print "\nTransColour™, Parses RGB, CMYK, and W within the image and makes them transparent."

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub           
# Version : 2.0
# Details : Decolourize the specified file.   
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

directory = "./transcolour"
dir_exist = os.path.exists(directory)

if dir_exist == False:
    os.mkdir(directory)
else:
    print "System Message    : Please remove directory " + directory + " to continue..."
    raw_input("System Message    : Press any key to continue..\n")
    exit(True)

colours = ["red", "green", "blue", "cyan", "magenta", "yellow", "black", "white"]

for paint in colours:
    os.system("convert " + filename + " -transparent " + paint + " " + directory + "/" + paint + "-" + filename)

print "System Message    : All images have been exported to directory " + directory + "..." 
raw_input("System Message    : Press any key to continue...")

#Eof
