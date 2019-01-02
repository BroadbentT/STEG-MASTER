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
import shutil

argvments = len(sys.argv)

if argvments >= 2:
    filesname = sys.argv[1]

banner = "display"
if argvments >= 3:
    bannertst = sys.argv[2]

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
    print " ____  _____ ____  _   _  ____ _____ ___ ___  _   _  "
    print "|  _ \| ____|  _ \| | | |/ ___|_   _|_ _/ _ \| \ | | "
    print "| |_) |  _| | | | | | | | |     | |  | | | | |  \| | "
    print "|  _ <| |___| |_| | |_| | |___  | |  | | |_| | |\  | "
    print "|_| \_\_____|____/ \___/ \____| |_| |___\___/|_| \_| " 
    print "                                                     "
    print "BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)"
    print "\nReduction™ - Conducts a statisical examination of directory ./p-mask-2."

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version : 2.0                                                                
# Details : Check data exsits to undertake test.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

test1 = os.path.exists('./pmask-2')
test2 = os.path.exists('./reduction')
test3 = os.path.exists('./POI')

if test1 == False:
    print "System Message    : You need to run pallete mask first..."
    raw_input("System Message    : Press any key to continue...\n")
    exit (True)

if test2 == False:
    os.mkdir("./reduction")
else:
    print "\nSystem Message    : Please remove directories ./reducation and ./POI first..."
    raw_input("System Message    : Press any key to continue...\n")
    exit(True)

if test3 == False:
   os.mkdir("./POI")
else:
    print "System Message    : Reduction has already been run once...."
    print "System Message    : Remove directories ./Statistical and ./POI to run again..."
    raw_input("System Message    : Press any key to continue...\n")
    exit(True)

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version : 2.0                                                                
# Details : Decolourize the specified file.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("cp ./pmask-2/*.* ./reduction/")
os.system("convert ./reduction/*.*")

dirsize = 0
startpath = "./reduction"
for path, dirs, files in os.walk(startpath):
    for getfile in files:
        calcfile = os.path.join(path, getfile)
        dirsize += os.path.getsize(calcfile)
    dirsize = int(dirsize) + 0

list = os.listdir("./reduction")
numberfiles = len(list)
numberfiles = int(numberfiles) - 1

print "System Message    : Factoring is currently set at fifty percent...."

average = dirsize / numberfiles
average = average/50

count = 0
dirsize = 0
startpath = "./reduction"
for path, dirs, files in os.walk(startpath):
    for getfile in files:
        calcfile = os.path.join(path, getfile)
        if os.path.getsize(calcfile) < average:
              count = count + 1
              os.system("cp " + calcfile + " ./POI")
        dirsize += os.path.getsize(calcfile)
    dirsize = int(dirsize) + 0

print "System Message    : " + str(count) + " files were found to be of interest..."
print "System Message    : They have been placed in the ./POI directory..."
raw_input("System Message    : Press any key to continue...\n")
exit(True)

#Eof
