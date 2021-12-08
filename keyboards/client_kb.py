from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from create_bot import config

config.get('RUSSIAN', 'client_b1_text')
# Кнопки меню

b2 = KeyboardButton(config.get('RUSSIAN', 'client_b3_text'))
b3 = KeyboardButton(config.get('RUSSIAN', 'client_b1_text'))
b4 = KeyboardButton(config.get('RUSSIAN', 'client_b2_text'))

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b3, b4).add(b2)
