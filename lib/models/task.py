from db import CURSOR, CONN

class Task:
    def __init__(self, title, description, project_id, id=None):
        self.id = id
        self.title = title
        self.description = description
        self.project_id = project_id

    def save(self):
        if self.id is None:
            CURSOR.execute(
                'INSERT INTO tasks (title, description, project_id) VALUES (?, ?, ?)',
                (self.title, self.description, self.project_id)
            )
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute(
                'UPDATE tasks SET title = ?, description = ?, project_id = ? WHERE id = ?',
                (self.title, self.description, self.project_id, self.id)
            )
        CONN.commit()

    @staticmethod
    def get_all():
        CURSOR.execute('SELECT id, title, description, project_id FROM tasks')
        rows = CURSOR.fetchall()
        return [Task.from_db_row(row) for row in rows]

    @staticmethod
    def from_db_row(row):
        return Task(title=row[1], description=row[2], project_id=row[3], id=row[0])
