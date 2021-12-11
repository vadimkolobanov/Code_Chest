from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other, moderator_panel
from database import sqlite

# Здесь базовая функция, которая показывает сообщение при запуске бота в консоль.
async def on_startup(_):
    print('Start')
    sqlite.sql_start()

# Регистрация хэндлера из файла clients в папке handlers.
client.register_handlers_client(dp)  # dp - Диспетчер, обязательный аргумент для всех регистраций.
admin.register_handlers_admin(dp)
moderator_panel.register_handlers_moderator(dp)
other.register_handlers_other(dp)
# Вызов этого метода, начинает прослушивание сервера телеграм на наличие подходящих нам событий. Трогать ненужно
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
