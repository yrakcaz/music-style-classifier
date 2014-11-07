import subprocess
from yaafelib import *

class Extractor:
    def __init__(self):
        self.song = ""
        self.fp = FeaturePlan(sample_rate=44100)
        self.fp.addFeature('sr: SpectralRolloff')
        self.fp.addFeature('zcr: ZCR')
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
        return float(((sum(self.feats['sr']) / len(self.feats['sr'])) / 50)[0])

    def get_rolloff_ect(self):
        m = float((sum(self.feats['sr']) / len(self.feats['sr']))[0])
        l = [(x - m) ** 2 for x in self.feats['sr']]
        v = float(sum(l) / len(l))
        return (v ** 0.5) / 50

    def get_zcr_moy(self):
        return float(((sum(self.feats['zcr']) / len(self.feats['zcr'])) * 1000)[0])

    def get_zcr_ect(self):
        m = float((sum(self.feats['zcr']) / len(self.feats['zcr']))[0])
        l = [(x - m) ** 2 for x in self.feats['zcr']]
        v = float(sum(l) / len(l))
        return (v ** 0.5) * 1000
