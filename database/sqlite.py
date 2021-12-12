import sqlite3 as sql
from create_bot import bot
import random
from keyboards import kb_client

base = sql.connect('code_chest.db')

def sql_start():


    if base:
        print('Connected to database')
    base.execute("CREATE TABLE if NOT EXISTS projects(level TEXT, language TEXT, name TEXT, description TEXT)")
    base.commit()


async def sql_add_project(state):
    async with state.proxy() as data:
        base.execute("INSERT INTO projects VALUES (?, ?, ?, ?)", tuple(data.values()))
        base.commit()


async def sql_read(message, state):
    async with state.proxy() as data:
        try:
            execute = base.execute(
                f"SELECT * FROM projects WHERE level == '{data['choise_level']}' AND language LIKE '{data['choise_lang']}'")
            result = execute.fetchall()
            answer = result[random.randint(0, len(result) - 1)]
            await bot.send_message(message.from_user.id,
                                   f'Level {answer[0]}\n  {answer[1]}\n Название проекта:\n {answer[2]}\n Описание:\n {answer[3]}',
                                   reply_markup=kb_client)

        except Exception:
            await bot.send_message(message.from_user.id, "Проектов по заданным критериям нет", reply_markup=kb_client)


async def sql_all_projects():
    return base.execute("SELECT * FROM projects").fetchall()


async def sql_delete_project(data):
    base.execute("DELETE FROM projects WHERE name = ?", (data,))
    base.commit()
