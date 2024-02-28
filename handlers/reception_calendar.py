from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_instance import bot
from keyboards import reception_calendar_keyboard
from states import ReceptionCalendarStates



async def reception_calendar_menu(message: types, state: FSMContext):
    await ReceptionCalendarStates.MENU.set()
    await message.answer("Выберете дейсвие:", reply_markup=reception_calendar_keyboard)


async def process_reception_calendar_menu(message: types, state: FSMContext):
    if message.text == "Дни открытых дверей":
        await bot.send_message(message.chat.id, "Дни открытых дверей")
        # прописать парсер с проверкой даты

    if message.text == "Даты проведения олимпиад":
        pass

