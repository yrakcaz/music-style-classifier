import subprocess

class Extractor:
    def __init__(self):
        self.song = ""

    def set_song(self, song):
        self.song = song

    def get_tempo(self):
        sub = subprocess.Popen(["sh", "-c", "training/BPMDetector " + self.song], bufsize = 0, stdout = subprocess.PIPE, stdin = subprocess.PIPE)
        out, err = sub.communicate()
        i = 0
        while out[i] != '\n' and out[i] != '.':
            i += 1
        val = int(out[:i])
        return val
