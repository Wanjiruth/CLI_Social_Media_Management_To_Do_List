from db import CURSOR, CONN

class Project:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def save(self):
        if self.id is None:
            CURSOR.execute(
                'INSERT INTO projects (name) VALUES (?)',
                (self.name,)
            )
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute(
                'UPDATE projects SET name = ? WHERE id = ?',
                (self.name, self.id)
            )
        CONN.commit()

    @staticmethod
    def get_all():
        CURSOR.execute('SELECT id, name FROM projects')
        rows = CURSOR.fetchall()
        return [Project.from_db_row(row) for row in rows]

    @staticmethod
    def from_db_row(row):
        return Project(name=row[1], id=row[0])
