#!/usr/bin/python

# -------------------------------------------------------------------------------------
#                  PYTHON UTILITY FILE FOR DECRYPTING STEGGED FILES
#                BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Pre load any required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import sys
import shutil

# -------------------------------------------------------------------------------------
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Conduct simple and routine tests on supplied arguements.   
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

paratest = len(sys.argv)

if paratest >= 2:
    filename = sys.argv[1]
else:
    print "\nUse the command python steg-cracker.py picture.jpg\n"
    exit(True)

filextend = filename[-4:]
filetypes = [".png", ".bmp", ".jpg", ".gif", "tiff", "jpeg"]
rightfile = False

if os.geteuid() != 0:
    print "\nPlease run this python script as root..."
    exit(True)

if os.path.exists(filename) == 0:
    print "\nFile " + filename + " was not found, did you spell it correctly?"
    exit(True)

for check in filetypes:
    if check == filextend.lower():
        rightfile = True

if rightfile == False:
    print "File " + filename + " is not recognised as a picture format...."
    exit (True)

# -------------------------------------------------------------------------------------
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Check all required dependencies are installed on the system.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

instaled = True
chklist1 = ["steg", "exiftool", "hexeditor", "binwalk", "xpdf", "enscript", "stegcracker"]

for check in chklist1:
    checked = os.system("locate " + check + " > /dev/null")
    if checked != 0:
        print check + " is missing..."
        instaled = False

if instaled == True:
    print "\nAll required dependencies are pre-installed...\n"
else:
    print "\nInstall missing dependencies before you begin..."
    exit (True)

# -------------------------------------------------------------------------------------
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Start of the main menu display.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("md5sum " + filename + " > Hash.txt")
hashdata = open("Hash.txt").readline().rstrip()
hashdata = hashdata.replace(filename,"")
os.remove('Hash.txt')

menu = {}
menu['(0)']="Display Image Information."
menu['(1)']="Correct Image Extension."
menu['(2)']="Hexfile Examination."
menu['(3)']="Extract Data Files."
menu['(4)']="Stegcrack Image."
menu['(5)']="Colour Mask."
menu['(6)']="Pallete Mask."
menu['(7)']="Reduction Test."
menu['(8)']="Clean System."
menu['(9)']="Exit"

while True: 
    os.system("clear")

# -------------------------------------------------------------------------------------
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Display a universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

    print " ____ _____ _____ ____   __  __    _    ____ _____ _____ ____   "
    print "/ ___|_   _| ____/ ___| |  \/  |  / \  / ___|_   _| ____|  _ \  "
    print "\___ \ | | |  _|| |  _  | |\/| | / _ \ \___ \ | | |  _| | |_) | "
    print " ___) || | | |__| |_| | | |  | |/ ___ \ ___) || | | |___|  _ <  "
    print "|____/ |_| |_____\____| |_|  |_/_/   \_\____/ |_| |_____|_| \_\ "
    print "                                                                "
    print "     BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)      "
    print "\n"
 
# -------------------------------------------------------------------------------------

    print "File Name         : " + filename
    print "Hash Value        : " + hashdata + "\n"

    options=menu.keys()
    options.sort()
    for entry in options: 
        print entry, menu[entry]
    selection=raw_input("Please Select: ") 

# ------------------------------------------------------------------------------------- 
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Menu option zero selected - Hex Editor.
# Modified: N/A
# -------------------------------------------------------------------------------------

    if selection =='0':
        os.system("python infomaker.py " + filename + " nodisplay")        

# ------------------------------------------------------------------------------------- 
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Menu option one selected - Reformat the image.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection =='1':
        os.system("echo " + filename + " > trackfile.txt")
        os.system("python converter.py " + filename + " nodisplay")
        filechan = open("trackfile.txt").readline().rstrip()
        os.remove('trackfile.txt')
        if filechan != filename:
            filename = filechan
        
# ------------------------------------------------------------------------------------- 
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Menu option two selected - Hex Editor.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection =='2':
 	os.system("hexeditor " + filename)

# ------------------------------------------------------------------------------------- 
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Menu option three selected - Extract picture data to directories.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '3':
        datafile = os.path.exists('./datadump')
        if datafile == True:
            print "\nSystem Message    : Please remove directory ./datadump first..."
            raw_input("System Message    : Press any key to continue...")
        else:
            os.mkdir('./datadump')
            os.system("binwalk -b " + filename)
	    os.system("foremost -Q " + filename + " -o ./datadump/")
            os.system("binwalk -q -e -V -C ./datadump " + filename)
	    os.system("strings " + filename + " > ./datadump/strings.txt")
            print "System Message    : Data files exported to directory ./datadump..."
            raw_input("System Message    : Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Menu option four selected - Stegcrack Image.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection =='4':
        testrunn = os.path.exists('./' + filename + ".out")
	if testrunn == True:
            print "\nSystem Message    : The extraction file already exists in the directory..."
            raw_input("System Message    : Press any key to continue...")
        else:
            print "\nSystem Message    : Please wait, this could take sometime..."
            os.system("stegcracker " + filename + " /usr/share/wordlists/rockyou.txt > F1.txt")
            os.system("tail -2 F1.txt > F2.txt")
            os.system("awk '/password:/{print $NF}' F2.txt > F3.txt")
            password = open("F3.txt").readline().rstrip()
            os.remove('./F1.txt')
            os.remove('./F2.txt')
            os.remove('./F3.txt')
            if password != "":
                print "System Message    : The password is '" + password + "'..."
                print "System Message    : An extracted file has been written to " + filename + ".out..."
                raw_input("System Message    : Press any key to continue...")
            else:
                raw_input("System Message    : Password file exhausted, press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Menu option five - Colour mask file.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '5': 
        os.system("python colourmask.py " + filename + " nodisplay")

# ------------------------------------------------------------------------------------- 
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Menu option six selected - mask 8 bit pxel cunks.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '6':
        os.system("python palletemask-0.py " + filename + " nodisplay")

# ------------------------------------------------------------------------------------- 
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Menu option seven selected - Conduct statistical test.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '7': 
        os.system("python reduction.py " + filename + " nodisplay")

# ------------------------------------------------------------------------------------- 
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Menu option eight selected - Tidy up the directory.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '8': 
        clutters = os.path.exists('./datadump')
        if clutters == True:
            shutil.rmtree('./datadump')
        clutters = os.path.exists('./information')
        if clutters == True:
            shutil.rmtree('./information')
        clutters = os.path.exists('./pmask-1')
        if clutters == True:
            shutil.rmtree('./pmask-1')
        clutters = os.path.exists('./pmask-2')
        if clutters == True:
            shutil.rmtree('./pmask-2')
        clutters = os.path.exists('./POI')
        if clutters == True:
            shutil.rmtree('./POI')
        clutters = os.path.exists('./reduction')
        if clutters == True:
            shutil.rmtree('./reduction')
        clutters = os.path.exists('./rgb')
        if clutters == True:
            shutil.rmtree('./rgb')
        clutters = os.path.exists('./' + filename + ".out")
        if clutters == True:
            os.remove('./' + filename + ".out")
        print "\nSystem Message    : All system generated files have been removed..."
        raw_input("System Message    : Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Menu option nine selected - Quit program.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '9':
        break

# ------------------------------------------------------------------------------------- 
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Catch all other entries.
# Modified: N/A
# -------------------------------------------------------------------------------------

    else:
        print ""

#Eof
