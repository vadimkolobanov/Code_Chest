from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

STORAGE = MemoryStorage()
# Токен прописан в VENV, хранить его в коде - плохо.
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=STORAGE)
