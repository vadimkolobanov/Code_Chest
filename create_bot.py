from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

# Токен прописан в VENV, хранить его в коде - плохо.
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
