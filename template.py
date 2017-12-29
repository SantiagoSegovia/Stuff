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
#| Title:    Script template                                            |
#| Date:     19/12/2017                                                 |
#| Help key: None                                                       |
#------------------------------------------------------------------------
import os
import sys

_my_path = os.path.dirname(__file__)
sys.path.append(os.path.realpath(_my_path))
import appendAll
import My_logger as logger
import argsParser as argsParser

log = logger.get_log()
parser = argsParser.parser

def _parse_arguments():
    log.info("Parsing arguments")
    try:
        parser.addAction(action_str = "--run", 
                    shorcut = "-r", 
                    dest = "run",
                    help="Run such an important action.")
        parser.addOption(option_str = "--path",
                    shorcut="-p",
                    dest="path",
                    type=str,
                    help="This is a very important directory for the script.",
                    default=None)
        parser.addOption(option_str = "--count",
                    shorcut="-c",
                    dest="numberOfPins",
                    type=int,
                    help="This is the number of pins of something.",
                    default=0)
        parser.addOption(option_str = "--demo",
                    shorcut="-d",
                    dest="isDemo",
                    type=bool,
                    help="True if only is a demo.",
                    default=True)
        parser.addOption(option_str = "--version",
                    shorcut="-v",
                    dest="version",
                    type=float,
                    help="Excpected in forma ##.##",
                    default=1.0)
        arguments = parser.parse()
        return arguments
    except:
        log.error("Something were very bad parsing the arguments")
        log.exit(20)

def main():
    try:
        arguments = _parse_arguments()
        print arguments.run
        print arguments.path
        print arguments.numberOfPins
        print arguments.isDemo
        print arguments.version
        raw_input()
    except:
        log.error("Error in main application level.")
        log.exit(50)

if __name__ == "__main__":
    main()