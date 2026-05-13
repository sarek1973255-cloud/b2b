from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile
import asyncio

from config import BOT_TOKEN
from parser import search_companies
from excel import save_excel

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "Отправь категорию бизнеса.\n\n"
        "Например:\n"
        "автосервис Ташкент"
    )


@dp.message()
async def search(message: types.Message):

    query = message.text

    msg = await message.answer("🔍 Ищу компании...")

    data = search_companies(query)

    if not data:
        await msg.edit_text("Ничего не найдено")
        return

    file = save_excel(data)

    await msg.edit_text(f"✅ Найдено: {len(data)} компаний")

    document = FSInputFile(file)

    await message.answer_document(document)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
