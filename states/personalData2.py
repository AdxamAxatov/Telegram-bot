from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData2(StatesGroup):
    fullname = State()
    phoneNumber = State()