from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_instance import bot
from keyboards import start_keyboard, institutes_keyboard
from states import MenuStates, DirectonsStates
from db import Institutes


async def directions_menu(message: types, state: FSMContext):
    await DirectonsStates.MENU.set()
    await message.answer("Выберете институт(факультет):", reply_markup=institutes_keyboard, parse_mode="HTML")


async def process_directions_menu(message: types.Message, state: FSMContext):
    instituteDB = Institutes()
    institutes = Institutes.get_names()
    if message.text in institutes:
        pass