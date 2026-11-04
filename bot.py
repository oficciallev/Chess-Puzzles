import os
import logging
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Загружаем приватные переменные из файла .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not WEB_APP_URL:
        await update.message.reply_text("Ошибка: WEB_APP_URL не задан в .env файле.")
        return

    keyboard = [
        [
            InlineKeyboardButton(
                text="♟️ Играть в Шахматные Задачи",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Привет! Нажми кнопку ниже, чтобы открыть мини-приложение с бесконечными шахматными задачами:",
        reply_markup=reply_markup
    )

if __name__ == '__main__':
    if not BOT_TOKEN:
        raise ValueError("Ошибка: BOT_TOKEN не найден в .env файле!")
        
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот успешно запущен...")
    app.run_polling() 