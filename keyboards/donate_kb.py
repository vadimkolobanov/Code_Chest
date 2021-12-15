from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from create_bot import config

button_donate = InlineKeyboardButton('Перевод с карты', url="http://surl.li/ayyaj")
bot_link = InlineKeyboardButton('@code_chest_bot', url="https://t.me/code_chest_bot")
bot_ds = InlineKeyboardButton('Связь с разработчиками Discord', url="https://discord.gg/XEWjcZQZ5Y")
bot_telegram = InlineKeyboardButton('Общий чат Telegram', url="https://t.me/+C03fbNGA9yI2OWIy")

kb_donate = InlineKeyboardMarkup()
kb_donate.add(button_donate).add(bot_link).add(bot_ds).add(bot_telegram)
