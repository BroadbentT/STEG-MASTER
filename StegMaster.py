#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#                 PYTHON UTILITY FILE FOR DECRYPTING STEGGED FILES
#               BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Pre load any required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import sys
import shutil
import os.path
from termcolor import colored				# pip install termcolor

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                                
# Details : Conduct simple and routine tests on user supplied arguements.   
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

if os.geteuid() != 0:	
   print "\nPlease run this python script as root..."
   exit(True)

if len(sys.argv) < 2:
   print "\nUse the command python steg_master.py picture.jpg\n"
   exit(True)

rightfile = False
fileName  = sys.argv[1]
filextend = os.path.splitext(fileName)[1]
imagefile = [".png", ".bmp", ".jpg", ".gif", ".tiff", ".jpeg", "wav"]

if os.path.exists(fileName) == 0:
   print "\nFile " + fileName+ " was not found, did you spell it correctly?"
   exit(True)

for image in imagefile:
   if image == filextend.lower():
      rightfile = True

if rightfile == False:
   print "File " + fileName + " is not recognised as a picture format"
   exit (True)

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Check all required dependencies are installed on the system.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

chk_list1 = ["exiftool", "hexeditor", "binwalk", "xpdf", "enscript", "stegcracker", "steghide"]
installed = True

for check in chk_list1:
   checked = os.system("locate -i " + check + " > /dev/null")
   if checked != 0:
      print "I could not find " + check + "..."
      installed = False

if installed == False:
   print "Install missing dependencies before you begin"
   exit (True)

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Create functionall call to display my universal header.
# -------------------------------------------------------------------------------------

def header(fileName, hashData):
   os.system("clear")
   print " ____ _____ _____ ____    __  __    _    ____ _____ _____ ____    "
   print "/ ___|_   _| ____/ ___|  |  \/  |  / \  / ___|_   _| ____|  _ \   "
   print "\___ \ | | |  _|| |  _   | |\/| | / _ \ \___ \ | | |  _| | |_) |  "
   print " ___) || | | |__| |_| |  | |  | |/ ___ \ ___) || | | |___|  _ <   "
   print "|____/ |_| |_____\____|  |_|  |_/_/   \_\____/ |_| |_____|_| \_\  "
   print "                                                                  "
   print "BY TERENCE BROADBENT MSc DIGITAL FORENSICS & CYBERCRIME ANALYSIS\n"
   print "Filename : " + fileName
   print "MD5 Hash : " + hashData
   print('-' * 63) + "\n"

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Initiate program variables.
# Modified: N/A
# -------------------------------------------------------------------------------------

os.system("md5sum '" + fileName + "' > .Hash.txt")
hashData = open(".Hash.txt").readline().rstrip()
hashData = hashData.replace(fileName,"")
os.remove('.Hash.txt')

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Create the menu system.
# -------------------------------------------------------------------------------------

menu = {}
menu['(01)']="Display Metadata."
menu['(02)']="Reformat Image." 
menu['(03)']="Hexfile Examination."
menu['(04)']="Extract Data."
menu['(05)']="Stegcrack Image."
menu['(06)']="Parse Colours."
menu['(07)']="Mask Colours."
menu['(08)']="Compression Test."
menu['(09)']="Create Differential."
menu['(10)']="Create LSB Image."
menu['(11)']="View Parsed."
menu['(12)']="View Differntial."
menu['(13)']="View LSB"
menu['(14)']="Clean and Exit."

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Main Menu.
# -------------------------------------------------------------------------------------

