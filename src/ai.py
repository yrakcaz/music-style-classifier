from songmodel import SongModel
from extractor import Extractor
from sklearn import svm, multiclass, neighbors
import subprocess, math

class AI:
    def __init__(self, song):
        self.song = song
        self.model = SongModel()
        self.extractor = Extractor()
        self.tempo = 0
        self.rolloffmoy = 0.0
        self.rolloffect = 0.0
        self.zcrmoy = 0.0
        self.zcrect = 0.0
        self.duration = 0.0
        self.genre = []
        for l in open("training/Tracks/genres.txt"):
            self.genre.append(l.replace('\n',''))

    def get_song_datas(self):
        self.extractor.set_song(self.song)
        self.tempo = self.extractor.get_tempo()
        self.rolloffmoy = self.extractor.get_rolloff_moy()
        self.rolloffect = self.extractor.get_rolloff_ect()
        self.zcrmoy = self.extractor.get_zcr_moy()
        self.zcrect = self.extractor.get_zcr_ect()
        self.duration = self.extractor.get_duration()

    def classify_with_knn(self):
        vect, mat = self.model.get_datas()
        clf = neighbors.KNeighborsClassifier()
        clf.fit(mat, vect)
        self.get_song_datas()
        l = [[self.tempo, self.rolloffmoy, self.rolloffect, self.zcrmoy, self.zcrect, self.duration]]
        ret = clf.predict(l)
        print(self.genre[ret[0]])

    def classify_with_svm(self):
        vect, mat = self.model.get_datas()
        clf = svm.SVC(class_weight='auto', kernel='linear')
        clf.fit(mat, vect)
        self.get_song_datas()
        l = [[self.tempo, self.rolloffmoy, self.rolloffect, self.zcrmoy, self.zcrect, self.duration]]
        ret = clf.predict(l)
        print(self.genre[int(ret[0])])
