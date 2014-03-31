#! env python2.7

import sys, subprocess
import json

def main():
    argv = sys.argv
    argc = len(argv)
    print("\033[34m\033[1m================================================\033[0m\033[0m")
    print("\033[34m\033[1m          TESTS Music Style Classifier          \033[0m\033[0m")
    print("\033[34m\033[1m================================================\033[0m\033[0m\n")
    treat("training/set.txt")

def parse_file(f):
    content = ""
    with open(f) as f:
        for line in f:
            content += line
    return json.loads(content)

def treat(f):
    nbtests = 0
    nbsucc = 0
    for item in parse_file(f):
        nbtests += 1
        sub = subprocess.Popen(["sh", "-c", "python2.7 classify.py " + item[0]],
                               bufsize = 0, stdout = subprocess.PIPE, stdin = subprocess.PIPE)
        out, err = sub.communicate()
        val = out[:len(out) - 1]
        success = False
        if (val == item[1]):
            success = True
        print("\033[35mSong : \033[0m" + item[0])
        print("\033[35mResult : \033[0m" + val)
        print("\033[35mExpected : \033[0m" + item[1])
        if (success):
            nbsucc += 1
            print("\033[32m\033[1m[SUCCESS]\033[0m\033[0m\n")
        else:
            print("\033[31m\033[1m[FAILURE]\033[0m\033[0m\n")
    print("\033[33m\033[1mSuccess : " + str(nbsucc) + "/" + str(nbtests) + "\033[0m\033[0m")

main()