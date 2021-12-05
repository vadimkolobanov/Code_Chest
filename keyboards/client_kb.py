from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Кнопки меню
b1 = KeyboardButton('/start')
b2 = KeyboardButton('/stop')
b3 = KeyboardButton('/Получить')
b4 = KeyboardButton('/Предложить')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b3, b4).add(b2)
