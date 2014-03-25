#! env python2.7

import sys
from teacher import Teacher
from ai import AI

def main():
    argv = sys.argv
    argc = len(argv)
    if argc < 2:
        print("Use classify --train or classify [song].")
    elif argv[1] == "--train":
        teacher = Teacher()
        teacher.train()
    else:
        ai = AI(argv[1])
        ai.classify()

main()
