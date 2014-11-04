import sqlite3
import matplotlib.pyplot as plt

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
            cur.execute("CREATE TABLE IF NOT EXISTS Songs(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Style TEXT, Tempo INT, Rolloff FLOAT)")

    def __del__(self):
        self.db.close()

    def add(self, name, style, tempo, rolloff):
        val = "INSERT INTO Songs ('Name', 'Style', 'Tempo', 'Rolloff') VALUES('" + name + "','" + style + "'," + str(tempo) + "," + str(rolloff) + ")"
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
                mat.append([row[3], row[4]])
                i += 1
        return (vect, mat)

    def plot(self):
        vect, mat = self.get_datas()
        plt.scatter([row[0] for row in mat], [row[1] for row in mat], c=vect)
        plt.show()
