from aiogram import types, Dispatcher

from create_bot import dp
from database import sqlite


async def del_command(message: types.Message):
    lst = ['1060217483', '404447469', '781220211']
    print(message.from_user.id)
    # if str(message.from_user.id) in lst:
    #     read = await sqlite.sql_all_projects()
    #     for proj in read:
    #         await bot.send_message(message.from_user.id, proj[2], reply_markup=InlineKeyboardMarkup().add \
    #             (InlineKeyboardButton(f'Удалить {proj[2]} уровень {proj[1]}', callback_data=f'del {proj[2]}')))
    # else:
    #     await bot.send_message(message.from_user.id, 'Вам запрещен доступ')


@dp.callback_query_handler(lambda x: x.data.startswith('del '))
async def delete_project(callback_query: types.CallbackQuery):
    await sqlite.sql_delete_project(callback_query.data.replace('del ', ""))
    await callback_query.answer(text=f'Проект удален', show_alert=True)


def register_handlers_moderator(dp: Dispatcher):
    dp.register_message_handler(del_command, commands=['delete'])
