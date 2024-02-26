from aiogram.dispatcher.filters.state import StatesGroup, State


class MenuStates(StatesGroup):
    START = State()
    MAIN_MENU = State()
    ML = State()
    SUBMITTING_APLICATION = State()
    CALENDAR = State()
    EGE = State()
    OTHER = State()
    FAQ = State()


class SubmitttingAplicationStates(StatesGroup):
    MENU = State()
    DOCUMENT_EXAMPLES = State()
    COMMISION_WAY = State()
    DOP_UNITS = State()
    OLIMPIADS = State()
    CONTACTS = State()
    DOCUMENT_LISTS = State()


class DocumentExamplesStates(StatesGroup):
    MENU = State()
    OCH = State()
    ZAOCH = State()
    EV = State()