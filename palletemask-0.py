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
import shutil

argvments = len(sys.argv)

if argvments >= 2:
    filesname = sys.argv[1]

filextend = filesname[-4:]

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

if bannertst != "nodisplay":
    print " ____   _    _     _     _____ _____ _____   __  __    _    ____  _  __ "
    print "|  _ \ / \  | |   | |   | ____|_   _| ____| |  \/  |  / \  / ___|| |/ / "
    print "| |_) / _ \ | |   | |   |  _|   | | |  _|   | |\/| | / _ \ \___ \| ' /  "
    print "|  __/ ___ \| |___| |___| |___  | | | |___  | |  | |/ ___ \ ___) | . \  "
    print "|_| /_/   \_\_____|_____|_____| |_| |_____| |_|  |_/_/   \_\____/|_|\_\ "
    print "                                                                        "
    print "         BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)          "
    print "\n"
   
# -------------------------------------------------------------------------------------
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Decolourize the specified file.   
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

if filextend != ".png":
    print "\nSystem Message    : To use this utility, reformat '" + filesname + "' to a .png format..."
    raw_input("System Message    : Press any key to continue...\n")
    exit(True)

test1 = os.path.exists('./pmask-1')
if test1 == False:
    os.mkdir('./pmask-1')
else:
    print "\nSystem Message    : Please remove directory ./pmask-1 first..."
    raw_input("System Message    : Press any key to continue...")
    exit(True)

test2 = os.path.exists('./pmask-2')
if test2 == False:
    os.mkdir('./pmask-2')
else:
    shutil.rmtree('./pmask-1')
    print "\nSystem Message    : Please remove directory ./pmask-2 first.."
    raw_input("System Message    : Press any key to continue..")
    exit(True)

print "\nSystem Message    : Pallete mask changes the pixil colours of the image...." 

for loop in range (0,255):
    os.system("python palletemask-1.py " + filesname + " ./pmask-1/pixilmask-" + str(loop) + ".png " + str(loop))

print "System Message    : Check the files exported to directory ./pmask-1..." 
print "System Message    : Find an image that seems to reveal hidden information, such as image 127..."
print "System Message    : Enter that value below for further in-depth analysis, or any other key to quit..."  

while True:
    userinput = raw_input("System Message    : ")
    if (userinput.isalpha()) or (userinput==""):
        print "System Message    : Quiting program..."
        shutil.rmtree('pmask-1')
        shutil.rmtree('pmask-2')
        raw_input("System Message    : Press any key to continue...\n")
        exit(True)
    elif (int(userinput)+0 < 0) or (int(userinput)+0 > 255):
        print "System Message    : Incorrect value entered...?"
    else:
        break

for loop in range (0,129):
    cmd =" ./pmask-2/range-color-" + str(userinput) + "+" + str(loop) + ".png " + str(loop) + " " + str(userinput)
    os.system("python palletemask-2.py " + filesname + cmd)

print "System Message    : Now check the exported files in directory ./maskdump2..."
raw_input("System Message    : Press any key to continue...\n")
exit(True) 

#Eof
