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
# Details : Pre load any required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import sys
import os.path
import shutil

argvment = len(sys.argv)

if argvment >= 2:
    filename = sys.argv[1]
else:
    print "Use the command python steg-master.py image.jpg"
    exit(True)

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Conduct simple and routine tests on supplied arguements.   
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

filextend = os.path.splitext(filename)[1]
imagefile = [".png", ".bmp", ".jpg", ".gif", ".tiff", ".jpeg"]
rightfile = False

if os.geteuid() != 0:
    print "Please run this python script as root"
    exit(True)

if os.path.exists(filename) == 0:
    print "\nFile " + filename + " was not found, did you spell it correctly?"
    exit(True)

for image in imagefile:
    if image == filextend.lower():
        rightfile = True

if rightfile == False:
    print "File " + filename + " is not recognised as a picture format"
    exit (True)

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Check all required dependencies are installed on the system.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

chk_list1 = ["steg", "exiftool", "hexeditor", "binwalk", "xpdf", "enscript", "stegcracker"]
installed = True

for check in chk_list1:
    checked = os.system("locate " + check + " > /dev/null")
    if checked != 0:
        print check + " is missing..."
        installed = False

if installed == False:
    print "Install missing dependencies before you begin"
    exit (True)

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Create all the variables for the main menu display.
# Modified: N/A
# -------------------------------------------------------------------------------------

os.system("md5sum " + filename + " > .Hash.txt")
hashdata = open(".Hash.txt").readline().rstrip()
hashdata = hashdata.replace(filename,"")
os.remove('.Hash.txt')

menu = {}
menu['(01)']="InfoMaker™."
menu['(02)']="Correct Image Extension." 
menu['(03)']="Hexfile Examination."
menu['(04)']="Extract Data Files. "
menu['(05)']="Stegcrack Image. "
menu['(06)']="TransColour™."
menu['(07)']="PalleteMask™."
menu['(08)']="Reduction™."
menu['(09)']="ImageDiff™."
menu['(10)']="TransColour™ Viewer."
menu['(11)']="ImageDiff™ Viewer."
menu['(20)']="Clean System."
menu['(21)']="Exit."

while True: 
    os.system("clear")

# -------------------------------------------------------------------------------------
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Display a universal header, plus the main menu system.  
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

    print " ____ _____ _____ ____   __  __    _    ____ _____ _____ ____   "
    print "/ ___|_   _| ____/ ___| |  \/  |  / \  / ___|_   _| ____|  _ \  "
    print "\___ \ | | |  _|| |  _  | |\/| | / _ \ \___ \ | | |  _| | |_) | "
    print " ___) || | | |__| |_| | | |  | |/ ___ \ ___) || | | |___|  _ <  "
    print "|____/ |_| |_____\____| |_|  |_/_/   \_\____/ |_| |_____|_| \_\ "
    print "                                                                "
    print "     BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)      "
    print ""
    print "File Name         : " + filename
    print "Hash Value        : " + hashdata + "\n"

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Main menu controller.
# Modified: N/A
# -------------------------------------------------------------------------------------

    options=menu.keys()
    print('-' * 63)
    options.sort()
    for entry in options: 
        print entry, menu[entry]
    selection=raw_input("\nPlease Select: ") 

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version : 1.0                                                                
# Details : Menu option selected - Display image information.
# Modified: N/A
# -------------------------------------------------------------------------------------

    if selection =='1':
        os.system("python info_maker.py " + filename + " nodisplay")        

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - Set the image to its native format.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection =='2':
        with open('.trackfile.txt', 'w') as the_file:
            the_file.write(filename)
        os.system("python converter.py " + filename + " nodisplay")
        file_changed = open('.trackfile.txt').readline().rstrip()        
        if file_changed != filename:
            filename = file_changed        
        os.remove('.trackfile.txt')
        
# ------------------------------------------------------------------------------------- 
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Menu option selected - Hex Editor.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection =='3':
 	os.system("hexeditor " + filename)

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - Extract any data from the image.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '4':
        directory = "./datadump"
        check = os.path.exists('./datadump')
        if check == True:
            print "\nSystem Message    : Please remove directory " + directory + " first..."
            raw_input("System Message    : Press any key to continue...")
        else:
            os.mkdir('./datadump')
            os.system("binwalk -b " + filename)
	    os.system("foremost -Q " + filename + " -o " + directory)
            os.system("binwalk -q -e -V -C " + directory + "/" + filename)
	    os.system("strings " + filename + " > " + directory + "/strings.txt")
            print "System Message    : Data files exported to directory " + directory + "..."
            raw_input("System Message    : Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - Stegcrack the image.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection =='5':
        testrunn = os.path.exists('./' + filename + ".out")
	if testrunn == True:
            print "\nSystem Message    : The extraction file already exists in this directory..."
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
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0
# Details : Menu option - Parse the colours in the image and set them as transparent.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '6': 
        os.system("python trans_colour.py " + filename + " nodisplay")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - 8 bit mask the pixel cunks.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '7':
        os.system("python pallete_mask.py " + filename + " nodisplay")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - Conduct a quick statistical test.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '8': 
        os.system("python reduction.py " + filename + " nodisplay")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - Create a differental image.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '9':
        os.system("python image_diff.py " + filename + " nodisplay")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - View TransColour™️ images.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '10':
        quicktest = os.path.exists('./transcolour')
        if quicktest == False:
            print "\nSystem Message    : You need to run TransColour™️ First..."
            raw_input("System Message    : Press any key to continue...")
        else:
            os.system("eog --slide-show ./transcolour")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - View DiffImage™️ images.
# -------------------------------------------------------------------------------------

    elif selection == '11':
        quicktest = os.path.exists('./difference')
        if quicktest == False:
            print "\nSystem Message    : You need to run ImageDiff™️ First..."
            raw_input("System Message    : Press any key to continue...")
        else:
            os.system("eog --slide-show ./difference")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - Tidy up the directory.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '20': 
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
        clutters = os.path.exists('./transcolour')
        if clutters == True:
            shutil.rmtree('./transcolour')
        clutters = os.path.exists('./difference')
        if clutters == True:
            shutil.rmtree('./difference')
        clutters = os.path.exists('./' + filename + ".out")
        if clutters == True:
            os.remove('./' + filename + ".out")
        print "\nSystem Message    : All system generated files have been removed..."
        raw_input("System Message    : Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - Quit the program.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '21':
        break

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Catch all other entries.
# Modified: N/A
# -------------------------------------------------------------------------------------

    else:
        print ""

#Eof
