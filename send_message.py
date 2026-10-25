
import asyncio
import logging
import os

from aiogram import Bot

logging.basicConfig(level=logging.INFO)


async def main():
    token = os.environ["BOT_TOKEN"]
    group_id = int(os.environ["GROUP_ID"])
    thread_id = int(os.environ["THREAD_ID"])
    time_label = os.environ["TIME_LABEL"]

    bot = Bot(token=token)
    try:
        await bot.send_message(
            chat_id=group_id,
            message_thread_id=thread_id,
            text=(
                f"📢 Трена сегодня в {time_label}!\n\n"
                "Если точно идешь — ставь реакцию на это сообщение"
            ),
        )
        logging.info("Message sent successfully")
    except Exception as e:
        logging.error(f"Ошибка при отправке: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
