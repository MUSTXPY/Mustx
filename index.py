from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
from telegram.ext.filters import Text
import requests

TOKEN = '7329897812:AAFRhRpqQXlQfON5MxyALmC_7Zm_ttmRtLI'

def short_link(url: str) -> str:
    tinyurl_api = "https://tinyurl.com/api-create.php"
    params = {'url': url}
    headers = {'User-Agent': "okhttp/3.9.1", 'Accept-Encoding': "gzip"}
    
    response = requests.get(tinyurl_api, params=params, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return "Failed to shorten the link. Please try again later."


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    keyboard = [
        [InlineKeyboardButton("المطور", url="https://t.me/PIlPG")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    
    await update.message.reply_text(
        "مرحبًا! أرسل لي أي رابط وسأقوم باختصاره لك. .",
        reply_markup=reply_markup
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    if user_message.startswith("http://") or user_message.startswith("https://"):
        short_url = short_link(user_message)
        await update.message.reply_text(f"الرابط الي اختصرته هو هذا :  {short_url}")
    else:
        await update.message.reply_text("الرابط مو صحيح كابتن جرب غيره او ارسل رابط  يبدأ بـ http:// أو https://")


def main() -> None:
    
    application = ApplicationBuilder().token(TOKEN).build()

    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(Text(), handle_message))

    
    application.run_polling()

if __name__ == '__main__':
    main()