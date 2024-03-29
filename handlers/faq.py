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
        await bot.send_message(message.chat.id, "Прохождение обязательного предварительного медицинского осмотра необходимо при поступлении на направления:\n\n"
                                                "🔹 11.05.01 Радиоэлектронные системы и комплексы\n"
                                                "🔹 13.03.02, 13.04.02 Электроэнергетика и электротехника\n"
                                                "🔹 13.05.02 Специальные электромеханические системы\n"
                                                "🔹 14.03.01 Ядерная энергетика и теплофизика\n"
                                                "🔹 23.03.01, 23.04.01 Технология транспортных процессов\n\n"
                                                "Направление на обследование поступающий получает после подачи заявления.")

    if message.text == "Нужна ли справка 086-У?":
        await bot.send_message(message.chat.id, "При подаче документов в Приемную комиссию медицинские справки не требуются. Копия справки 086-у и полиса ОМС, а также сертификат о прививках могут потребоваться студенту, уже зачисленному на первый курс. На поступление наличие медицинских документов не влияет.")

    if message.text == "Сколько баллов ЕГЭ по предмету необходимо набрать, чтобы воспользоваться правом поступления «без вступительных испытаний»?":
        await bot.send_message(message.chat.id, "Необходимо сдать ЕГЭ по предмету, подтверждающему победу или занятое призовое место, на 75 баллов и выше")

    if message.text == "Если одинаковое количество баллов?":
        await bot.send_message(message.chat.id, "Приемная комиссия будет смотреть на индивидуальные достижения")

    if message.text == "Можно ли перевестись на бюджет с платного?":
        await bot.send_message(message.chat.id, "Да\n"
                                                "Перевестись можно на конкурсной основе при наличии вакантных бюджетных мест. Для перевода необходимо сдать две идущие друг за другом сессии на «хорошо» и «отлично».")

    if message.text == "Что делать если нет отчества?":
        await bot.send_message(message.chat.id, "ФИО (или отсутствие Отчества) в документах, представляемых в приемную комиссию - аттестат, диплом и другие, - должны полностью соответствовать документу, удостоверяющему личность, т.е. ПАСПОРТУ.Проверьте, чтобы во всех сопровождающих документах также отчество НЕ было вписано - должно быть ПОЛНОЕ совпадение с паспортными данными.")

    if message.text == "Имеет ли значение дата подачи заявления при одинаковых баллах?":
        await bot.send_message(message.chat.id, "Нет, дата подачи значения не имеет. Главное - придерживаться сроков подачи документов и обращать внимание на минимальные значения результатов ЕГЭ, установленных в ГУАП.")

    if message.text == "Как проходит конкурс?":
        await bot.send_message(message.chat.id, "В основном конкурс проходит по направлениям подготовки или специальностям, однако, в 2024 году также будет вестись конкурс по отдельным образовательным программам в рамках направлений подготовки 09.03.01 «Информатика и вычислительная техника» и 09.03.03 «Прикладная информатика». Обратите внимание, для разных образовательных программ данных направлений подготовки выделено разное количество мест и установлены разные минимальные баллы для поступления. Для остальных направлений и специальностей подобного разделения нет, а выбор образовательной программы внутри конкретного направления подготовки будет осуществляться уже после зачисления.")

    if message.text == "Какие есть формы обучения?":
        await bot.send_message(message.chat.id, "очное, очно-заочное, вечернее")

    if message.text == "Назад":
        await MenuStates.MAIN_MENU.set()
        await bot.send_message(message.from_user.id, "Главное меню. Выберете действие:", reply_markup=start_keyboard)

