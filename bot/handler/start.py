from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.dispacher import dp, bot
from db import *

@dp.message_handler(commands='start')
async def main_handler(msg: types.Message, state: FSMContext):
    await msg.answer(f"Assalomu alykum {msg.from_user.first_name}")
    r = qr_code_is_true(msg.text.rsplit()[1])
    if r == True:
        await state.set_state("First_name")
        await msg.answer("Ismingizni kiriting")
    else:
        await msg.answer("Bu qr code active bolgan")

@dp.message_handler(state="First_name")
async def lirst_name_check_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as storage:
        storage["first_name"] = msg.text
    await state.set_state("last_name")
    await msg.answer("Familiyangizni kiriting")

@dp.message_handler(state="last_name")
async def last_name_check_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as storage:
        storage["last_name"] = msg.text
    await state.set_state("phone")
    await msg.answer("Telefon raqamingizni kiriting")

@dp.message_handler(state="phone")
async def phone_check_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as storage:
        storage["phone"] = msg.text
    register_user(user_id=msg.from_user.id, first_name=storage.get("first_name"), last_name=storage.get("last_name"), phone=storage.get("phone"))
    await msg.answer("Siz ishtirokchi boldingiz")
