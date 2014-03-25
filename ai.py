from songmodel import SongModel
import subprocess

class AI:
    def __init__(self, song):
        self.song = song
        self.model = SongModel()
        self.val = 0

    def get_song_datas(self):
        sub = subprocess.Popen(["sh", "-c", "training/BPMDetector --display " + self.song], bufsize = 0, stdout = subprocess.PIPE, stdin = subprocess.PIPE)
        out, err = sub.communicate()
        i = 0
        while out[i] != '\n' and out[i] != '.':
            i += 1
        val = int(out[:i])
        self.val = val

    def distance(self, bpm):
        if (self.val == 0):
            self.get_song_datas()
        return abs(bpm - self.val)

    def classify(self):
        dist = []
        vect, mat = self.model.get_datas()
        i = 0
        for item in mat:
            dist.append([i, self.distance(item[0])])
            i += 1
        print(dist)
        dist = sorted(dist, key=lambda x: x[1])
        print(dist)
        k = 4
        i = 0
        ktab = []
        while i < k:
            ktab.append(vect[dist[i][0]])
            i += 1
        ktab.sort()
        print(ktab)
        count = 0
        maxval = 0
        val = 0
        last = 0
        for item in ktab:
            if last != item:
                count = 0
            if count > maxval:
                maxval = count
                val = item
            count += 1
            last = item
        print(val)
