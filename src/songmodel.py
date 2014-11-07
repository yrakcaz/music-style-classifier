import sqlite3
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class SongModel:
    def __init__(self):
        i = 0
        self.genre = {}
        for l in open("training/Tracks/genres.txt"):
            self.genre[l.replace('\n', '')] = i
            i += 1
        self.db = sqlite3.connect('training/datas.db')
        with self.db:
            cur = self.db.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Songs(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Style TEXT, Tempo INT, RolloffMoy FLOAT, RolloffEct FLOAT, ZcrMoy FLOAT, ZcrEct FLOAT)")

    def __del__(self):
        self.db.close()

    def add(self, name, style, tempo, rolloffmoy, rolloffect, zcrmoy, zcrect):
        val = "INSERT INTO Songs ('Name', 'Style', 'Tempo', 'RolloffMoy', 'RolloffEct', 'ZcrMoy', 'ZcrEct') VALUES('" + name + "','" + style + "'," + str(tempo) + "," + str(rolloffmoy) + "," + str(rolloffect) + "," + str(zcrmoy) + "," + str(zcrect) + ")"
        with self.db:
            cur = self.db.cursor()
            cur.execute("SELECT Id FROM Songs WHERE Name = '" + name + "'")
            if cur.fetchone() == None:
                cur.execute(val)

    def get_datas(self):
        vect = []
        mat = []
        with self.db:
            cur = self.db.cursor()
            cur.execute("SELECT * FROM Songs")
            rows = cur.fetchall()
            i = 0
            for row in rows:
                vect.append(self.genre[row[2]])
                mat.append([row[3], row[4], row[5], row[6], row[7]])
                i += 1
        return (vect, mat)

    def plot(self):
        vect, mat = self.get_datas()
        #fig = plt.figure()
        #ax = fig.add_subplot(111, projection='3d')
        #ax.scatter([row[0] for row in mat], [row[1] for row in mat], [row[2] for row in mat], c=vect)
        #ax.set_xlabel("BPM")
        #ax.set_ylabel("rolloff moyen")
        #ax.set_zlabel("rolloff ecart-type")
        plt.scatter([row[3] for row in mat], [row[4] for row in mat], c=vect)
        plt.show()
