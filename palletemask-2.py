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
import struct
from zlib import crc32

#shutil.copyfile(sys.argv[1], sys.argv[2])

# -------------------------------------------------------------------------------------
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Show a universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

#    print " ____   _    _     _     _____ _____ _____   __  __    _    ____  _  __ "
#    print "|  _ \ / \  | |   | |   | ____|_   _| ____| |  \/  |  / \  / ___|| |/ / "
#    print "| |_) / _ \ | |   | |   |  _|   | | |  _|   | |\/| | / _ \ \___ \| ' /  "
#    print "|  __/ ___ \| |___| |___| |___  | | | |___  | |  | |/ ___ \ ___) | . \  "
#    print "|_| /_/   \_\_____|_____|_____| |_| |_____| |_|  |_/_/   \_\____/|_|\_\ "
#    print "                                                                        "
#    print "         BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)          "

# -------------------------------------------------------------------------------------
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Decolourize the specified file.   
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

defined = int(sys.argv[4])
defined = defined + 0
pngsig = '\x89PNG\r\n\x1a\n'

def swap_palette(filename, n):
    with open(filename, 'r+b') as f:
        f.seek(0)
        if f.read(len(pngsig)) != pngsig:
            print "\nSystem Message                  : File is not compatable with this program..."
        while True:
            chunkstr = f.read(8)
            if len(chunkstr) != 8:
                break
            length, chtype = struct.unpack('>L4s', chunkstr)
            if chtype == 'PLTE':
                curpos = f.tell()
                paldata = f.read(length)
# Replace palette entry defined to defined + n with white, the rest with black
                paldata = ("\x00\x00\x00" * defined) + ("\xff\xff\xff"*n) + ("\x00\x00\x00" * (256 - (defined + n)))
# Go back and write the modified palette in-place
                f.seek(curpos)
                f.write(paldata)
                f.write(struct.pack('>L', crc32(chtype+paldata)&0xffffffff))
            else:
                f.seek(length+4, os.SEEK_CUR)

# -------------------------------------------------------------------------------------
# AUTHOR: Terence Broadbent                                                    
# CONTRACT: SME                                                               
# Version: 1.0                                                                
# Details: Run the function swap_pallette with specified arguements.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

#swap_palette(sys.argv[2], int(sys.argv[3]))

if __name__ == '__main__':
    shutil.copyfile(sys.argv[1], sys.argv[2])
    swap_palette(sys.argv[2], int(sys.argv[3]))

#Eof

