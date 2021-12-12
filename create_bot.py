from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from configparser import ConfigParser
from dotenv import load_dotenv

config = ConfigParser()
config.read("lang/russian.ini", encoding='utf-8')

STORAGE = MemoryStorage()
# Токен прописан в VENV, хранить его в коде - плохо.

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
bot = Bot(token=str(os.getenv('TEST_TOKEN')))
dp = Dispatcher(bot, storage=STORAGE)
