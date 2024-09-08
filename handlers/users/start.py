from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart, Command
from api import ism_manosi_funksiyasi

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text=""" 🎉 Assalomu alaykum! 🎉
        Bizning botga xush kelibsiz! 🤖
        Iltimos, ismni kiriting va biz sizga kerakli ma'lumotlarni taqdim etamiz. """)
    except:
        await message.answer(text="""🎉 Assalomu alaykum! 🎉
        Bizning botga xush kelibsiz! 🤖
        Iltimos, ismni kiriting va biz sizga kerakli ma'lumotlarni taqdim etamiz.""")


@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer(""" ℹ️ **Bot Haqida** ℹ️
        Bu bot sizga ismning ma'nosini taqdim etadi. Quyidagi funksiyalarga ega:
        🔍 **Ism Ma'lumotlari** - Foydalanuvchi tomonidan kiritilgan ismning ma'nosini qidiradi va natijani taqdim etadi.
        📅 **Versiya** - 1.0
        🔧 **Yaratuvchi** - Nurbek Uktamov
        Agar botni takomillashtirish yoki qo'shimcha funktsiyalar qo'shish bo'yicha takliflaringiz bo'lsa, iltimos, biz bilan bog'laning!""")


@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer(""" 🆘 Yordam 🆘
        Bu bot sizga ismning ma'nosini taqdim etadi. Quyidagi amallarni bajaring:
        1. **Ismni kiriting** - Bot siz kiritingan ismning ma'nosini qidiradi va natijani yuboradi.
        2. **Yordam** - Botning asosiy funksiyalarini ko'rsatadi.
        Agar qo‘shimcha savollaringiz bo‘lsa, biz bilan bog‘laning! """)


@dp.message()
async def handle_message(message: Message):
    ism = message.text.strip()
    malumot = ism_manosi_funksiyasi(ism)
    
    # Yaxshi ko'rinish uchun emoji va formatlangan matn qo'shish
    await message.reply(
        f"📜 **{ism}** ismining Manosi:\n\n{malumot}\n\n🔍 Yana bir ism kiriting!",
        parse_mode='Markdown'
    )