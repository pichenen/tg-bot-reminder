import asyncio
import logging
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Укажите свои данные
TOKEN = "8949593330:AAGmqKz6zd-sSI-BTP4ZkogUiwYyLoefjI0"
GROUP_ID = -1004442377674

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Функция, которая будет публиковать сообщение в группу
async def send_scheduled_message(time):
    try:
        await bot.send_message(chat_id=GROUP_ID, message_thread_id=2, text=f"📢 Трена сегодня в {time}! \n\nЕсли точно идешь - ставь реакцию на это сообщение")
        logging.info("Сообщение успешно отправлено в группу.")
    except Exception as e:
        logging.error(f"Ошибка при отправке: {e}")

async def main():

    # ПО РАСПИСАНИЮ (если бот запущен постоянно и принимает сообщения)
    # Настраиваем часовой пояс (например, Московское время)
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    # ПРИМЕРЫ НАСТРОЙКИ РАСПИСАНИЯ:
    # Вариант А: Каждый день каждую минуту:
    # scheduler.add_job(send_scheduled_message("20:00"), "cron", minute="*/1")
    # Вариант Б: Только по будням (с понедельника по пятницу) в 09:30
    # scheduler.add_job(send_scheduled_message, "cron", day_of_week="mon-fri", hour=9, minute=30)

    scheduler.add_job(send_scheduled_message, args=["19:30"], trigger="cron", day_of_week="sun,mon,fri", hour=8, minute="58")
    scheduler.add_job(send_scheduled_message, args=["20:00"], trigger="cron", day_of_week="sun,mon,fri", hour=8, minute="59")
    scheduler.start()

    # ПРОСТО ОТПРАВКА СООБЩЕНИЙ ПРИ СТАРТЕ СКРИПТА
    # await send_scheduled_message("19:30")
    # await send_scheduled_message("20:00")

    # Запуск приема сообщений (если боту также нужно отвечать на команды в группе)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
