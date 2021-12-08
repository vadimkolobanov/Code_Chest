from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import bot
from keyboards import kb_client, kb_lvl, kb_lang
from aiogram.types import ReplyKeyboardRemove
from database import sqlite
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import config


# Машина состояний клиента
class FSMClient(StatesGroup):
    choise_level = State()
    choise_lang = State()


# Это хэндлер, он реагирует на команду /start /help и пишет привет
async def command_start(message: types.Message):
    try:

        await bot.send_message(message.from_user.id, config.get('RUSSIAN', 'hello_message'), reply_markup=kb_client)
        await message.delete()
    except Exception:
        await message.reply(config.get('RUSSIAN', 'except_message'))


# Команда получить, и старт Машины состояний. Тут указыввется с какого состояния начинать
async def command_get_project(message: types.Message):
    await FSMClient.choise_level.set()
    await bot.send_message(message.from_user.id, config.get('RUSSIAN', 'level'), reply_markup=kb_lvl)


# Выбор уровня для выборки
async def set_level(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['choise_level'] = message.text
        await FSMClient.next()
    await bot.send_message(message.from_user.id, config.get('RUSSIAN', 'prog_lang'), reply_markup=kb_lang)


# Выбор языка программирования для выборки из БД и тут же вызов функции выборки.
async def set_lang(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['choise_lang'] = message.text
    await sqlite.sql_read(message, state)
    await state.finish()


# Этот хэндлер отправляет кнопку, которая удаляет клавиатуру, и вызвать снова ее можно только через /start
async def stop_work(message: types.Message):
    await bot.send_message(message.from_user.id, config.get('RUSSIAN', 'exit_btn'), reply_markup=ReplyKeyboardRemove())


# Здесь нужно регистрировать все новые хэндлеры
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start',
                                                         'help'])  # Пример зарегистрированного хэндлера здесь указывают команды.
    dp.register_message_handler(stop_work, Text(equals=config.get('RUSSIAN', 'client_b3_text'), ignore_case=True))
    dp.register_message_handler(command_get_project,
                                Text(equals=config.get('RUSSIAN', 'client_b1_text'), ignore_case=True), state=None)
    dp.register_message_handler(set_level, state=FSMClient.choise_level)
    dp.register_message_handler(set_lang, state=FSMClient.choise_lang)
