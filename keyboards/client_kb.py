from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Кнопки меню
b1 = KeyboardButton('/start')
b2 = KeyboardButton('/stop')
b3 = KeyboardButton('/Предложить')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b2).add(b3)

