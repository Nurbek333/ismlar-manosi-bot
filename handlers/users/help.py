from aiogram.types import Message
from loader import dp
from aiogram.filters import Command


#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer(""" 🆘 Yordam 🆘
        Bu bot sizga ismning ma'nosini taqdim etadi. Quyidagi amallarni bajaring:
        1. **Ismni kiriting** - Bot siz kiritingan ismning ma'nosini qidiradi va natijani yuboradi.
        2. **Yordam** - Botning asosiy funksiyalarini ko'rsatadi.
        Agar qo‘shimcha savollaringiz bo‘lsa, biz bilan bog‘laning! """)
