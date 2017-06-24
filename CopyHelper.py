#!/usr/bin/python

import os
import string
import time
import shutil

###################################################
# File name will be changed to YYMMDD_filename format 

# Source directory of the images.
__SRCDIR__ = "/home/tarun/Downloads"

# Destination Directory to Store your images
__DESTDIR__ = "/home/tarun/Pictures/Recent"


def copyIt(arg, dirname, names):
    sdatetime = time.strftime("%y%m%d")
    for name in names:
        if string.lower(name[-3:]) in ("jpg", "mov", "png"):
            srcfile = "%s/%s" % (dirname, name)
            destfile = "%s/%s_%s" % (__DESTDIR__, sdatetime, name)
            print destfile
            shutil.copyfile( srcfile, destfile)


if __name__ == "__main__":
    os.path.walk(__SRCDIR__, copyIt, None)