#! env python2.7

import sys
from src.teacher import Teacher
from src.ai import AI

def main():
    argv = sys.argv
    argc = len(argv)
    if argc < 2 or argv[1] == "--help":
        print("Use classify --train or classify [song].")
    elif argv[1] == "--train":
        teacher = Teacher()
        teacher.train()
    elif argv[1] == "--display":
        teacher = Teacher()
        teacher.display()
    else:
        ai = AI(argv[1])
        ai.classify()

main()
