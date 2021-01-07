import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS birthRecords(id INTEGER PRIMARY KEY,name varchar(50) NOT NULL, birthday text NOT NULL)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT id,name,birthday FROM birthRecords")
        rows = self.cur.fetchall()
        return rows

    def insert(self,name, birthday):
        self.cur.execute("INSERT INTO birthRecords VALUES(NULL, ?, ?)", (name, birthday))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM birthRecords WHERE id = ?",(id,))
        self.conn.commit()

    def update(self,id, name, birthday):
        self.cur.execute("UPDATE birthRecords SET name = ?, birthday = ? WHERE id = ?" , (name,birthday,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
