from songmodel import SongModel
import subprocess

genre = []
genre.append("dubstep")
genre.append("dnb")
genre.append("electro")
genre.append("house")

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

    def get_max(self, ktab):
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
        return val

    def knn(self, dist, k, vect):
        i = 0
        ktab = []
        while i < k:
            ktab.append(vect[dist[i][0]])
            i += 1
        ktab.sort()
        return self.get_max(ktab)

    def classify(self):
        dist = []
        vect, mat = self.model.get_datas()
        i = 0
        for item in mat:
            dist.append([i, self.distance(item[0])])
            i += 1
        dist = sorted(dist, key=lambda x: x[1])
        style = genre[self.knn(dist, 5, vect)]
        print("Your song is probably a " + style + " song!")
