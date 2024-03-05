from aiogram import types
from aiogram.dispatcher import FSMContext

from bot_instance import bot
from keyboards import start_keyboard, ege_keyboard
from states import MenuStates, EGEStates



async def ask_points(message: types.Message, state: FSMContext):

    await EGEStates.ASK_POINTS.set()
    await bot.send_message(message.chat.id, "Выберите один или несколько ответов:", reply_markup=ege_keyboard)




async def process_callback(callback_query: types.CallbackQuery):
    # Получаем выбранный ответ из коллбэка
    selected_answer = callback_query.data.split('_')[1]

    # Здесь вы можете выполнить действия на основе выбора пользователя
    # Например, отправить сообщение о том, что ответ выбран
    await bot.send_message(callback_query.from_user.id, f"Вы выбрали ответ номер {selected_answer}")
