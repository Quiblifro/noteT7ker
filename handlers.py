from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import kb


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение", reply_markup=kb.menu)


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}", reply_markup=kb.menu)


# from aiogram import types, F, Router
# from aiogram.types import Message
# from aiogram.filters import Command
# from userlist import Userlist
# from user import User
# from note import Event
# userlist = Userlist()
# router = Router()


# @router.message(Command("start"))
# async def start(message: types.Message):
#     user = User(message.chat.id)
#     userlist.add(user)
#     print(userlist.users)
    
#     markup = types.InlineKeyboardMarkup()
    
#     getnote_callback = lambda: getnote(message)
#     addnote_callback = lambda: addnote(message)
    
#     markup.add(types.InlineKeyboardButton('посмотреть заметки', callback_data=getnote_callback))
#     markup.add(types.InlineKeyboardButton('добавить заметку', callback_data= addnote_callback)) 
#     await message.reply('К вашим услугам:', reply_markup=markup)

# #добавление заметки
# def addnote(message):
#     bot.send_message(message.chat.id, "что вы хотите запомнить?")
#     user = userlist.get(message.chat.id)
#     content = message.text
#     user.add_event(Event(content, user.id))

# #просмотр заметок
# def getnote(message):
#     pass

# if __name__ == '__main__':
#     dp.start_polling(dp, skip_updates=True)