from aiogram.dispatcher.filters.state import State, StatesGroup

class AutoInfo(StatesGroup):
    title = State()
    year = State ()
    price = State ()
    color = State ()
    probeg = State ()
    extra = State ()
    image = State ()
    