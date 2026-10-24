import asyncio
import logging
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Укажите свои данные
TOKEN = "7666349195:AAEs3ZxzyH5nxctodIGx_i_R-bCPTqToKVE"
GROUP_ID = -1004442377674  # СЮДА_ВСТАВЬТЕ_ID_ГРУППЫ (обязательно с минусом)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Функция, которая будет публиковать сообщение в группу
async def send_scheduled_message():
    try:
        await bot.send_message(chat_id=GROUP_ID, text="📢 Внимание! Это автоматическое сообщение в группу по расписанию.")
        logging.info("Сообщение успешно отправлено в группу.")
    except Exception as e:
        logging.error(f"Ошибка при отправке: {e}")

async def main():
    # Настраиваем часовой пояс (например, Московское время)
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    
    # ПРИМЕРЫ НАСТРОЙКИ РАСПИСАНИЯ:
    # Вариант А: Каждый день в 12:00 и 18:00
    scheduler.add_job(send_scheduled_message, "cron", hour="10,18", minute=30)
    
    # Вариант Б: Только по будням (с понедельника по пятницу) в 09:30
    # scheduler.add_job(send_scheduled_message, "cron", day_of_week="mon-fri", hour=9, minute=30)

    scheduler.start()
    
    # Запуск приема сообщений (если боту также нужно отвечать на команды в группе)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
