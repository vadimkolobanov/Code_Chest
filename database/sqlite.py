import sqlite3 as sql
from create_bot import bot


def sql_start():
    global base, cursor
    base = sql.connect('code_chest.db')
    cursor = base.cursor()
    if base:
        print('Connected to database')
    base.execute("CREATE TABLE if NOT EXISTS projects(level TEXT, language TEXT, name TEXT, description TEXT)")
    base.commit()


async def sql_add_project(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO projects VALUES (?, ?, ?, ?)", tuple(data.values()))
        base.commit()


async def sql_read(message):
    for answer in cursor.execute("SELECT * FROM projects").fetchall():
        await bot.send_message(message.from_user.id,
                               f'Уровень {answer[0]}\n Язык {answer[1]}\n Название проекта {answer[2]}\n Описание {answer[3]}')
