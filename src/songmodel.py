import sqlite3

genre = {"dubstep": 0, "dnb": 1, "electro": 2, "house": 3, "trance": 4}

class SongModel:
    def __init__(self):
        self.db = sqlite3.connect('datas.db')
        with self.db:
            cur = self.db.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Songs(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Style TEXT, Tempo INT, Moy INT)")

    def __del__(self):
        self.db.close()

    def add(self, name, style, tempo, moy):
        val = "INSERT INTO Songs ('Name', 'Style', 'Tempo', 'Moy') VALUES('" + name + "','" + style + "'," + str(tempo) + "," + str(moy) + ")"
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
                vect.append(genre[row[2]])
                mat.append([row[3], row[4]])
                i += 1
        return (vect, mat)
