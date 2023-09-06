from aiogram.fsm.state import StatesGroup, State

class NoteState(StatesGroup):
    text = State()

class EditNoteState(StatesGroup):
    id = State()
    text = State()
    message = State()
    