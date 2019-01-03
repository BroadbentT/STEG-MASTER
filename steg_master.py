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
import linecache

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
# Details : Create the variables for the main menu display.
# Modified: N/A
# -------------------------------------------------------------------------------------

os.system("md5sum " + filename + " > .Hash.txt")
hashdata = open(".Hash.txt").readline().rstrip()
hashdata = hashdata.replace(filename,"")
os.remove('.Hash.txt')

menu = {}
menu['(01)']="Display Information."
menu['(02)']="Correct Image Format." 
menu['(03)']="Hexfile Examination."
menu['(04)']="Extract Data."
menu['(05)']="Stegcrack Image."
menu['(06)']="Parse Colours."
menu['(07)']="Mask Colours."
menu['(08)']="Compression Test."
menu['(09)']="Compare Images."
menu['(10)']="Signifant Bit."
menu['(11)']="View Parsed."
menu['(12)']="View Difference."
menu['(20)']="Clean System."
menu['(21)']="Exit."

while True: 
    os.system("clear")

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Display a universal header and start the menu system.
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

    options=menu.keys()
    print('-' * 63)
    options.sort()
    for entry in options: 
        print entry, menu[entry]
    selection=raw_input("\nPlease Select: ") 

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - Display the image information to the user.
# Modified: N/A
# -------------------------------------------------------------------------------------

    if selection =='1':
        directory = open("directories.txt", "r").readlines()[0].rstrip()
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.mkdir(directory)

        os.system("exiftool " + filename + " > " + directory + filename)
        os.system("sed -i -e 1d " + directory + filename)
        os.system("sed -i -e 2d " + directory + filename)
        os.system("enscript -q " + directory + filename + " --output=- | ps2pdf - > " + directory + "Intelligence.pdf")
        os.remove(directory + filename)
        os.system("xpdf " + directory + "Intelligence.pdf")

        print "System Message    : This information has been stored in directory " +  directory + "..."
        raw_input("System Message    : Press any key to continue...")       

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - Correct the image to its native format.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection =='2':
        current_extension = os.path.splitext(filename)[1]

        os.system("exiftool -q " + filename + " > .F1.txt")
        os.system("awk '/File Type Extension/{print $NF}' .F1.txt > .F2.txt")
        correct_extension = open(".F2.txt").readline().rstrip()
        correct_extension = "." + correct_extension
        os.remove('.F1.txt')
        os.remove('.F2.txt')

        if current_extension.lower() != correct_extension.lower():
            newimage = filename[:filename.index(current_extension)]
            newimage = newimage + correct_extension
            os.system("mv " + filename + " " + newimage)
            filename = newimage
            print "System Message    : The image has been changed to its native format..."
        else:
            print "System Message    : The image is already in its correct native format..."
           
        raw_input("System Message    : Press any key to continue..")
        
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - Open the hexeditor with the image.
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
        directory = open("directories.txt", "r").readlines()[1].rstrip()
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.mkdir(directory)
        
        os.system("binwalk -b " + filename)
        os.system("foremost -Q " + filename + " -o " + directory)
        os.system("binwalk -q -e -V -C " + directory + filename)
        os.system("binwalk -q -D '.sql:myd:myisamchk' " + filename + " -C " + directory + filename) #myisamchk command
	os.system("strings " + filename + " > " + directory + "/strings.txt")
        
        print "System Message    : Extracted files have been exported to directory " + directory + "..."        
        raw_input("System Message    : Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - Stegcrack the image.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection =='5':
        quicktest = os.path.exists('./' + filename + ".out")
	if quicktest == False:
            print "System Message    : Please wait, this could take sometime..."
           
            dictionary = open("directories.txt", "r").readlines()[9].rstrip()
            os.system("stegcracker " + filename + " " + dictionary + " > F1.txt")           

            os.system("tail -2 F1.txt > F2.txt")
            os.system("awk '/password:/{print $NF}' F2.txt > F3.txt")
            password = open("F3.txt").readline().rstrip()
           
            os.remove('./F1.txt')
            os.remove('./F2.txt')
            os.remove('./F3.txt')
            
            if password != "":
                print "System Message    : The password is '" + password + "'..."
                print "System Message    : An extraction file has been written to " + filename + ".out..."
            else:
                print "System Message    : Password file exhausted..."
        else:
            print "\nSystem Message    : The extraction file already exists in this directory..."

        raw_input("System Message    : Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0
# Details : Menu option - Parse the colours in the image and set them as transparent.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '6': 
        directory = open("directories.txt", "r").readlines()[2].rstrip()
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.mkdir(directory)

        colours = ["red", "green", "blue", "cyan", "magenta", "yellow", "black", "white"]

        for paint in colours:
            os.system("convert " + filename + " -transparent " + paint + " " + directory + paint + "-" + filename)

        print "\nSystem Message    : All images have been exported to directory " + directory + "..." 
        raw_input("System Message    : Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - 8 bit mask the pixel cunks.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '7':
        extension = os.path.splitext(filename)[1]
        if extension != ".png":
            print "System Message    : To use this utility, first convert " + filename + " to a .png format..."
        else:
            directory1 = open("directories.txt", "r").readlines()[3].rstrip()
            directory2 = open("directories.txt", "r").readlines()[4].rstrip()
            if os.path.exists(directory1):
                shutil.rmtree(directory1)
                shutil.rmtree(directory2)
            os.mkdir(directory1)
            os.mkdir(directory2)

            for chunk in range (0,255):
                os.system("python mask-1.py " + filename + " " + directory1 + "pixilmask-" + str(chunk) + ".png " + str(chunk))

            print "System Message    : Check the files exported to directory " + directory1 + "..." 
            print "System Message    : Find an image that seems to reveal hidden information, such as image 127..."
            print "System Message    : Enter that value below for further in-depth analysis, or any other key to quit..."  

            userinput = raw_input("System Message    : ")
            if (userinput.isalpha()) or (userinput=="") or (int(userinput)+0 < 0) or (int(userinput)+0 > 255):
                print "System Message    : Sorry, the value entered is not incorrect..."
                shutil.rmtree(directory1)
                shutil.rmtree(directory2)
            else:
                for chunk in range (0,129):
                    cmd = " " + directory2 + "range-color-" + str(userinput) + "+" + str(chunk) + ".png " + str(chunk) + " " + str(userinput)
                    os.system("python mask-2.py " + filename + cmd)
                print "System Message    : Now check the exported files in directory " + directory2 + "..."
        raw_input("System Message    : Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - Conduct a quick statistical test.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '8':
        directory1 = open("directories.txt", "r").readlines()[4].rstrip()
        directory2 = open("directories.txt", "r").readlines()[5].rstrip()
        directory3 = open("directories.txt", "r").readlines()[6].rstrip()
        if os.path.exists(directory1):
            if os.path.exists(directory2):
                shutil.rmtree(directory2)
                shutil.rmtree(directory3)
            os.mkdir(directory2)
            os.mkdir(directory3)
          
            os.system("cp " + directory1 + "*.* " + directory2)
            os.system("convert " + directory2 + "*.*")
            
            dirsize = 0
            for path, dirs, files in os.walk(directory2):
                for getfile in files:
                    calcfile = os.path.join(path, getfile)
                    dirsize += os.path.getsize(calcfile)
                    dirsize = int(dirsize) + 0
           
            average = (dirsize / len(directory2)-1)/50

            count = 0
            for path, dirs, files in os.walk(directory2):
                for getfile in files:
                    calcfile = os.path.join(path, getfile)
                    if os.path.getsize(calcfile) < average:
                        count = count + 1
                        os.system("cp " + calcfile + " " + directory3)

            print "System Message    : " + str(count) + " images were found to be of interest..."
            print "System Message    : They have been placed in the " + directory3 + " directory..."
        else:
            print "System Message    : You need to run pallete mask first..."
        raw_input("System Message    : Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - Create a differental image.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '9':
        directory = open("directories.txt", "r").readlines()[7].rstrip()
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.mkdir(directory)
        
        os.system("cp " + filename + " " + directory + filename)

        current_extension = os.path.splitext(filename)[1]
        newimage = filename[:filename.index(current_extension)]
        newimage = newimage + "-stripped" + current_extension
        option = 0

        print "System Message    : Do you currently have a second image to compare with?..."
        print "System Message    : [1] Yes [2] No..."
        user_option = raw_input("System Message    : ")

        if user_option == "1":
            print "System Message    : Please enter the name of this file..."
            newimage = raw_input("System Message    : ")
            if os.path.exists(newimage) == 0:
                print "System Message    : File " + newimage + " was not found, did you spell it correctly?"
            else:
                os.system("cp " + newimage + " " + directory + newimage)
                option = 1 

        if user_option == "2":
            print "System Message    : OK, I will create a second stripped and flattened image for you..."
            os.system("convert -strip -flatten " + filename + " " + directory + newimage)
            option = 1       

        if option == 1:
            print "System Message    : Comparing images and creating differential image..."
            image1 = directory + filename
            image2 = directory + newimage
            image3 = directory + "difference" + current_extension
            os.system("compare -density 300 " + image1 + " " + image2 + " -compose src " + image3)
            print "System Message    : All images have been placed in directory " + directory + "..."
        else:
            print "System Message    : File " + user_option + " was not found..."
        
        raw_input("System Message    : Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - View TransColour images.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '10':
        print "System Message    : Option not currently implemented..."
        raw_input("System Message    : Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - View TransColour images.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '11':
        directory = open("directories.txt", "r").readlines()[2].rstrip()
        quicktest = os.path.exists(directory)
        if quicktest == False:
            print "\nSystem Message    : You need to run parse colours first..."
        else:
            os.system("eog --slide-show " + directory)
        raw_input("System Message    : Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - View DiffImage images.
# -------------------------------------------------------------------------------------

    elif selection == '12':
        directory = open("directories.txt", "r").readlines()[7].rstrip()
        quicktest = os.path.exists(directory)
        if quicktest == False:
            print "\nSystem Message    : You need to run diff image first..."
        else:
            os.system("eog --slide-show " + directory)
        raw_input("System Message    : Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - Tidy up the directory.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '20':
        count = 0
        with open('directories.txt') as file:
            for line in file:
                directory = open("directories.txt", "r").readlines()[count].rstrip()
                clutters = os.path.exists(directory)
                if clutters == True:
                    shutil.rmtree(directory)
                count = count + 1

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
