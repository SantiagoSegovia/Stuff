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
DEBUG = 4
INFO = 3
WARNING = 2
ACTIONS = 1
class Logger:
    class __Logger:
        def __init__(self, filename):
            filename = os.path.realpath(filename)
            self.output = filename
            self.printLevel = INFO
            self.writeLevel = DEBUG
            self.file = open(filename,"a")
            self.user = os.environ['COMPUTERNAME']
            self.date = time.strftime("%d/%m/%Y")
            self.hour = time.strftime("%I:%M:%S")
            self.trace = False
            self.file.write("%s\n\nUser: %s\nDate: %s\nHour: %s\nFile: %s\nLogName: %s\n\n"%(header,self.user,self.date,self.hour,os.path.basename(log_name),self.output))
        def __str__(self):
            return self.output
        def debug(self,Msg):
            _str = "DEBUG:    %s"%(Msg)
            if self.file != None and self.writeLevel >= DEBUG:
                self.file.write(_str + "\n")
            if (not self.trace) and self.printLevel >= DEBUG:
                print _str
        def info(self,Msg):
            _str = "INFO:     %s"%(Msg)
            if self.file != None and self.writeLevel >= INFO:
                self.file.write(_str + "\n")
            if (not self.trace) and self.printLevel >= INFO:
                print _str
        def warning(self,Msg):
            _str = "WARNING:  %s"%(Msg)
            if self.file != None and self.writeLevel >= WARNING:
                self.file.write(_str + "\n")
            if (not self.trace) and self.printLevel >= WARNING:
                print _str
        def error(self,Msg, exit = False):
            _str = "ERROR:    %s"%(Msg)
            if self.file != None and self.writeLevel >= ACTIONS:
                self.file.write(_str + "\n")
            if (not self.trace) and self.printLevel >= ACTIONS:
                print _str
            if exit:
                self.exit(exit_code = 50)
        def success(self,Msg, exit = False):
            _str = "SUCCESS:  %s"%(Msg)
            if self.file != None and self.writeLevel >= ACTIONS:
                self.file.write(_str + "\n")
            if (not self.trace) and self.printLevel >= ACTIONS:
                print _str
            if exit:
                self.exit()
        def exit(self,exit_code = 0, Msg = "",erase = False):
            if Msg != "":
                _str = "EXITTING: %s"%(Msg)
                if self.file != None and self.writeLevel >= ACTIONS:
                    self.file.write(_str + "\n")
                if (not self.trace) and self.printLevel >= ACTIONS:
                    print _str
            if exit_code == 50:
                _str = "exit code 50 UNKNOWN ERROR"
            elif exit_code == 20:
                _str = "exit code 20 BAD ARGUMENT"
            elif exit_code == 12:
                _str = "exit code 12 DIFF FILENAME"
            else:
                _str = "exit code %i"%(exit_code)
            if self.file != None and self.writeLevel >= ACTIONS:
                self.file.write(_str + "\n")
            if (not self.trace) and self.printLevel >= ACTIONS:
                print _str
            if not self.trace:
                traceback.print_exc()
                self.trace = True
            try:
                self.file.close()
                self.file = None
            except:
                pass
            if erase:
                if _is_cmd:
                    os.system("del /s %s"%(self.output))
                else:
                    os.system("rm -f %s"%(self.output))
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
    sys.stdout.flush()
    creator = Logger(__file__)
    log = creator.getting_log()
    print "Logger ready :)"
    sys.stdout.flush()
    printHelp()
    sys.stdout.flush()
    log.info("Logger used in test Mode")
    sys.stdout.flush()
    while True:
        sys.stdout.write(">>> log.")
        sys.stdout.flush()
        asking = raw_input()
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
        sys.stdout.flush()
            

if __name__ == "__main__":
    main()
else:
    creator = Logger(log_name)
