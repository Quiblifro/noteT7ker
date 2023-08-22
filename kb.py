from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="📝 Добавить заметку", callback_data="addnote"),
    InlineKeyboardButton(text="🔎 Посмотреть заметки", callback_data="getnote")],

]
menu = InlineKeyboardMarkup(inline_keyboard=menu)