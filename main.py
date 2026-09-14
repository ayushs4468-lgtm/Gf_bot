import os, threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_USERNAME = "@Helloo_golu_bot"
custom_replies = {"love you":"love you too","miss you":"miss you too","hello":"hello jaan","babu":"haan babu","jaanu":"haan jaanu","kiss":"muahh","good morning":"good morning jaan","good night":"good night jaan"}

app_flask = Flask('')
@app_flask.route('/')
def home(): return "Bot Alive"
def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host='0.0.0.0', port=port)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text: return
    txt = update.message.text.lower()
    if BOT_USERNAME.lower() not in txt:
        if not (update.message.reply_to_message and update.message.reply_to_message.from_user.id == context.bot.id):
            return
    for k,v in custom_replies.items():
        if k in txt:
            await update.message.reply_text(v)
            return
    await update.message.reply_text("haan bolo na")

def main():
    TOKEN = os.environ.get("BOT_TOKEN")
    threading.Thread(target=run_flask, daemon=True).start()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
if __name__ == "__main__": main()
