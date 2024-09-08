from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer(""" ℹ️ **Bot Haqida** ℹ️
        Bu bot sizga ismning ma'nosini taqdim etadi. Quyidagi funksiyalarga ega:
        🔍 **Ism Ma'lumotlari** - Foydalanuvchi tomonidan kiritilgan ismning ma'nosini qidiradi va natijani taqdim etadi.
        📅 **Versiya** - 1.0
        🔧 **Yaratuvchi** - Nurbek Uktamov
        Agar botni takomillashtirish yoki qo'shimcha funktsiyalar qo'shish bo'yicha takliflaringiz bo'lsa, iltimos, biz bilan bog'laning!""")

