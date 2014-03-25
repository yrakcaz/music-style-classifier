#! env python2.7

import sys
from teacher import Teacher
from ai import AI

def main():
    argv = sys.argv
    argc = len(argv)
    #teacher = Teacher()
    #teacher.train()
    #teacher.print_content()
    ai = AI(argv[1])
    ai.classify()

main()
