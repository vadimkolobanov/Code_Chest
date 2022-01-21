from aiogram import types, Dispatcher

from create_bot import bot
from create_bot import config
from keyboards.client_kb import kb_client


async def other_text(message: types.Message):
    await bot.send_message(message.from_user.id, config.get('RUSSIAN', 'other_messages'), reply_markup=kb_client)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(other_text)
