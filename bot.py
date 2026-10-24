import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "8927221526:AAGmCSUht17JBX22Krai3yTKip0f1O5kRA0"

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🏙️ Добро пожаловать в RealCity!\n\n"
        "Это твоя виртуальная жизнь.\n"
        "Твой стартовый капитал: 1 000 ₽\n\n"
        "Здесь ты сможешь покупать дома, машины, "
        "открывать бизнесы и участвовать в гонках."
    )


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())