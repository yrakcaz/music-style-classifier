#! env python2.7

import sys
from teacher import Teacher

def main():
    argv = sys.argv
    argc = len(argv)
    teacher = Teacher()
    teacher.train()
    teacher.print_content()

main()
