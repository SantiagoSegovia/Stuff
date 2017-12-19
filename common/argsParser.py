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
#| Title:    Arguments parser                                           |
#| Date:     19/12/2017                                                 |
#| Help key: None                                                       |
#------------------------------------------------------------------------
import os
import sys

_my_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(_my_path,"..")))
import appendAll
import My_logger as logger

log = logger.get_log()

parser = None

class parserClass:
    class args:
        def __init__(self):
            setattr(self,"help",None)
    class action:
        def __init__(self,action_str,shorcut,dest,help):
            self.action_str = action_str
            self.shorcut = shorcut
            self.dest = dest
            self.help = help
            log.debug("Action added: %s"%action_str)
    class option:
        def __init__(self,option_str,shorcut,dest,types,help,default):
            self.option_str = option_str
            self.shorcut = shorcut
            self.dest = dest
            if type(types) is str:
                if types in ["int","INT","<int>","<INT>"]:
                    self.types = int
                elif types in ["str","STR","<str>","<STR>"]:
                    self.types = str
                elif types in ["float","FLOAT","<float>","<FLOAT>"]:
                    self.types = float
                elif types in ["bool","BOOL","<bool>","<BOOL>","boolean","BOOLEAN","<boolean>","<BOOLEAN>"]:
                    self.types = bool
                else:
                    log.error("Invalid type: %s"%types)
                    log.exit(50)
            else:
                self.types = types
            self.help = help
            if (default != None) and (not (type(default) is self.types)):
                log.error("Invalid default type: %s vs %s"%(str(type(default)),str(self.types)))
                log.exit(50)
            else:
                self.default = default
            log.debug("Option added: %s"%option_str)

    def __init__(self):
        self.arguments = self.args()
        self.actions = []
        self.addAction(action_str = "--help", shorcut = "-h", dest = "help",help="Print this format")
        self.options = []

    def printHelp(self):
        print "Help for: %s"%os.path.basename(logger.log_name)
        print "Actions"
        for act in self.actions:
            if act.shorcut == None:
                print "%s: \n\t%s\n\tDestination: arguments.%s"%(act.action_str,act.help,act.dest)
            else:
                print "%s, %s: \n\t%s\n\tDestination: arguments.%s"%(act.action_str,act.shorcut,act.help,act.dest)
        print "Options"
        for opt in self.options:
            if opt.shorcut == None:
                print "%s: (%s)\n\t%s\n\tDestination: arguments.%s\n\tDefault: %s"%(opt.option_str,str(opt.types),opt.help,opt.dest,opt.default)
            else:
                print "%s, %s: (%s)\n\t%s\n\tDestination: arguments.%s\n\tDefault: %s"%(opt.option_str,opt.shorcut,str(opt.types),opt.help,opt.dest,opt.default)

    def getActionList(self):
        res = []
        for act in self.actions:
            res.append(act.action_str)
        res2 = []
        for act in self.actions:
            res2.append(act.shorcut)
        return [res,res2]

    def getOptionList(self):
        res = []
        for opt in self.options:
            res.append(opt.option_str)
        res2 = []
        for opt in self.options:
            res2.append(opt.shorcut)
        return [res,res2]

    def addAction(self,action_str,shorcut=None,dest="no dest specified",help="The author of this script is very lazy and did not add any help for this action"):
        if not action_str.startswith("--"):
            log.error("Failed to add action %s. Actions must start with '--'."%action_str)
        if (shorcut != None) and (not shorcut.startswith("-")):
            log.error("Failed to add action %s. Action shortcuts must start with '-'."%shorcut)
        self.actions.append(self.action(action_str,shorcut,dest,help))
        setattr(self.arguments,dest,False)

    def addOption(self,option_str,shorcut=None,dest="no dest specified",type=str,help="The author of this script is very lazy and did not add any help for this action",default=None):
        self.options.append(self.option(option_str,shorcut,dest,type,help,default))
        setattr(self.arguments,dest,default)

    def parse(self):
        if ("--help" in sys.argv) or ("-h" in sys.argv):
            self.printHelp()
            log.exit(erase = True)
        [actions_l,actions_s] = self.getActionList()
        actions = actions_l
        actions.extend(actions_s)
        [options_l,options_s] = self.getOptionList()
        options = options_l
        options.extend(options_s)
        used = []
        for i in range(len(sys.argv)):
            used.append(False)
        for i in range(len(sys.argv)):
            arg = sys.argv[i]
            if arg in actions:
                if arg in actions_l:
                    idx = actions_l.index(arg)
                else:
                    idx = actions_s.index(arg)
                setattr(self.arguments,self.actions[idx].dest,True)
                if used[i]:
                    log.error("Repeated action: %s"%(arg))
                    log.exit(20)
                else:
                    used[i] = True
            if arg in options:
                if arg in options_l:
                    idx = options_l.index(arg)
                else:
                    idx = options_s.index(arg)
                if len(sys.argv) > (i+1) and not sys.argv[i+1].startswith("-"):
                    setattr(self.arguments,self.options[idx].dest,sys.argv[i+1])
                    if used[i]:
                        log.error("Repeated option: %s"%(arg))
                        log.exit(20)
                    else:
                        used[i] = True
                    if used[i+1]:
                        log.error("No argument in option. Expected %s %s"%(arg,str(self.options[idx].types)))
                        log.exit(20)
                    else:
                        used[i+1] = True
                else:
                    log.error("No argument in option. Expected %s %s"%(arg,str(self.options[idx].types)))
                    log.exit(20)
        return self.arguments

def Create():
    global parser
    parser = parserClass()

if __name__ == "__main__":
    log.info("Running in help/demo mode.")
    print "Use this library to add easy actions and options to your scripts"
    print "Valid types: int(hex or dec autodetected), str, bool and float"
    log.exit(0)

else:
    Create()