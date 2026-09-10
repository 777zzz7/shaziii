# -*- coding: utf-8 -*-
"""
Бот-валентинка для Шасанем :)
Установка:  pip install aiogram
Запуск:     python bot.py
Перед запуском вставь токен и ссылку на мини-апп (см. README.md).
"""
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

BOT_TOKEN = "СЮДА_ТОКЕН_ОТ_BOTFATHER"          # <-- вставь токен
WEBAPP_URL = "https://ТВОЙ-ДОМЕН.github.io/miniapp/"  # <-- ссылка на index.html (обязательно HTTPS!)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(
            text="❤️ Ты сюда, любимая ❤️",
            web_app=WebAppInfo(url=WEBAPP_URL),
        )
    ]])
    await message.answer(
        "Привет, моё сердце 💌
"
        "У меня для тебя кое-что очень важное…
"
        "Нажми на кнопку ниже 👇",
        reply_markup=kb,
    )


@dp.message(F.text)
async def any_text(message: Message):
    # если она пишет что угодно — мягко возвращаем к кнопке
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="❤️ Ты сюда, любимая ❤️", web_app=WebAppInfo(url=WEBAPP_URL))
    ]])
    await message.answer("Любимая, тут всё в кнопке 👇💌", reply_markup=kb)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
