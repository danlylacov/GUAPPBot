from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_instance import bot
from keyboards import reception_calendar_keyboard, start_keyboard
from states import ReceptionCalendarStates, MenuStates
from db import EnterCalendar



async def reception_calendar_menu(message: types, state: FSMContext):
    await ReceptionCalendarStates.MENU.set()
    await message.answer("Выберете дейсвие:", reply_markup=reception_calendar_keyboard)


async def process_reception_calendar_menu(message: types, state: FSMContext):
    if message.text == "Дни открытых дверей":
        await bot.send_message(message.chat.id, "Дни открытых дверей")
        # прописать парсер с проверкой даты

    if message.text == "Даты проведения олимпиад":
        pass
        # сделать парсер с оф сайта

    if message.text == "Бюджет":
        enter_calendarDB = EnterCalendar()
        calendar = enter_calendarDB.get_budget()
        result = 'Календарь приема:\n\n'
        for entry in calendar:
            if entry[0] != None or entry[1] != None:
                result += f"📅 {entry[0]} 📅\n{entry[1]}\n\n"

        await bot.send_message(message.chat.id, result)

    if message.text == "Контракт":
        enter_calendarDB = EnterCalendar()
        calendar = enter_calendarDB.get_contract()
        result = 'Календарь приема:\n\n'
        for entry in calendar:
            if entry[0] != None or entry[1] != None:
                result += f"📅 {entry[0]} 📅\n{entry[1]}\n\n"

        await bot.send_message(message.chat.id, result)

    if message.text == "По квоте":
        enter_calendarDB = EnterCalendar()
        calendar = enter_calendarDB.get_kvot()
        result = 'Календарь приема:\n\n'
        for entry in calendar:
            if entry[0] != None or entry[1] != None:
                result += f"📅 {entry[0]} 📅\n{entry[1]}\n\n"

        await bot.send_message(message.chat.id, result)



    if message.text == "Назад":
        await MenuStates.MAIN_MENU.set()
        await bot.send_message(message.from_user.id, "Главное меню. Выберете действие:", reply_markup=start_keyboard)





