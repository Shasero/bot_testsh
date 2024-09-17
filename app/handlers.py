from aiogram import F, Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()

@router.message(CommandStart)
async def start(message: Message):
    await message.answer(f'Привет! {html.bold(message.from_user.full_name)}', reply_markup=kb.main)