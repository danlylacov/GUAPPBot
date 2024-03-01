from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_instance import bot
from keyboards import start_keyboard, faq_keyboard
from states import MenuStates, FAQStates



async def faq_menu(message: types, state: FSMContext):
    await FAQStates.MENU.set()
    await message.answer("Выберете дейсвие:", reply_markup=faq_keyboard)


async def process_faq_menu(message: types, state: FSMContext):
    if message.text == "Нужен ли мед осмотр?":
        pass

    if message.text == "Нужна ли справка 086-У?":
        pass

    if message.text == "Сколько баллов ЕГЭ по предмету необходимо набрать, чтобы воспользоваться правом поступления «без вступительных испытаний»?":
        pass

    if message.text == "Если одинаковое количество баллов?":
        pass

    if message.text == "Можно ли перевестись на бюджет с платного?":
        pass

    if message.text == "Что делать если нет отчества?":
        pass

    if message.text == "Имеет ли значение дата подачи заявления при одинаковых баллах?":
        pass

    if message.text == "Как проходит конкурс?":
        pass

    if message.text == "Какие есть формы обучения?":
        pass

    if message.text == "Назад":
        await MenuStates.MAIN_MENU.set()
        await bot.send_message(message.from_user.id, "Главное меню. Выберете действие:", reply_markup=start_keyboard)