while True: 
   header(fileName, hashData)
   options=menu.keys()
   options.sort()
   for entry in options: 
      print entry, menu[entry]
   selection=raw_input("\nPlease Select: ") 

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu option selected - Display the image information to the user.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='1':
      dirName = open("directories.txt", "r").readlines()[0].rstrip()
      if os.path.exists(dirName):
         shutil.rmtree(dirName)
      os.mkdir(dirName)
      os.system("exiftool '" + fileName + "' > " + dirName + "'" + fileName + "'")
      os.system("sed -i -e 1d " + dirName + "'" + fileName + "'")
      os.system("sed -i -e 2d " + dirName + "'" + fileName + "'")
      os.system("enscript -q " + dirName + "'" + fileName + "' --output=- | ps2pdf - > " + dirName + "Intelligence.pdf")
      os.remove(dirName + fileName)
      os.system("xpdf " + dirName + "Intelligence.pdf")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu option selected - Correct the image to its native format.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection =='2':
      current_extension = os.path.splitext(fileName)[1]
      os.system("exiftool -q '" + fileName + "' > .F1.txt")
      os.system("awk '/File Type Extension/{print $NF}' .F1.txt > .F2.txt")
      correct_extension = open(".F2.txt").readline().rstrip()
      correct_extension = "." + correct_extension
      os.remove('.F1.txt')
      os.remove('.F2.txt')
      if current_extension.lower() != correct_extension.lower():
         newimage = fileName[:fileName.index(current_extension)]
         newimage = newimage + correct_extension
         os.system("mv '" + fileName + "' " + "'" + newimage + "'")
         fileName = newimage
         print "\nThe image has been changed to its native format..."
      else:
         print "\nThe image is already in its correct native format..."           
      raw_input("Press any key to continue..")
        
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu option selected - Open the hexeditor with the image.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection =='3':
      os.system("hexeditor '" + fileName + "'")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu option selected - Extract any data from the image.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '4':
      dirName = open("directories.txt", "r").readlines()[1].rstrip()
      if os.path.exists(dirName):
         shutil.rmtree(dirName)
      os.mkdir(dirName)        
      os.system("binwalk -b '" + fileName + "'")
      os.system("foremost -Q '" + fileName + "' -o " + dirName)
      os.system("binwalk -q -e -V -C '" + dirName + fileName + "'")
      os.system("binwalk -q -D '.sql:myd:myisamchk' '" + fileName + "' -C '" + dirName + fileName + "'") #myisamchk command
      os.system("strings '" + fileName + "' > " + dirName + "/strings.txt")
      print "Extracted files have been exported to dirName " + dirName + "..."
      raw_input("Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu option selected - Stegcrack the image.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '5':
      filextend = os.path.splitext(fileName)[1]
      imagefile = [".jpg", ".jpeg", ".bmp", ".gif", ".wav", ".au"]
      rightfile = False
      for image in imagefile:
         if image == filextend.lower():
            rightfile = True
      if rightfile == True:
         quicktest = os.path.exists("'" + fileName + ".out'")
         if quicktest == False:
            print "\nPlease wait, this could take sometime..."
            dictionary = open("directories.txt", "r").readlines()[10].rstrip()
            os.system("stegcracker '" + fileName + "' " + dictionary + " > F1.txt > /dev/null 2>&1")
            os.system("tail -2 F1.txt > F2.txt")
            os.system("awk '/password:/{print $NF}' F2.txt > F3.txt")
            password = open("F3.txt").readline().rstrip()           
            os.remove('./F1.txt')
            os.remove('./F2.txt')
            os.remove('./F3.txt')            
            if password != "":
               print "The password is '" + password + "'..."
               print "An extraction file has been written to " + fileName + ".out..."
            else:
               print "Password file exhausted..."
         else:
            print "\nThe extraction file already exists in this dirName..."
         raw_input("Press any key to continue...")
      else:
         print "\nUnsupported file type..."
         raw_input("Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Menu option - Parse the colours in the image and set them as transparent.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '6': 
      dirName = open("directories.txt", "r").readlines()[2].rstrip()
      if os.path.exists(dirName):
         shutil.rmtree(dirName)
      os.mkdir(dirName)
      colours = ["red", "green", "blue", "cyan", "magenta", "yellow", "black", "white"]
      for paint in colours:
         os.system("convert '" + fileName + "' -transparent " + paint + " '" + dirName + paint + "-" + fileName + "'")
      print "\nAll images have been exported to dirName " + dirName + "..." 
      raw_input("Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu option selected - 8 bit mask the pixel cunks.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '7':
      extension = os.path.splitext(fileName)[1]
      if extension != ".png":
         print "\nTo use this utility, first convert " + fileName+ " to a .png format..."
      else:
         directory1 = open("directories.txt", "r").readlines()[3].rstrip()
         directory2 = open("directories.txt", "r").readlines()[4].rstrip()
         if os.path.exists(directory1):
            shutil.rmtree(directory1)
            shutil.rmtree(directory2)
         os.mkdir(directory1)
         os.mkdir(directory2)
         for chunk in range (0,255):
            os.system("python mask-1.py '" + fileName + "' " + directory1 + "pixilmask-" + str(chunk) + ".png " + str(chunk))
         print "\nCheck the files exported to dirName " + directory1 + "..." 
         print "Find an image that seems to reveal hidden information, such as image 127..."
         print "Enter that value below for further in-depth analysis, or any other key to quit..."  
         userinput = raw_input("")
         if (userinput.isalpha()) or (userinput=="") or (int(userinput)+0 < 0) or (int(userinput)+0 > 255):
            print "Sorry, the value entered is not incorrect..."
            shutil.rmtree(directory1)
            shutil.rmtree(directory2)
         else:
            for chunk in range (0,129):
               cmd = " " + directory2 + "range-color-" + str(userinput) + "+" + str(chunk) + ".png " + str(chunk) + " " + str(userinput)
               os.system("python mask-2.py '" + fileName + "'" + cmd)
            print "Now check the exported files in dirName " + directory2 + "..."
      raw_input("Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu option selected - Conduct a statistical image compression test.
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
         print "" + str(count) + " images were found to be of interest..."
         print "They have been placed in the " + directory3 + " dirName..."
      else:
         print "You need to option (7) first..."
      raw_input("Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu option selected - Create a differental image.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '9':
      dirName = open("directories.txt", "r").readlines()[7].rstrip()
      if os.path.exists(dirName):
         shutil.rmtree(dirName)
      os.mkdir(dirName)      
      os.system("cp '" + fileName + "' " + "'" + dirName + fileName + "'")
      current_extension = os.path.splitext(fileName)[1]
      newimage = fileName[:fileName.index(current_extension)]
      newimage = newimage + "-stripped" + current_extension
      option = 0
      print "\nDo you currently have a second image to compare with?..."
      print "[1] Yes [2] No..."
      user_option = raw_input("")
      if user_option == "1":
         print "Please enter the name of this file..."
         newimage = raw_input("")
         if os.path.exists(newimage) == 0:
            print "File " + newimage + " was not found, did you spell it correctly?"
         else:
            os.system("cp '" + newimage + "' " + dirName + newimage)
            option = 1 
      if user_option == "2":
         print "OK, I will create a second stripped and flattened image for you..."
         os.system("convert -strip -flatten '" + fileName + "' '" + dirName + newimage + "'")
         option = 1       
      if option == 1:
         print "Comparing images and creating differential image..."
         image1 = dirName + fileName
         image2 = dirName + newimage
         image3 = dirName + "difference" + current_extension
         os.system("compare -density 300 '" + image1 + "' '" + image2 + "' -compose src '" + image3 + "'")
         print "All images have been placed in directory " + dirName + "..."
      else:
         print "File " + user_option + " was not found..."
      raw_input("Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu option selected - Create least signicant bit image (lsb = 2).
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '10':
      dirName = open("directories.txt", "r").readlines()[8].rstrip()
      if os.path.exists(dirName):
         shutil.rmtree(dirName)
      os.mkdir(dirName)      
      os.system("stegolsb stegdetect -i '" + fileName + "' -n 2")
      lsbFile = fileName[:-4]
      lsbFile = lsbFile + "_2LSBs"
      lsbFile = lsbFile + fileName[-4:]
      os.system("mv '" + lsbFile + "' " + dirName)
      print "\nThe LSB image has been placed in directory " + dirName + "..." 
      raw_input("Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu option selected - View parsed images.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '11':
      dirName = open("directories.txt", "r").readlines()[2].rstrip()
      quicktest = os.path.exists(dirName)
      if quicktest == False:
         print "\nYou need to run option (6) first..."
         raw_input("Press any key to continue...")
      else:
         os.system("eog --slide-show " + dirName)

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu option selected - View diferential images.
# -------------------------------------------------------------------------------------

   elif selection == '12':
      dirName = open("directories.txt", "r").readlines()[7].rstrip()
      quicktest = os.path.exists(dirName)
      if quicktest == False:
         print "\nYou need to run option (9) first..."
         raw_input("Press any key to continue...")
      else:
         os.system("eog --slide-show " + dirName)

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu option selected - View LSB image.
# -------------------------------------------------------------------------------------

   elif selection == '13':
      dirName = open("directories.txt", "r").readlines()[8].rstrip()
      quicktest = os.path.exists(dirName)
      if quicktest == False:
         print "\nYou need to run option (10) first..."
         raw_input("Press any key to continue...")
      else:
         os.system("eog --slide-show " + dirName)

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu option selected - Clean and exit.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '14':
      for loop in range (0, 9):
         dirName = open("directories.txt", "r").readlines()[loop].rstrip()
         clutter = os.path.exists(dirName)
         if clutter == True:
            shutil.rmtree(dirName)
      clutter = os.path.exists("'" + fileName + ".out'")
      if clutter == True:
         os.remove("'" + fileName+ ".out'")        
      print "\nAll system generated files and directories have been sucessfully removed...\n"
      exit(True)

#Eof
