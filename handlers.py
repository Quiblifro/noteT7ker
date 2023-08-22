from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from models.user import User

import kb


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    id = msg.from_user.id
    name = msg.from_user.first_name

    user = User.get_or_none(telegram_id=id)
    if not user:
        user = User(telegram_id=id, name=name)
        user.save()

    await msg.answer("Привет! Я помогу тебе вести заметки быстро и удобно", reply_markup=kb.menu)



@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}", reply_markup=kb.menu)
