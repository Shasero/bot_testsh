from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardMarkup, KeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo

main = ReplyKeyboardMarkup(keyboard=[
                            [KeyboardButton(text='Открыть веб страницу', web_app=WebAppInfo(url='https://google.com'))]], resize_keyboard=True)

