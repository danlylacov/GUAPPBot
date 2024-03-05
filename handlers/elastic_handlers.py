from aiogram import types
from aiogram.dispatcher import FSMContext
from elasticSearch import ElasticSearch

from bot_instance import bot
from keyboards import start_keyboard, back_keyboard
from states import MenuStates, ElasticSearchStates




ES = ElasticSearch()

async def elastic_handler(message: types, context: FSMContext):
    await ElasticSearchStates.ASK_QUESTION.set()
    await bot.send_message(message.chat.id, "❓ Напишите ваш вопрос:", reply_markup=back_keyboard)



async def process_message(message: types.Message, state: FSMContext):
    answers = ES.ask_question(message.text)
    answer_keyboard = types.InlineKeyboardMarkup()
    if message.text == "Назад":
        await MenuStates.MAIN_MENU.set()
        await bot.send_message(message.from_user.id, "Главное меню. Выберете действие:", reply_markup=start_keyboard)

    elif answers == []:
        await bot.send_message(message.from_user.id, "⛔️ Извините я не понял вопроса ⛔️\nПопробуйте еще раз!")
        await ElasticSearchStates.ASK_QUESTION.set()
        await bot.send_message(message.from_user.id, "❓ Напишите ваш вопрос:")

    else:
        answer = ''
        for i in range(len(answers)):
            answer_keyboard.add(types.InlineKeyboardButton(f"{i+1}", callback_data=f'{answers[i]}'))
            answer += f'{i+1}. {answers[i]}\n'
        await ElasticSearchStates.ANSWER_QUESTION.set()
        await bot.send_message(message.chat.id, "👉 Уточните вопрос:\n"+answer, reply_markup=answer_keyboard)


async def answer_question(callback_query: types.CallbackQuery, state: FSMContext):
    question = callback_query.data
    answer = ES.get_answer(question)
    await bot.send_message(callback_query.from_user.id, f'<b>{question}</b>\n\n{answer}', parse_mode="HTML")
    await ElasticSearchStates.ASK_QUESTION.set()
    await bot.send_message(callback_query.from_user.id, "❓ Напишите ваш вопрос:")

    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)


