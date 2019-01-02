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
# CONTRACT: SME                                                               
# Version : 2.0                                                                
# Details : Show a universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

if banner == "nodisplay":
    print ""
else:
    print " ___ _   _ _____ ___    __  __    _    _  _______ ____   "
    print "|_ _| \ | |  ___/ _ \  |  \/  |  / \  | |/ / ____|  _ \  "
    print " | ||  \| | |_ | | | | | |\/| | / _ \ | ' /|  _| | |_) | "
    print " | || |\  |  _|| |_| | | |  | |/ ___ \| . \| |___|  _ <  "
    print "|___|_| \_|_|   \___/  |_|  |_/_/   \_\_|\_\_____|_| \_\ "
    print "                                                         "
    print " BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)  "
    print "\nInfoMaker™ - Displays information relating to the image.\n"

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Gather information about the image...   
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

directory = "./information"
intelfile = "Intelligence.pdf"

direxists = os.path.exists(directory)

if direxists == True:
    intelfile = intelfile[:-4]
    countfile = os.listdir(directory)
    filenumbr = len(countfile)
    filenumbr = filenumbr + 1
    intelfile = intelfile + "-" + str(filenumbr)
    intelfile = intelfile + ".pdf"
else:
    os.mkdir(directory)

os.system("exiftool " + filename + " > " + directory + "/" + filename)
os.system("sed -i -e 1d " + directory + "/" + filename)
os.system("sed -i -e 2d " + directory + "/" + filename)
os.system("enscript -q " + directory + "/" + filename + " --output=- | ps2pdf - > " + directory + "/" + intelfile)
os.remove(directory + "/" + filename)
os.system("xpdf " + directory + "/" + intelfile)

print "System Message    : This information has been stored in directory " +  directory + "..."
raw_input("System Message    : Press any key to continue...")
exit(False)

#Eof

