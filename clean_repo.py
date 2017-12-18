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
#| Title:    Clean all repo                                             |
#| Date:     18/12/2017                                                 |
#| Help key: None                                                       |
#------------------------------------------------------------------------
import os

import appendAll
import subdirs as subs
import My_logger as logger

try:
    rc = os.system("clear")
    if rc != 0:
        _is_cmd = True
        os.system("cls")
    else:
        _is_cmd = False
except:
    _is_cmd = True
    os.system("cls")

def main():
    dirs = subs.get_subdirs(".")
    _clean_folder_script = os.path.join(os.path.realpath("."),"clean_folder.sh")
    _clean_folder_bat_script = os.path.join(os.path.realpath("."),"clean_folder.bat")
    for dir in dirs:
        dir = os.path.realpath(dir)
        log.info("Cleaning path: %s"%dir)
        if _is_cmd:
            os.system("%s %s"%(_clean_folder_bat_script,dir))
        else:
            os.system("bash %s %s"%(_clean_folder_script,dir))
    log.info("Sounds weird, but need to delete this log file to get a fully clean repo.")
    log.exit(0,erase = True)

if __name__ == "__main__":
    log = logger.get_log()
    try:
        main()
    except:
        try:
            log.exit(50)
        except:
            pass
    if _is_cmd:
        raw_input("Press Enter to Finish")
