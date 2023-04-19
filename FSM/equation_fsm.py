from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMEquation(StatesGroup):
    first = State()
    excerpt = State()
    equation = State()
    test = State()
    last = State()
