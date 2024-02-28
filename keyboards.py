from aiogram import types

back_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_button = types.KeyboardButton("Назад")
back_keyboard.add(back_button)

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("ИИ")
button2 = types.KeyboardButton("Подача заявления")
button3 = types.KeyboardButton("Календарь приема")
button4 = types.KeyboardButton("ЕГЭ")
button5 = types.KeyboardButton("Другое")
button6 = types.KeyboardButton("FAQ")
start_keyboard.row(button1, button4, button5, button6)
start_keyboard.add(button2, button3)

submittting_aplication_keyboard = types.ReplyKeyboardMarkup()
submittting_aplication_buttons = [
    types.KeyboardButton("✏️Образцы документов для заполнения✏️"),
    types.KeyboardButton("📍Как пройти к комиссии?📍"),
    types.KeyboardButton("Дополнительные баллы при зачислении"),
    types.KeyboardButton("📞Контакты комиссии?📞"),
    types.KeyboardButton("Какие документы нужны для поступления?")
]
for button in submittting_aplication_buttons:
    submittting_aplication_keyboard.add(button)
submittting_aplication_keyboard.add(back_button)

document_examples_keyboard = types.InlineKeyboardMarkup()
document_examples_buttons = [
    types.InlineKeyboardButton("Очное", callback_data="och"),
    types.InlineKeyboardButton("Очно-заочное", callback_data="zaoch"),
    types.InlineKeyboardButton("Вечернее", callback_data="ev")
]
for button in document_examples_buttons:
    document_examples_keyboard.add(button)

reception_calendar_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
reception_calendar_buttons = [
    types.KeyboardButton("Бюджет"),
    types.KeyboardButton("Контракт"),
    types.KeyboardButton("По квоте"),
]
reception_calendar_keyboard.row(*reception_calendar_buttons)
reception_calendar_keyboard.row(types.KeyboardButton("Даты проведения олимпиад"))
reception_calendar_keyboard.row(types.KeyboardButton("Дни открытых дверей"))
reception_calendar_keyboard.add(back_button)
