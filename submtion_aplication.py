from aiogram import types
from aiogram.dispatcher import FSMContext

from bot import dp, bot, send_welcome
from keyboards import submittting_aplication_keyboard, document_examples_keyboard, back_keyboard
from states import SubmitttingAplicationStates, MenuStates, DocumentExamplesStates


@dp.message_handler(state=MenuStates.SUBMITTING_APLICATION)
async def submiting_aplication_menu(message: types.Message, state: FSMContext):
    await SubmitttingAplicationStates.MENU.set()
    await bot.send_message(message.from_user.id, "Выберите дейсвие:", reply_markup=submittting_aplication_keyboard)


@dp.message_handler(state=SubmitttingAplicationStates.MENU)
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



@dp.message_handler(state=SubmitttingAplicationStates.DOCUMENT_EXAMPLES)
async def process_document_examples(message: types.Message, state: FSMContext):
    await DocumentExamplesStates.MENU.set()
    await bot.send_message(message.from_user.id, "Выберете форму обучения:", reply_markup=document_examples_keyboard)


@dp.callback_query_handler(state=DocumentExamplesStates.MENU)
async def document_examples(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == "och":
        await bot.send_message(callback_query.from_user.id, "Документы об очном", reply_markup=back_keyboard)
    elif callback_query.data == "zaoch":
        await bot.send_message(callback_query.from_user.id, "Документы об очно-заочном", reply_markup=back_keyboard)
    elif callback_query.data == "ev":
        await bot.send_message(callback_query.from_user.id, "Документы об вечернем", reply_markup=back_keyboard)


@dp.message_handler(state=DocumentExamplesStates.MENU)
async def document_examples_back(message: types, state: FSMContext):
    if message.text == "Назад":
        await MenuStates.SUBMITTING_APLICATION.set()
        await submiting_aplication_menu(message, state)