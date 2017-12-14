import os
import sys

def AddToPath(my_dir):
    sys.path.append(my_dir)

def get_subdirs(a_dir):
    dir_list = next(os.walk(a_dir))[1]

    return dir_list

def SubDirs(my_dir, printTree = False, addToSysPath = False, header = "\\", max_depth = 10):
    if printTree:
        print header + my_dir
    if addToSysPath:
        AddToPath(my_dir)
    header = header.replace("\\"," |\\")
    if len(header) > max_depth:
        return
    subdirs = get_subdirs(my_dir)
    for i in range(len(subdirs)):
        subdir = subdirs[i]
        if printTree:
            print header.replace("\\"," ")
        if i == len(subdirs) - 1:
            header = header[:-2] + " " + header[-1] 
        SubDirs(os.path.join(my_dir,subdir),printTree=printTree,addToSysPath=addToSysPath,header=header,max_depth=max_depth)

def AddToPathRecursive(my_dir):
    SubDirs(my_dir, addToSysPath = True)

def Tree(my_dir):
    SubDirs(my_dir, printTree = True)

if __name__ == "__main__":
    print "This is a library."
    print "To use it add this lines in your script"
    print "import subdirs"

Tree(sys.argv[1])
