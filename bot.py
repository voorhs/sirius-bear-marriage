import asyncio
import os
from io import BytesIO

from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from dotenv import load_dotenv

from bear_marriage.data import read_points


load_dotenv()

bot = Bot(os.environ["TG_TOKEN"])
db = Dispatcher()

user_data = {}

async def main():
    await db.start_polling(bot)


@db.message(Command(("start")))
async def send_welcome(message: Message):
    # await message.reply(message.text)
    await message.reply("Welcome to Bear Marriage Bot!!!!!!! Use /upload to upload your data")

@db.message(Command("upload"))
async def upload_instr(message: Message):
    await message.reply("You can send the file as attachment")

@db.message(lambda message: message.content_type == ContentType.DOCUMENT)
async def handle_docs(message: Message):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_content = await bot.download_file(file.file_path)

    user_data[message.from_user.id] = {
        "file": BytesIO(file_content.read()),
    }
    
    await message.reply("Data uploaded successfully!")


if __name__ == "__main__":
    asyncio.run(main())
