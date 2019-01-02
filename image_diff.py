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
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Display a universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

if banner == "nodisplay":
   print ""
else:
    print " ___ __  __    _    ____ _____   ____ ___ _____ _____  "
    print "|_ _|  \/  |  / \  / ___| ____| |  _ \_ _|  ___|  ___| "
    print " | || |\/| | / _ \| |  _|  _|   | | | | || |_  | |_    "
    print " | || |  | |/ ___ \ |_| | |___  | |_| | ||  _| |  _|   "
    print "|___|_|  |_/_/   \_\____|_____| |____/___|_|   |_|     "
    print "                                                       "
    print "BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)  "
    print "\nImageDiff™ - Outputs the difference between specified two images.\n"

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Check the current directory status, i.e. has this utility been run before.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

directory = "./difference"
dir_check = os.path.exists(directory)

if dir_check == True:
    print "System Message    : Please remove the directory " + directory + " first..."
    raw_input("System Message    : Press any key to continue...\n")
    exit (True)
else:
    os.mkdir(directory)

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : identify the correct two images to be compared.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("cp " + filename + " " + directory + "/" + filename)

current_extension = os.path.splitext(filename)[1]
newimage = filename[:filename.index(current_extension)]
newimage = newimage + "-stripped" + current_extension

print "System Message    : Do you currently have a second image to compare with?..."
user_option = raw_input("System Message    : [1] Yes [2] No...\n")

if user_option == "1":
    newimage = raw_input("System Message    : Press enter the name of this file...\n")
    if os.path.exists(newimage) == 0:
        print "System Message    : File " + newimage + " was not found, did you spell it correctly?"
        raw_input("System Message    : Press any key to continue...\n")
        exit(True)
    else:
        os.system("cp " + newimage + " " + directory + "/" + newimage)
elif user_option == "2":
    print "System Message    : OK, I will create a second stripped and flattened image for you..."
    os.system("convert -strip -flatten " + filename + " " + directory + "/" + newimage)
else:
    print "System Message    : Incorrect responce..."
    raw_input("System Message    : Press any key to continue...\n")
    exit(True)

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Compare the two images and create a third, differential image.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

print "System Message    : Comparing images and creating differential image..."
os.system("compare -density 300 " + directory + "/" + filename + " " + directory + "/" + newimage + " -compose src " + directory + "/diff" + current_extension)
print "System Message    : All images have been placed in directory " + directory + "..."
raw_input("System Message    : Press any key to continue...")
exit(True)

#Eof
