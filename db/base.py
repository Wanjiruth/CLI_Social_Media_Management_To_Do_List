from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# SQLite database file path
DB_FILE = 'company.db'

# Database engine
engine = create_engine(f'sqlite:///{DB_FILE}', echo=True)
meta = MetaData()

# Define your tables
projects = Table(
    'projects', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False)
)

tasks = Table(
    'tasks', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('description', String),
    Column('project_id', Integer),
)

def create_tables():
    meta.create_all(engine)
    print("Tables created successfully.")
