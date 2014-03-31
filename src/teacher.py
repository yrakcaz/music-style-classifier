from songmodel import SongModel
import json, subprocess

class Teacher:
    def __init__(self):
        self.model = SongModel()

    def parse_set(self):
        content = ""
        with open("training/set.txt") as f:
            for l in f:
                content += l
        return json.loads(content)

    def train(self):
        for item in self.parse_set():
            sub = subprocess.Popen(["sh", "-c", "training/BPMDetector --display " + item[0]], bufsize = 0, stdout = subprocess.PIPE, stdin = subprocess.PIPE)
            out, err = sub.communicate()
            i = 0
            while out[i] != '\n' and out[i] != '.':
                i += 1
            val = int(out[:i])
            sub1 = subprocess.Popen(["sh", "-c", "training/BPMDetector --moy " + item[0]], bufsize = 0, stdout = subprocess.PIPE, stdin = subprocess.PIPE)
            out, err = sub1.communicate()
            i = 0
            while out[i] != '\n':
                i += 1
            val1 = abs(int(out[:i]) / 4000000)
            self.model.add(item[0], item[1], val, val1)
            print("ADDED : " + item[0] + " " + item[1] + " " + str(val) + " " + str(val1))
        print("DONE")
