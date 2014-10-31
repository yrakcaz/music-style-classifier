from songmodel import SongModel
from extractor import Extractor
import json, subprocess

class Teacher:
    def __init__(self):
        self.model = SongModel()
        self.extractor = Extractor()

    def parse_set(self):
        content = []
        with open("training/Tracks/ground_truth.csv") as f:
            for l in f:
                l = l.replace('\"', '').replace('\n', '')
                name = ""
                genre = ""
                flag = 0
                for c in l:
                    if c == ',':
                        flag = 1
                    elif flag == 0:
                        name += c
                    elif flag == 1:
                        genre += c
                content.append([name, genre])
        return content

    def train(self):
        for item in self.parse_set():
            self.extractor.set_song(item[0])
            tempo = self.extractor.get_tempo()
            self.model.add(item[0], item[1], tempo)
            print("ADDED : " + item[0] + " " + item[1] + " " + str(tempo))
        print("DONE")
