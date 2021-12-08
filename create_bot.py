from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from configparser import ConfigParser

config = ConfigParser()
config.read("lang/russian.ini", encoding='utf-8')

STORAGE = MemoryStorage()
# Токен прописан в VENV, хранить его в коде - плохо.
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=STORAGE)
