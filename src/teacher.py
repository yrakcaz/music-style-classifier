from songmodel import SongModel
import json, subprocess
import matplotlib.pyplot as plot
import acoustid

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
            val1 = abs(int(out[:i]) / 8000000)
            s, val2 = acoustid.fingerprint_file(item[0])
            self.model.add(item[0], item[1], val, val1, val2)
            print("ADDED : " + item[0] + " " + item[1] + " " + str(val) + " " + str(val1) + " " + str(val2))
        print("DONE")

    def display(self):
        vect, mat, h = self.model.get_datas()
        x = []
        y = []
        color = []
        i = 0
        for item in mat:
            color.append
            x.append(item[0])
            y.append(item[1])
            i += 1
        plot.scatter(x, y, s=50, c=vect, alpha=0.5)
        plot.show()

