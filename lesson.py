from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from keyboard import menu, nastroyka, kontakt, otmen, next_menu, instagram, otmen1

BOT_TOKEN = "7259676590:AAFF0Ok1_am9BIQTAydElnshM-P5vxdlsFQ"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

photo = "https://avatars.mds.yandex.net/i?id=cb05b294b802c97b5693912b3014aa20f3ca6922-9065836-images-thumbs&n=13"


@dp.message_handler(commands=["start", "help"])
async def start_bot(message: types.Message):
    await message.answer(text="""Здравствуйте! Добро пожаловать в наш бот! Давайте для начала выберем язык обслуживания!

 Assalomu aleykum! Botimizga xush kelibsiz! Keling, avvaliga xizmat ko’rsatish tilini tanlab olaylik.

 Hello! Welcome to our Bot! Let's choose the language of service first""",
                         reply_markup=next_menu())


@dp.callback_query_handler()
async def callback_func(callback: types.CallbackQuery):
    if callback.data == "English 🇺🇸":
        await callback.message.answer(text="")
    elif callback.data == "Русский 🇷🇺":
        await callback.message.answer_photo(photo=photo,
                                            caption="""Добро пожаловать в "Let's Food" - бота по обслуживанию и доставке еды! Наш бот готов предложить Вам различные блюда каждый день в соответствии с меню. Работаем мы с 11:00 до 20:00, чтобы Ваш обед был вкусным и своевременным. 
Подробности о нашем меню можно узнать, следуя за нами в Instagram   @letsfood_tashkent (https://www.instagram.com/letsfood_tashkent) , для получения инструкции как пользоваться ботом нажмите /instruction
Мы готовы удовлетворить любой вкус и сделать Ваш обед незабываемым!

Также, мы рады сообщить, что при заказе более 5 порций, доставка осуществляется бесплатно! В нашем меню имеются два варианта порций: "Cет" и "Полусет". 
Стоимость порции:

"Cет" составляет 40 000, 

"Полусет" - 35 000. 

Мы гарантируем, что каждое блюдо будет свежим, вкусным и приготовлено с любовью. Ждем Вашего заказа!

Кушай вкусно, каждый день
@letsfood_bot""",
                                            reply_markup=menu())
        await callback.message.answer(text="instagram", reply_markup=instagram())
    elif callback.data == "Õzbek🇺🇿":
        await callback.message.answer(text="")


@dp.message_handler(Text(equals="Заказать 🛍"))
async def start_bot(message: types.Message):
    await message.answer(text="""Извините за неудобства, но у нас закончились обеды
Попробуйте новые вкусы уже завтра!
@letsfood_bot""")


@dp.message_handler(Text(equals="Информация ℹ️"))
async def start_bot(message: types.Message):
    await message.answer(text="""📌 Здесь вы можете найти информацию о нашем ресторане    
📞 Номер телефона: +998(90) 177-73-37
🕐 Время работы: 10:00 - 20:00
⚡️Contact: @letsfood_bot_admin 
📲 Следите за нами в социальных сетях::""",
                         reply_markup=instagram())


@dp.message_handler(Text(equals="Настройки⚙️"))
async def start_bot(message: types.Message):
    await message.answer(text="Изменить настройки", reply_markup=nastroyka())


@dp.message_handler(Text(equals="Отзыв/комментарий  📩"))
async def start_bot(message: types.Message):
    await message.answer(text="Отправьте свой отзыв", reply_markup=otmen())


@dp.message_handler(Text(equals="Отменить ❌"))
async def start_bot(message: types.Message):
    await message.answer(text="Отправьте свой отзыв", reply_markup=menu())


@dp.message_handler(Text(equals="Изменить язык🇷🇺"))
async def start_bot(message: types.Message):
    await message.answer(text="Выберите свой язык:", reply_markup=next_menu())


@dp.message_handler(Text(equals="Изменить имя✏️"))
async def start_bot(message: types.Message):
    await message.answer(text="Отправьте свой имя:", reply_markup=otmen1())


@dp.message_handler(Text(equals="Отменит"))
async def start_bot(message: types.Message):
    await message.answer(text="Оrtga", reply_markup=nastroyka())


@dp.message_handler(Text(equals="Изменить номер телефона 📱"))
async def start_bot(message: types.Message):
    await message.answer(text="""Введите свой номер телефона:
\n
Ваш текущий телефон:   998910181159""", reply_markup=kontakt())


@dp.message_handler(Text(equals="Назад ⬅"))
async def start_bot(message: types.Message):
    await message.answer(text="Отправьте свой имя:", reply_markup=nastroyka())


@dp.message_handler(Text(equals="Назад ⬅️"))
async def start_bot(message: types.Message):
    await message.answer(text="Для заказа нажмите 🛍 Заказать", reply_markup=menu())
if __name__ == '__main__':
    executor.start_polling(dp)
