import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts(id INTEGER PRIMARY KEY,name text NOT NULL, birthday text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT id,name,birthday FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self,name, birthday):
        self.cur.execute("INSERT INTO parts VALUES(NULL, ?, ?)", (name, birthday))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id = ?",(id,))
        self.conn.commit()

    def update(self,id, name, birthday):
        self.cur.execute("UPDATE parts SET name = ?, birthday = ? WHERE id = ?" , (name,birthday,id))
        self.conn.commit()


    def __del__(self):
        self.conn.close()
