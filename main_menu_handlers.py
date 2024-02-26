# main_menu_handlers.py

from aiogram import types
from aiogram.dispatcher import FSMContext

from bot_instance import bot
from keyboards import start_keyboard, submittting_aplication_keyboard, document_examples_keyboard, back_keyboard
from states import MenuStates, SubmitttingAplicationStates, DocumentExamplesStates



# -----------------------------------------------------------------
# ГЛАВНОЕ МЕНЮ
async def send_welcome(message: types.Message, state: FSMContext):
    await MenuStates.MAIN_MENU.set()
    await message.answer("Привет! Я бот", reply_markup=start_keyboard)

async def process_menu(message: types.Message, state: FSMContext):
    if message.text == "Подача заявления":
        await MenuStates.SUBMITTING_APLICATION.set()
        await submiting_aplication_menu(message, state)
# -----------------------------------------------------------------




# -----------------------------------------------------------------
# ПОДАЧА ЗАЯВДЕНИЯ
async def submiting_aplication_menu(message: types.Message, state: FSMContext):
    await SubmitttingAplicationStates.MENU.set()
    await message.answer("Выберите действие:", reply_markup=submittting_aplication_keyboard)

async def process_submitting_aplication_menu(message: types.Message, state: FSMContext):
    if message.text == "Образцы документов для заполнения":
        await SubmitttingAplicationStates.DOCUMENT_EXAMPLES.set()
        await process_document_examples(message, state)

    if message.text == "Как пройти к комиссии?":
        await SubmitttingAplicationStates.COMMISION_WAY.set()


    if message.text == "Дополнительные баллы при зачислении":
        await SubmitttingAplicationStates.DOP_UNITS.set()


    if message.text == "Контакты комиссии?":
        await SubmitttingAplicationStates.CONTACTS.set()


    if message.text == "Какие документы нужны для поступления?":
        await SubmitttingAplicationStates.DOCUMENT_LISTS.set()

    if message.text == "Назад":
        await MenuStates.START.set()
        await send_welcome(message, state)


async def process_document_examples(message: types.Message, state: FSMContext):
    await DocumentExamplesStates.MENU.set()
    await message.reply("Выберете форму обучения:", reply_markup=document_examples_keyboard)


async def document_examples(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == "och":
        await bot.send_message(callback_query.from_user.id, "Документы об очном", reply_markup=back_keyboard)
    elif callback_query.data == "zaoch":
        await bot.send_message(callback_query.from_user.id, "Документы об очно-заочном", reply_markup=back_keyboard)
    elif callback_query.data == "ev":
        await bot.send_message(callback_query.from_user.id, "Документы об вечернем", reply_markup=back_keyboard)

async def document_examples_back(message: types, state: FSMContext):
    if message.text == "Назад":
        await MenuStates.SUBMITTING_APLICATION.set()
        await submiting_aplication_menu(message, state)
# -----------------------------------------------------------------





