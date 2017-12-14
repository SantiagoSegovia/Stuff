#!/usr/bin/python
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@     @@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@
#  @@@  @@@@@@@@@@@@@@@ @@@@@@@@@  @@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@ @@@@
#  @@@@@@@     @@@      @@@@@@@@@  @@@@@@  @@@  @@@@  @@@@     @@@@@ @@@@
#@     @@  @@@  @  @@@  @@     @@      @@  @@@  @@      @  @@@  @@@@ @@@@
#@@@@@  @       @@      @  @@@  @  @@@  @@      @@@@  @@@       @@@@ @@@@
#  @@@  @  @@@@@@@@@@@  @  @@@  @  @@@  @@@@@@  @@@@  @@@  @@@@@@@@@@@@@@
#@     @@@      @      @@@     @@      @@      @@@@@  @@@@      @@@@ @@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#------------------------------------------------------------------------
#| Author:   Santiago Segovia                                           |
#| Title:    Get trees                                                  |
#| Date:     14/12/2017                                                 |
#| Help key: None                                                       |
#------------------------------------------------------------------------
import os
import sys

def AddToPath(my_dir):
    sys.path.append(my_dir)

def get_subdirs(a_dir,appendFiles = False):
    if not os.path.isdir(a_dir):
        return []
    dir_list = next(os.walk(a_dir))[1]
    if appendFiles:
        dir_list.extend(next(os.walk(a_dir))[2])
    return dir_list

def SubDirs(my_dir, printTree = False, addToSysPath = False, appendFiles = False, header = "\\", max_depth = 10):
    if printTree:
        print header + my_dir
    if addToSysPath:
        AddToPath(my_dir)
    header = header.replace("\\"," |\\")
    if len(header) > max_depth:
        return
    subdirs = get_subdirs(my_dir,appendFiles)
    for i in range(len(subdirs)):
        subdir = subdirs[i]
        if printTree:
            print header.replace("\\"," ")
        if i == len(subdirs) - 1:
            header = header[:-2] + " " + header[-1] 
        SubDirs(os.path.join(my_dir,subdir),printTree=printTree,addToSysPath=addToSysPath,appendFiles=appendFiles,header=header,max_depth=max_depth)

def AddToPathRecursive(my_dir):
    SubDirs(my_dir, addToSysPath = True)

def Tree(my_dir):
    SubDirs(my_dir, printTree = True, appendFiles = True)

if __name__ == "__main__":
    print "This is a library."
    print "To use it add this lines in your script"
    print "import subdirs"
    if len(sys.argv) > 1:
        Tree(sys.argv[1])
