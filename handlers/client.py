from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove


# Это хэндлер, он реагирует на команду /start /help и пишет привет
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет', reply_markup=kb_client)
        await message.delete()
    except Exception:
        await message.reply('Для общения с ботом через ЛС, необходимо ему написать')


# Этот хэндлер отправляет кнопку, которая удаляет клавиатуру, и вызвать ее можно только через /start
async def stop_work(message: types.Message):
    await bot.send_message(message.from_user.id, 'Работа завершена', reply_markup=ReplyKeyboardRemove())


# Здесь нужно регистрировать все новые хэндлеры
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start',
                                                         'help'])  # Пример зарегистрированного хэндлера здесь указывают команды.
    dp.register_message_handler(stop_work, commands=['stop'])
