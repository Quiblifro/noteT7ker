from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from models.user import User
from models.note import Note
from callbacks import NotesCallbackFactory

import asyncio

from states import NoteState


import text

import kb
#секунду
router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    id = msg.from_user.id
    name = msg.from_user.first_name

    user = User.get_or_none(telegram_id=id)
    if not user:
        user = User(telegram_id=id, name=name)
        user.save()

    await msg.answer(text.greet, reply_markup=kb.main_menu)

@router.message(F.text == "📝 Добавить заметку")
async def add_note(msg: Message, state : FSMContext):

    await msg.answer("Введите заметку:")
    await state.set_state(NoteState.text)

@router.message(NoteState.text)
async def get_text(msg : types.Message, state : FSMContext):
    await state.update_data(text = msg.text)

    user_id = User.get(telegram_id = msg.from_user.id).id
    Note.create(content=msg.text, author=user_id)

    await msg.answer("Заметка добавлена!")
    await state.clear()

@router.message(F.text == "🔎 Посмотреть заметки")
async def add_note(msg: Message, state : FSMContext):
    print("Я сюда зашел")
    user_id = User.get(telegram_id = msg.from_user.id).id
    notes = Note.select().where(Note.author == user_id)
    for i, note in enumerate(notes):

        await msg.answer(f'{i+1}. {note.content}', reply_markup=kb.note_menu(note.id))
    

@router.callback_query(NotesCallbackFactory.filter(F.action == "edit"))
async def edit_note(query : types.CallbackQuery, callback_data: NotesCallbackFactory):
    await query.message.answer(f"Редактирование заметки с id {callback_data.id}")

@router.callback_query(NotesCallbackFactory.filter(F.action == "remove"))
async def edit_note(query : types.CallbackQuery, callback_data: NotesCallbackFactory):
    await query.message.answer(f"Редактирование заметки с id {callback_data.id}")