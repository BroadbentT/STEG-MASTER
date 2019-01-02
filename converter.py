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
import os.path

argvment = len(sys.argv)

if argvment >= 2:
    filename = sys.argv[1]

banner = "display"

if argvment >= 3:
    banner = sys.argv[2]

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version : 2.0                                                                
# Details : Display a universal header.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

if banner == "nodisplay":
    print ""
else:
    print "  ____ ___  _   ___     _______ ____ _____ _____ ____   "
    print " / ___/ _ \| \ | \ \   / / ____|  _ \_   _| ____|  _ \  "
    print "| |  | | | |  \| |\ \ / /|  _| | |_) || | |  _| | |_) | "
    print "| |__| |_| | |\  | \ V / | |___|  _ < | | | |___|  _ <  "
    print " \____\___/|_| \_|  \_/  |_____|_| \_\|_| |_____|_| \_\ "
    print "                                                        "
    print " BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)  "
    print "\nConverter™ - Corrects the file extension of the specified image to its native format.\n"

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 2.0                                                                
# Details : Find the correct native format for this image.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("exiftool -q " + filename + " > .F1.txt")
os.system("awk '/File Type Extension/{print $NF}' .F1.txt > .F2.txt")
correct_extension = open(".F2.txt").readline().rstrip()
correct_extension = "." + correct_extension
os.remove('.F1.txt')
os.remove('.F2.txt')

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 2.0                                                                
# Details : Check to see if image needs to be changed to it native format.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

current_extension = os.path.splitext(filename)[1]

if current_extension.lower() == correct_extension.lower():
    print "System Message    : The image is already in its correct native format..."
    raw_input("System Message    : Press any key to continue..")
    exit(False)

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 2.0                                                                
# Details : Create a new image, and let stegmaster know the name of that image.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

newimage = filename[:filename.index(current_extension)]
newimage = newimage + correct_extension
os.system("mv " + filename + " " + newimage)

with open('.trackfile.txt', 'w') as the_file:
    the_file.write(newimage)

print "System Message    : The image has been changed to its native format..."
raw_input("System Message    : Press any key to continue..\n")
exit(False)

#Eof
