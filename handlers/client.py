from aiogram import types, Dispatcher
from create_bot import bot


# Это хэндлер, он реагирует на команду /start /help и пишет привет
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет')
        await message.delete()
    except Exception:
        await message.reply('Для общения с ботом через ЛС, необходимо ему написать')


# Здесь нужно регистрировать все новые хэндлеры
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start',
                                                         'help'])  # Пример зарегистрированного хэндлера здесь указывают команды.
