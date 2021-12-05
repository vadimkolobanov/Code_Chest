from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


# Это класс машины состояний, тоесь поля которые нужно вводить пользователю
class FSMAdmin(StatesGroup):
    level = State()
    language = State()
    name = State()
    description = State()


# Это функция начала ввода она вызывается по команде /предложить ( указано внизу при регистрации Хэндлера)
async def cm_start(message: types.Message):
    await FSMAdmin.level.set()
    await message.reply("Укажите уровень сложности проекта (1-5)")


# Хэндлер записывает введенный уровень
async def add_lvl(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['level'] = message.text
    await FSMAdmin.next()
    await message.reply("Введите Язык программирования")


# Хэндлер записывает введенный язык программирования
async def add_language(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['language'] = message.text
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

    async with state.proxy() as data:
        await message.reply(str(data))

    await state.finish()  # эта команда убивает машину состояний, поэтому все действия должны быть сделаны до нее


# Регистрация всех хэндлеров
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands='Предложить', state=None)
    dp.register_message_handler(add_lvl, content_types=['text'], state=FSMAdmin.level)
    dp.register_message_handler(add_language, state=FSMAdmin.language)
    dp.register_message_handler(add_name, state=FSMAdmin.name)
    dp.register_message_handler(add_description, state=FSMAdmin.description)
