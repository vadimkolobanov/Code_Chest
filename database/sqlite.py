import os
import random

import psycopg2
import requests
from dotenv import load_dotenv

from create_bot import bot
from keyboards import kb_client

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

connection = psycopg2.connect(user='cwipxlmngfkrtf',
                              password='9d0df424b46c906b7fc24e5d3a639a62e375299d506fe2d711d4652fc0ef4a35',
                              host='ec2-54-77-182-219.eu-west-1.compute.amazonaws.com',
                              port='5432',
                              database='dejq0an5tcejbu')

our_base = connection.cursor()


def sql_start():
    if our_base:
        print('Connected to databases')


async def sql_add_project(state):
    async with state.proxy() as data:
        post_date = {
            'name': data['name'],
            'description': data['description'],
            'level': data['level'],
            'programming_language': data['language'],
            'check': False,
            'is active': False

        }
        add_project = requests.post('https://apicodechest.herokuapp.com/api/projects/', data=post_date)
        if add_project.status_code == 201:
            print('ok')
        else:
            print('error')


async def sql_read(message, state):
    async with state.proxy() as data:
        try:
            url = f"https://apicodechest.herokuapp.com/api/projects/{data['choise_lang']}/{data['choise_level']}"
            response = requests.get(url).json()
            item = response(random.randint(0, len(response)))

            await bot.send_message(message.from_user.id,
                                   f"**Level**: {item['level']}\n "
                                   f"**{item['programming_language']}**\n"
                                   f"**Название проекта**:\n {item['name']}\n "
                                   f"**Описание**:\n {item['description']}",
                                   reply_markup=kb_client)

        except Exception:
            await bot.send_message(message.from_user.id, "Проектов по заданным критериям нет", reply_markup=kb_client)
