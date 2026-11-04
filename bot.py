import os
import logging
import telebot
from telebot import types
from dotenv import load_dotenv

# Загружаем приватные переменные из .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")

if not BOT_TOKEN:
    raise ValueError("Ошибка: BOT_TOKEN не найден в .env файле!")
if not WEB_APP_URL:
    raise ValueError("Ошибка: WEB_APP_URL не найден в .env файле!")

bot = telebot.TeleBot(BOT_TOKEN)
logging.basicConfig(level=logging.INFO)

@bot.message_handler(commands=['start'])
def start_handler(message):
    keyboard = types.InlineKeyboardMarkup()
    web_app_btn = types.InlineKeyboardButton(
        text="♟️ Играть в Шахматные Задачи",
        web_app=types.WebAppInfo(url=WEB_APP_URL)
    )
    keyboard.add(web_app_btn)

    bot.send_message(
        message.chat.id,
        "Привет! Нажми кнопку ниже, чтобы открыть мини-приложение с бесконечными шахматными задачами:",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    print("Бот успешно запущен!")
    bot.infinity_polling()