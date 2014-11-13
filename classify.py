#! env python2.7

import sys
from src.teacher import Teacher
from src.ai import AI
from src.songmodel import SongModel

def display_help():
    print("Use classify --train")
    print("             --knn [song]")
    print("             --svm [song]")

def main():
    argv = sys.argv
    argc = len(argv)
    if argc < 2 or argv[1] == "--help":
        display_help()
    elif argv[1] == "--train":
        teacher = Teacher()
        teacher.train()
    elif argv[1] == "--plot":
        model = SongModel()
        model.plot()
    elif argv[1] == "--knn":
        ai = AI(argv[2])
        ai.classify_with_knn()
    elif argv[1] == "--svm":
        ai = AI(argv[2])
        ai.classify_with_svm()
    else:
        display_help()

main()
