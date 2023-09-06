from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from models.user import User
from models.note import Note
from callbacks import NotesCallbackFactory
from states import NoteState, EditNoteState
import text
import asyncio
import kb
router = Router()


#starter
@router.message(Command("start"))
async def start_handler(msg: Message):
    id = msg.from_user.id
    name = msg.from_user.first_name

    user = User.get_or_none(telegram_id=id)
    if not user:
        user = User(telegram_id=id, name=name)
        user.save()

    await msg.answer(text.greet, reply_markup=kb.main_menu)


#добавление 
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


#просмотр 
@router.message(F.text == "🔎 Посмотреть заметки")
async def add_note(msg: Message, state : FSMContext):
    user_id = User.get(telegram_id = msg.from_user.id).id
    notes = Note.select().where(Note.author == user_id)
    for i, note in enumerate(notes):

        await msg.answer(f'{i+1}. {note.content}', reply_markup=kb.note_menu(note.id))
    

#редактирование
@router.callback_query(NotesCallbackFactory.filter(F.action == "edit"))
async def edit_note(query: types.CallbackQuery, callback_data: NotesCallbackFactory, state: FSMContext):
    note_id = callback_data.id
    note = Note.get_or_none(id=note_id)

    if note:
        await query.message.answer("Введите новый текст заметки:")
        await state.set_state(EditNoteState.text)
        await state.update_data(id=note_id)
        await state.update_data(message=query.message)

    else:
        await query.message.answer("Заметка не найдена.")
@router.message(EditNoteState.text)
async def edit_text(msg: types.Message, state: FSMContext):
    new_text = msg.text
    data = await state.get_data()
    id = data.get("id")
    message=data.get("message")
    note = Note.get_or_none(id=id)
    if note:
        note.content = new_text
        note.save()

        await message.edit_text(new_text, reply_markup=kb.note_menu(note.id))
        await state.clear()
    else:
        pass


#удаление
@router.callback_query(NotesCallbackFactory.filter(F.action == "remove"))
async def remove_note(query : types.CallbackQuery, callback_data: NotesCallbackFactory):
    id = callback_data.id
    note = Note.get_by_id(id)
    note.delete_instance()
    await query.message.edit_text("Заметка удалена!")