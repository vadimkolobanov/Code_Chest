from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import bot
from keyboards import kb_client, kb_lvl, kb_lang, kb_action

from database import sqlite

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
    await message.reply("Укажите уровень сложности проекта (1-5)", reply_markup=kb_lvl)


# Хэндлер записывает введенный уровень
async def add_lvl(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['level'] = message.text
    await FSMAdmin.next()  # перекидывает на следующую функцию, в порядке состояний в классе FSMAdmin
    await message.reply("Введите Язык программирования", reply_markup=kb_lang)


# Хэндлер записывает введенный язык программирования
async def add_language(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['language'] = message.text
        # data['user']=message.from_user.id
    await FSMAdmin.next()
    await message.reply("Введите название проекта")


# Хэндлер записывает имя проекта
async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply("Введите описание")


# Хэндлер записывает описание проекта и выводит результат
async def add_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=kb_action)


async def action_user(message: types.Message, state: FSMContext):
    if message.text == "Отправить на модерацию":

        await bot.send_message(message.from_user.id, 'Отправка на модерацию')

        await sqlite.sql_add_project(state=state)

        await bot.send_message(message.from_user.id, 'Возврат в меню', reply_markup=kb_client)
        await state.finish()
    else:
        await state.finish()  # Убивает машину состояний, обязательно иначе кнопки не обновятся
        await bot.send_message(message.from_user.id, 'Возврат в меню', reply_markup=kb_client)


# Регистрация всех хэндлеров
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands='Предложить', state=None)  # здесь должна стартовать машина состояний
    dp.register_message_handler(add_lvl, content_types=['text'], state=FSMAdmin.level)  # content_types не обязателен
    dp.register_message_handler(add_language, state=FSMAdmin.language)
    dp.register_message_handler(add_name, state=FSMAdmin.name)
    dp.register_message_handler(add_description, state=FSMAdmin.description)
    dp.register_message_handler(action_user, state=FSMAdmin.action)
