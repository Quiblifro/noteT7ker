from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from callbacks import NotesCallbackFactory

buttons = [
    [
        KeyboardButton(text="📝 Добавить заметку"),
        KeyboardButton(text="🔎 Посмотреть заметки")
    ],
]
main_menu = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder="Выберите команду")

def note_menu(id):

    buttons = [
        [
            InlineKeyboardButton(text="✏️", callback_data=NotesCallbackFactory(action="edit", id = id)),
            InlineKeyboardButton(text="❌", callback_data=NotesCallbackFactory(action="remove", id = id))
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)