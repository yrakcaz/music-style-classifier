from songmodel import SongModel
from extractor import Extractor
import subprocess, math

class AI:
    def __init__(self, song):
        self.song = song
        self.model = SongModel()
        self.extractor = Extractor()
        self.tempo = 0
        self.rolloffmoy = 0.0
        self.rolloffect = 0.0
        self.fluxmoy = 0.0
        self.fluxect = 0.0
        self.genre = []
        for l in open("training/Tracks/genres.txt"):
            self.genre.append(l.replace('\n',''))

    def get_song_datas(self):
        self.extractor.set_song(self.song)
        self.tempo = self.extractor.get_tempo()
        self.rolloffmoy = self.extractor.get_rolloff_moy()
        self.rolloffect = self.extractor.get_rolloff_ect()
        self.fluxmoy = self.extractor.get_flux_moy()
        self.fluxect = self.extractor.get_flux_ect()

    def distance(self, bpm, rolloffmoy, rolloffect, fluxmoy, fluxect):
        if (self.tempo == 0 or self.rolloffmoy == 0.0 or self.rolloffect == 0.0 or self.fluxmoy == 0.0 or self.fluxect == 0.0):
            self.get_song_datas()
        return math.sqrt(((bpm - self.tempo) ** 2) + ((rolloffmoy - self.rolloffmoy) ** 2) + ((rolloffect - self.rolloffect) ** 2) + ((fluxmoy - self.fluxmoy) ** 2) + ((fluxect - self.fluxect) ** 2))

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
            dist.append([i, self.distance(item[0], item[1], item[2], item[3], item[4])])
            i += 1
        dist = sorted(dist, key=lambda x: x[1])
        style = self.genre[self.knn(dist, 3, vect)]
        print(style)
