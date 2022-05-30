from aiogram.dispatcher.filters.state import State, StatesGroup


class NewBilet(StatesGroup):
    creating_0 = State()
    creating_1 = State()
    creating_2 = State()
    creating_3 = State()
    creating_4 = State()

class DeleteBilet(StatesGroup):
    deleting_0 = State()

class AddPhoto(StatesGroup):
    adding_0 = State()
    adding_1 = State()