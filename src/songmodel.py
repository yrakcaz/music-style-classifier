import sqlite3

genre = {"dubstep": 0, "dnb": 1, "electro": 2, "house": 3, "trance": 4}

class SongModel:
    def __init__(self):
        self.db = sqlite3.connect('training/datas.db')
        with self.db:
            cur = self.db.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Songs(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Style TEXT, Tempo INT, Moy INT, Fingerprint TEXT)")

    def __del__(self):
        self.db.close()

    def add(self, name, style, tempo, moy, fingerprint):
        val = "INSERT INTO Songs ('Name', 'Style', 'Tempo', 'Moy', 'Fingerprint') VALUES('" + name + "','" + style + "'," + str(tempo) + "," + str(moy) + "," + fingerprint + ")"
        with self.db:
            cur = self.db.cursor()
            cur.execute("SELECT Id FROM Songs WHERE Name = '" + name + "'")
            if cur.fetchone() == None:
                cur.execute(val)

    def get_datas(self):
        vect = []
        mat = []
        fingerprints = []
        with self.db:
            cur = self.db.cursor()
            cur.execute("SELECT * FROM Songs")
            rows = cur.fetchall()
            i = 0
            for row in rows:
                vect.append(genre[row[2]])
                mat.append([row[3], row[4]])
                fingerprints.append(row[5])
                i += 1
        return (vect, mat, fingerprints)
