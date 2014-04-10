from songmodel import SongModel
import subprocess, math
import acoustid

genre = []
genre.append("dubstep")
genre.append("dnb")
genre.append("electro")
genre.append("house")
genre.append("trance")

class AI:
    def __init__(self, song):
        self.song = song
        self.model = SongModel()
        self.val = 0
        self.val1 = 0
        self.val2 = ""

    def get_tempo(self):
        sub = subprocess.Popen(["sh", "-c", "training/BPMDetector --display " + self.song], bufsize = 0, stdout = subprocess.PIPE, stdin = subprocess.PIPE)
        out, err = sub.communicate()
        i = 0
        while out[i] != '\n' and out[i] != '.':
            i += 1
        val = int(out[:i])
        self.val = val

    def get_moy(self):
        sub = subprocess.Popen(["sh", "-c", "training/BPMDetector --moy " + self.song], bufsize = 0, stdout = subprocess.PIPE, stdin = subprocess.PIPE)
        out, err = sub.communicate()
        i = 0
        while out[i] != '\n':
            i += 1
        val = int(out[:i])
        self.val1 = abs(val / 8000000)


    def get_song_datas(self):
        self.get_tempo()
        self.get_moy()
        s, self.val2 = acoustid.fingerprint_file(self.song)

    def distance(self, bpm, moy, fingerprint):
        if (self.val == 0 and self.val1 == 0):
            self.get_song_datas()
        fingerdist = 0
        for i in xrange(min(len(fingerprint), len(self.val2))):
            fingerdist += abs(fingerprint[i] - self.val2[i])
        fingerdist /= min(len(fingerprint), len(self.val2))
        return math.sqrt((bpm - self.val) ** 2 + (moy - self.val1) ** 2 + fingerdist ** 2)

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
        vect, mat, h = self.model.get_datas()
        i = 0
        for item in mat:
            dist.append([i, self.distance(item[0], item[1], h[i])])
            i += 1
        dist = sorted(dist, key=lambda x: x[1])
        style = genre[self.knn(dist, 3, vect)]
        print(style)
