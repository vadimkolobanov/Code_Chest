from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from create_bot import config
# Кнопки выбора языка
lang_b1 = KeyboardButton('Python')

# Кнопки выбора уровней
lvl_buttons_1 = KeyboardButton('1')
lvl_buttons_2 = KeyboardButton('2')
lvl_buttons_3 = KeyboardButton('3')
lvl_buttons_4 = KeyboardButton('4')
lvl_buttons_5 = KeyboardButton('5')

# Кнопки действий
action_b1 = KeyboardButton(config.get('RUSSIAN', 'admin_b1_text'))
action_b2 = KeyboardButton(config.get('RUSSIAN', 'admin_b2_text'))

delete_button = InlineKeyboardButton('Удалить', callback_data='delete')

kb_lvl = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_lvl.row(lvl_buttons_1, lvl_buttons_2, lvl_buttons_3).row(lvl_buttons_4, lvl_buttons_5)

kb_lang = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_lang.add(lang_b1)

kb_action = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_action.row(action_b1, action_b2)

kb_inline_del = InlineKeyboardMarkup()
kb_inline_del.add(delete_button)
