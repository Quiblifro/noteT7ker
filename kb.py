from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from callbacks import NotesCallbackFactory

buttons = [
    [
        KeyboardButton(text="📝 Добавить заметку"),
        KeyboardButton(text="🔎 Посмотреть заметки")
    ],
]
main_menu = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder="Выберите команду")

def note_menu(id):
    builder = InlineKeyboardBuilder()
    
    builder.button(text="✏️", callback_data=NotesCallbackFactory(action="edit", id = int(id)))
    builder.button(text="❌", callback_data=NotesCallbackFactory(action="remove", id = int(id)))

    return builder.as_markup()