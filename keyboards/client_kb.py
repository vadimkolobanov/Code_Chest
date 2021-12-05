from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Кнопки меню
b1 = KeyboardButton('/start')
b2 = KeyboardButton('/stop')
b3 = KeyboardButton('/Предложить')

# Кнопки выбора языка
lang_b1 = KeyboardButton('Python')

# Кнопки выбора уровней
lvl_buttons_1 = KeyboardButton('1')
lvl_buttons_2 = KeyboardButton('2')
lvl_buttons_3 = KeyboardButton('3')
lvl_buttons_4 = KeyboardButton('4')
lvl_buttons_5 = KeyboardButton('5')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b2).add(b3)

kb_lvl = ReplyKeyboardMarkup(resize_keyboard=True)
kb_lvl.row(lvl_buttons_1, lvl_buttons_2, lvl_buttons_3).row(lvl_buttons_4, lvl_buttons_5)
