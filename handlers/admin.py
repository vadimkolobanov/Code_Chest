from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import bot
from create_bot import config
from database import sqlite
from keyboards import kb_client, kb_lvl, kb_lang, kb_action


# Это класс машины состояний, тоесь поля которые нужно вводить пользователю (Админ)
class FSMAdmin(StatesGroup):
    level = State()
    language = State()
    name = State()
    description = State()
    action = State()


# Это функция начала ввода она вызывается по команде /предложить ( указано внизу при регистрации Хэндлера)
async def cm_start(message: types.Message):
    await FSMAdmin.level.set()  # отсюда перекидывает в функцию, в которой state = FSMAdmin.level
    await message.reply(config.get('RUSSIAN', 'level'), reply_markup=kb_lvl)


# Хэндлер записывает введенный уровень
async def add_lvl(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['level'] = message.text
    await FSMAdmin.next()  # перекидывает на следующую функцию, в порядке состояний в классе FSMAdmin
    await message.reply(config.get('RUSSIAN', 'prog_lang'), reply_markup=kb_lang)


# Хэндлер записывает введенный язык программирования
async def add_language(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['language'] = message.text

    await FSMAdmin.next()
    await message.reply(config.get('RUSSIAN', 'add_project_name'))


# Хэндлер записывает имя проекта
async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply(config.get('RUSSIAN', 'add_description'))


# Хэндлер записывает описание проекта и выводит результат
async def add_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        data['tg_id'] = message.from_user.id
        data['username'] = message.from_user.username
    await FSMAdmin.next()
    await bot.send_message(message.from_user.id, config.get('RUSSIAN', 'get_action'), reply_markup=kb_action)


async def action_user(message: types.Message, state: FSMContext):
    if message.text == config.get('RUSSIAN', 'admin_b1_text'):

        await bot.send_message(message.from_user.id, config.get('RUSSIAN', 'admin_b1_text'))

        await sqlite.sql_add_project(state=state)

        await bot.send_message(message.from_user.id, config.get('RUSSIAN', 'back_to_menu'), reply_markup=kb_client)
        await state.finish()
    else:
        await state.finish()  # Убивает машину состояний, обязательно иначе кнопки не обновятся
        await bot.send_message(message.from_user.id, config.get('RUSSIAN', 'back_to_menu'), reply_markup=kb_client)


# Регистрация всех хэндлеров
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, Text(equals=config.get('RUSSIAN', 'client_b2_text'), ignore_case=True),
                                state=None)  # здесь должна стартовать машина состояний
    dp.register_message_handler(add_lvl, content_types=['text'], state=FSMAdmin.level)  # content_types не обязателен
    dp.register_message_handler(add_language, state=FSMAdmin.language)
    dp.register_message_handler(add_name, state=FSMAdmin.name)
    dp.register_message_handler(add_description, state=FSMAdmin.description)
    dp.register_message_handler(action_user, state=FSMAdmin.action)
