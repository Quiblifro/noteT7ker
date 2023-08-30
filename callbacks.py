from typing import Optional
from aiogram.filters.callback_data import CallbackData

class NotesCallbackFactory(CallbackData, prefix="note"):
    action: str
    id: int