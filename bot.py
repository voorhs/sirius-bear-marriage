import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


load_dotenv()

bot = Bot(os.environ["TG_TOKEN"])
db = Dispatcher()


async def main():
    await db.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
