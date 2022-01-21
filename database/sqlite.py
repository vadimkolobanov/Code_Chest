import os

import psycopg2
import requests
from dotenv import load_dotenv

from create_bot import bot
from keyboards import kb_client

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

    # Подключение к существующей базе данных
connection = psycopg2.connect(user='cwipxlmngfkrtf',
                              password='9d0df424b46c906b7fc24e5d3a639a62e375299d506fe2d711d4652fc0ef4a35',
                              host='ec2-54-77-182-219.eu-west-1.compute.amazonaws.com',
                              port='5432',
                              database='dejq0an5tcejbu')

base = connection.cursor()


def sql_start():
    if base:
        print('Connected to database')


async def sql_add_project(state):
    async with state.proxy() as data:
        pass
        # try:
        #     base.execute("INSERT INTO main_project VALUES (%s, %s, %s, %s, %s)", ('2', 'Python', 'sdf', 'ffd', 200))
        #     connection.commit()
        # except Exception as e:
        #     print(e)
        #     connection.rollback()


async def sql_read(message, state):
    async with state.proxy() as data:
        try:
            url = f"https://apicodechest.herokuapp.com/api/projects/{data['choise_lang']}/{data['choise_level']}"
            response = requests.get(url).json()
            for item in response:
                await bot.send_message(message.from_user.id,
                                           f"Level {item['level']}\n "
                                           f"{item['programming_language']}\n"
                                           f" Название проекта:\n {item['name']}\n "
                                           f"Описание:\n {item['description']}",
                                           reply_markup=kb_client)

        except Exception:
            await bot.send_message(message.from_user.id, "Проектов по заданным критериям нет", reply_markup=kb_client)


async def sql_all_projects():
    try:
        result = base.execute("SELECT * FROM main_project").fetchall()
        return result
    except:
        connection.rollback()


async def sql_delete_project(data):
    base.execute("DELETE FROM project WHERE name = ?", (data,))
    connection.commit()
