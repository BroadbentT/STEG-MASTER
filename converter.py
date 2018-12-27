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

paratest = len(sys.argv)
banntest = "display"

if paratest >= 2:
    filename = sys.argv[1]

if paratest >= 3:
    banntest = sys.argv[2]

# -------------------------------------------------------------------------------------
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Show a universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

if banntest == "nodisplay":
    print ""
else:
    print "  ____ ___  _   ___     _______ ____ _____ _____ ____   "
    print " / ___/ _ \| \ | \ \   / / ____|  _ \_   _| ____|  _ \  "
    print "| |  | | | |  \| |\ \ / /|  _| | |_) || | |  _| | |_) | "
    print "| |__| |_| | |\  | \ V / | |___|  _ < | | | |___|  _ <  "
    print " \____\___/|_| \_|  \_/  |_____|_| \_\|_| |_____|_| \_\ "
    print "                                                        "
    print " BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)  "
    print "\n"

# -------------------------------------------------------------------------------------
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Decolourize the specified file.   
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("exiftool " + filename + " > F1.txt")
os.system("awk '/File Type Extension/{print $NF}' F1.txt > F2.txt")
readata = open("F2.txt").readline().rstrip()

filetest = filename[-3:]
if filetest.lower() == readata.lower():
    os.remove('F1.txt')
    os.remove('F2.txt')
    print "System Message    : The image is already in its correct format..."
    raw_input("System Message    : Press any key to continue..\n")
    exit(False)

corrfile = filename[:-3]
finalchk = corrfile[-1:]
if finalchk != ".":
    corrfile = corrfile[:-1]

corrfile = corrfile + readata
os.system("mv " + filename + " " + corrfile)
os.system("echo " + corrfile + " > trackfile.txt")
os.remove('F1.txt')
os.remove('F2.txt')

print "System Message    : The image has been changed to its correct format..."
raw_input("System Message    : Press any key to continue..\n")
exit(False)

#Eof
