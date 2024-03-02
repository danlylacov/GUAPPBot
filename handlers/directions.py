from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_instance import bot
from keyboards import start_keyboard, institutes_keyboard
from states import MenuStates, DirectonsStates
from db import Institutes, Directions, Focus


async def directions_menu(message: types, state: FSMContext):
    await DirectonsStates.MENU.set()
    await message.answer("Выберете институт(факультет):", reply_markup=institutes_keyboard)


async def process_directions_menu(callback_query: types.CallbackQuery, state: FSMContext):
    instituteDB = Institutes()
    institutes_ids = instituteDB.get_ids()
    if (int(callback_query.data), ) in institutes_ids:
        await DirectonsStates.DIRECTIONS.set()
        directionDB = Directions()
        directions = directionDB.get_names_by_institute(callback_query.data)
        directions_keyboard = types.InlineKeyboardMarkup()
        for i in range(len(directions)):
            directions_keyboard.add(types.InlineKeyboardButton(directions[i][0], callback_data=f'{i+1}'))
        await bot.send_message(callback_query.from_user.id, "Выберете направление:", reply_markup=directions_keyboard)


async def show_directions(callback_query: types.CallbackQuery, state: FSMContext):
    directionsDB = Directions()
    directions = directionsDB.get_ids()
    if (int(callback_query.data), ) in directions:
        focusDB = Focus()
        focus = focusDB.get_names_by_direction(callback_query.data)
        focus_keyboard = types.InlineKeyboardMarkup()
        for i in range(len(focus)):
            focus_keyboard.add(types.InlineKeyboardButton(focus[i][0], callback_data=f'{i+1}'))
        await DirectonsStates.FOCUS.set()
        await bot.send_message(callback_query.from_user.id, "Выберете направленность:", reply_markup=focus_keyboard)


async def show_focus(callback_query: types.CallbackQuery, state: FSMContext):
    focusDB = Focus()
    focus = focusDB.get_names_by_direction(callback_query.data)
    if (int(callback_query.data), ) in focus:
        await bot.send_message(callback_query.from_user.id, )
