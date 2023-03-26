import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()

    if db:
        print('connected')

    db.execute('''
    CREATE TABLE IF NOT EXISTS mentors
    (id INTEGER PRIMARY KEY,
    name VARCHAR (30),
    direction VARCHAR (30),
    age INTEGER,
    "group" VARCHAR (10)
    )''')


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO mentors VALUES (?, ?, ?, ?, ?)',
                       tuple(data.values()))
        db.commit()


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (id,))
    db.commit()