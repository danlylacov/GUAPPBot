from aiogram import Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from bot_instance import bot


from main_menu_handlers import *


logging.basicConfig(level=logging.INFO)


dp = Dispatcher(bot, storage=MemoryStorage())

dp.register_message_handler(send_welcome)
dp.register_message_handler(send_welcome, commands=['start', 'help'], state=MenuStates.START)
dp.register_message_handler(process_menu, state=MenuStates.MAIN_MENU)
dp.register_message_handler(submiting_aplication_menu, state=MenuStates.SUBMITTING_APLICATION)
dp.register_message_handler(process_submitting_aplication_menu, state=SubmitttingAplicationStates.MENU)
dp.register_message_handler(process_document_examples, state=SubmitttingAplicationStates.DOCUMENT_EXAMPLES)
dp.register_callback_query_handler(document_examples, state=DocumentExamplesStates.MENU)
dp.register_message_handler(document_examples_back, state=DocumentExamplesStates.MENU)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
