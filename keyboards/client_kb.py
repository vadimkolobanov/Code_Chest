from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/stop')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b2)
