from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Chelyabinsk')
b2 = KeyboardButton('Minyar')

kb_client = ReplyKeyboardMarkup()
kb_client.add(b1).add(b2)
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(b1).add(b2)