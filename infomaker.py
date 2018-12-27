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
   "\n"
else:
    print " ___ _   _ _____ ___    __  __    _    _  _______ ____   "
    print "|_ _| \ | |  ___/ _ \  |  \/  |  / \  | |/ / ____|  _ \  "
    print " | ||  \| | |_ | | | | | |\/| | / _ \ | ' /|  _| | |_) | "
    print " | || |\  |  _|| |_| | | |  | |/ ___ \| . \| |___|  _ <  "
    print "|___|_| \_|_|   \___/  |_|  |_/_/   \_\_|\_\_____|_| \_\ "
    print "                                                         "
    print " BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)  "
    print "\n"

# -------------------------------------------------------------------------------------
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Gather information about the image...   
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

intelfile = "Intelligence.txt"

inteltest = os.path.exists('./information')
if inteltest == True:
    intelfile = intelfile[:-4]
    countfile = os.listdir('./information')
    filenumbr = len(countfile)
    filenumbr = filenumbr + 1
    intelfile = intelfile + "-" + str(filenumbr)
    intelfile = intelfile + ".pdf"
else:
    os.mkdir('./information')

os.system("exiftool " + filename + " > ./information/information.txt")
os.system("sed -i -e 1d ./information/information.txt")
os.system("sed -i -e 2d ./information/information.txt")
os.system("enscript -q ./information/information.txt --output=- | ps2pdf - > ./information/" + intelfile)
os.system("xpdf ./information/" + intelfile)
os.remove('./information/information.txt')

exit(False)
#Eof
