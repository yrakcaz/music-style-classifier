import subprocess
from yaafelib import *

class Extractor:
    def __init__(self):
        self.song = ""
        self.fp = FeaturePlan(sample_rate=44100)
        self.fp.addFeature('sr: SpectralRolloff')
        self.engine = Engine()
        self.engine.load(self.fp.getDataFlow())
        self.afp = AudioFileProcessor()
        self.feats = []

    def set_song(self, song):
        self.song = song
        self.afp.processFile(self.engine, self.song)
        self.feats = self.engine.readAllOutputs()

    def get_tempo(self):
        sub = subprocess.Popen(["sh", "-c", "training/BPMDetector " + self.song], bufsize = 0, stdout = subprocess.PIPE, stdin = subprocess.PIPE)
        out, err = sub.communicate()
        i = 0
        while out[i] != '\n' and out[i] != '.':
            i += 1
        val = int(out[:i])
        return val

    def get_rolloff_moy(self):
        return float(((sum(self.feats['sr']) / len(self.feats['sr'])) / 10)[0])
