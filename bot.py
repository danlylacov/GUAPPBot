from aiogram import Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

from handlers.main_menu_handlers import *
from handlers.submtion_aplication import *
from handlers.reception_calendar import *
from handlers.other import *
from handlers.faq import *
from handlers.directions import *
from handlers.elastic_handlers import *
from handlers.EGE import process_callback

from bot_instance import bot

from bot_instance import bot



logging.basicConfig(level=logging.INFO)


dp = Dispatcher(bot, storage=MemoryStorage())

dp.register_message_handler(send_welcome, commands=['start', 'help'])
dp.register_message_handler(send_welcome)
dp.register_message_handler(process_menu, state=MenuStates.MAIN_MENU)

dp.register_message_handler(submiting_aplication_menu, state=MenuStates.SUBMITTING_APLICATION)
dp.register_message_handler(process_submitting_aplication_menu, state=SubmitttingAplicationStates.MENU)
dp.register_message_handler(process_document_examples, state=SubmitttingAplicationStates.DOCUMENT_EXAMPLES)
dp.register_callback_query_handler(document_examples, state=DocumentExamplesStates.MENU)
dp.register_message_handler(document_examples_back, state=DocumentExamplesStates.MENU)

dp.register_message_handler(process_reception_calendar_menu, state=ReceptionCalendarStates.MENU)

dp.register_message_handler(process_other_menu, state=OtherStates.MENU)
dp.register_message_handler(process_dormitories, state=OtherStates.DORMITORIES)
dp.register_message_handler(process_lgotnoe, state=OtherStates.LGOTNOE)
dp.register_message_handler(process_military, state=OtherStates.MILITARY)
dp.register_message_handler(process_military_state, state=OtherStates.MILITARY_STATE)

dp.register_message_handler(process_faq_menu, state=FAQStates.MENU)

dp.register_callback_query_handler(process_directions_menu, state=DirectonsStates.MENU)
dp.register_callback_query_handler(show_directions, state=DirectonsStates.DIRECTIONS)
dp.register_callback_query_handler(show_focus, state=DirectonsStates.FOCUS)

dp.register_message_handler(process_message, state=ElasticSearchStates.ASK_QUESTION)
dp.register_callback_query_handler(answer_question, state=ElasticSearchStates.ANSWER_QUESTION)


dp.register_callback_query_handler(process_callback, lambda query: query.data.startswith('answer_'), state=EGEStates.ASK_POINTS)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
