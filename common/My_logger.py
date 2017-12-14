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
#| Title:    Logger                                                     |
#| Date:     14/12/2017                                                 |
#| Help key: None                                                       |
#------------------------------------------------------------------------
import os
import sys
import time
import traceback

import __main__
log_name = __main__.__file__

creator = None
header = "         .-'''-.                                                 \n"\
".---.   '   _    \\                                               \n"\
"|   | /   /` '.   \\                       __.....__              \n"\
"|   |.   |     \  '  .--./)   .--./)  .-''         '.            \n"\
"|   ||   '      |  '/.''\\\\   /.''\\\\  /     .-''''-.  `. .-,.--.  \n"\
"|   |\\    \\     / /| |  | | | |  | |/     /________\\   \\|  .-. | \n"\
"|   | `.   ` ..' /  \\`-' /   \\`-' / |                  || |  | | \n"\
"|   |    '-...-'`   /(''`    /(''`  \    .-------------'| |  | | \n"\
"|   |               \\ '---.  \\ '---. \\    '-.____...---.| |  '-  \n"\
"|   |                /''''.\  /''''.\\ `.             .' | |      \n"\
"'---'               ||     ||||     ||  `''-...... -'   | |      \n"\
"                    \\'. __// \\'. __//                   |_|      \n"\
"                     `'---'   `'---'                             \n"
class Logger:
    class __Logger:
        def __init__(self, filename):
            filename = os.path.realpath(filename)
            if os.path.exists(filename):
                [name,ext] = os.path.splitext(filename)
                if ext != ".log":
                    print "WARNING:  Invalid extention %s. Changing to .log"%ext
                    ext = ".log"
                count = 0
                while os.path.exists(name + ".%02i"%count + ext):
                    count += 1
                filename = name + ".%02i"%count + ext
            self.output = filename
            self.file = open(filename,"w")
            self.user = os.environ['COMPUTERNAME']
            self.date = time.strftime("%d/%m/%Y")
            self.hour = time.strftime("%I:%M:%S")
            self.file.write("%s\n\nUser: %s\nDate: %s\nHour: %s\nFile: %s\nLogName: %s\n\n"%(header,self.user,self.date,self.hour,os.path.basename(log_name),self.output))
        def __str__(self):
            return repr(self)
        def debug(self,Msg):
            _str = "DEBUG:    %s"%(Msg)
            self.file.write(_str + "\n")
            print _str
        def info(self,Msg):
            _str = "INFO:     %s"%(Msg)
            self.file.write(_str + "\n")
            print _str
        def warning(self,Msg):
            _str = "WARNING:  %s"%(Msg)
            self.file.write(_str + "\n")
            print _str
        def error(self,Msg, exit = False):
            _str = "ERROR:    %s"%(Msg)
            self.file.write(_str + "\n")
            print _str
            if exit:
                self.exit(exit_code = 50)
        def success(self,Msg, exit = False):
            _str = "SUCCESS:  %s"%(Msg)
            self.file.write(_str + "\n")
            print _str
            if exit:
                self.exit()
        def exit(self,exit_code = 0, Msg = ""):
            if Msg != "":
                _str = "EXITTING: %s"%(Msg)
                self.file.write(_str + "\n")
                print _str
            if exit_code == 50:
                _str = "exit code 50 UNKNOWN ERROR"
                self.file.write(_str + "\n")
                print _str
            elif exit_code == 12:
                _str = "exit code 12 DIFF FILENAME"
                self.file.write(_str + "\n")
                print _str
            else:
                _str = "exit code %i"%(exit_code)
                self.file.write(_str + "\n")
                print _str
            traceback.print_exc()
            try:
                self.file.close()
            except:
                pass
            sys.exit(exit_code)
            
    
    instance = None
    
    def __init__(self, filename):
        if not self.instance:
            self.instance = self.__Logger(os.path.splitext(filename)[0] + ".log")
        else:
            if self.instance.output != filename:
                self.instance.error("filenames: %s vs %s"%(self.instance.output,filename),12)
    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    def getting_log(self):
        return self.instance


def printHelp():
    print "---------------------------------- LOG help ---------------------------------"
    print "import My_logger as logger"
    print "log = logger.get_log()\n"
    print "Useful functions:"
    print '    log.debug("Message")'
    print '    log.info("Message")'
    print '    log.warning("Message")'
    print '    log.error("Message",exit=False)'
    print '         #exit only available as a library, no in test mode'
    print '    log.success("Message",exit=False) '
    print '         #exit only available as a library, no in test mode'
    print '    log.exit(exit_code = 0,"Message" = "")'
    print '         #exit_code and Message only available as a library, no in test mode'
    print "-----------------------------------------------------------------------------"

def get_log():
    return creator.getting_log()

def main():
    global creator
    print "Creating logger..."
    creator = Logger(__file__)
    log = creator.getting_log()
    print "Logger ready :)"
    printHelp()
    log.info("Logger used in test Mode")
    while True:
        asking = raw_input(">>> log.")
        if asking.startswith('debug(') and asking.endswith(')'):
            msg = asking.strip(')').strip('debug(')[1:-1]
            log.debug(msg)
        elif asking.startswith('info(') and asking.endswith(')'):
            msg = asking.strip(')').strip('info(')[1:-1]
            log.info(msg)
        elif asking.startswith('warning(') and asking.endswith(')'):
            msg = asking.strip(')').strip('warning(')[1:-1]
            log.warning(msg)
        elif asking.startswith('error(') and asking.endswith(')'):
            msg = asking.strip(')').strip('error(')[1:-1]
            log.error(msg)
        elif asking.startswith('success(') and asking.endswith(')'):
            msg = asking.strip(')').strip('success(')[1:-1]
            log.success(msg)
        elif asking == "exit()":
            log.exit()
            

if __name__ == "__main__":
    main()
else:
    creator = Logger(log_name)