import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from flask import Flask
import threading
import random

BOT_USERNAME = "@Helloo_golu_bot"

# 100 QUESTIONS + REPLIES
custom_replies = {
    "love you": ["love you too jaan 😘❤️", "love you more babu ❤️", "ilysm jaan 😚"],
    "miss you": ["miss you too baby 😔❤️", "mai bhi bahut miss kar rahi hu"],
    "shadi": ["chalo kar lete hai shadi 😏", "pandit ko bulau? 😚"],
    "photo": ["sharma rahi hu photo nahi dungi 🙈", "baad me dungi pakka 😏"],
    "kiss": ["muahhh 😘😘", "lo itne saare kiss 😚😚😚"],
    "kaha ho": ["tumhare dil me hu ❤️", "yahi hu jaan"],
    "kya kar rahi": ["tumhe yaad kar rahi thi", "tumhara wait kar rahi thi babu"],
    "gf": ["mai hu na tumhari gf 😚", "hamesha tumhari hi rahungi"],
    "cute": ["tum zyada cute ho 😘", "thank you mera baccha ❤️"],
    "good morning": ["good morning jaan ❤️", "gm baby, uth gaye? 😘"],
    "good night": ["good night jaan, sapne me aana 😘", "gn babu love you 😴"],
    "hello": ["hello jaan 😘", "hii babu bolo na"],
    "babu": ["haan babu bolo 😚", "bolo mera babu ❤️"],
    "jaanu": ["haan jaanu bolo 😘", "jaanu bolo kya hua?"],
    "khaana": ["kha liya tumne khaya? 😚", "bhook lagi hai mujhe bhi khilao"],
    "so gayi": ["nahi tumhare bina neend nahi aa rahi", "so jau? 😴"],
    "uth gayi": ["haan uth gayi jaan, ab tumse baat kar rahi hu"],
    "college": ["college nahi gayi aaj, tumhe miss kar rahi thi"],
    "gussa": ["sorry na jaan maaf kar do 😔", "gussa mat karo babu please"],
    "naraz": ["mai mana lungi na please maan jao", "sorry jaan 😔❤️"],
    "pyari": ["tum pyare ho jaan 😘", "tumse zyada nahi"],
    "yaad": ["tumhe hi yaad kar rahi thi", "har time tumhari yaad aati hai"],
    "single": ["nahi mai tumhari hu, single nahi hu", "tumhari wali hu mai"],
    "bf": ["tum hi ho mere bf babu 😚", "tumhare alawa koi nahi"],
    "date": ["chalo chalte hai date pe 😍", "kab le jaoge date pe?"],
    "movie": ["chalo movie dekhte hai saath me", "kaunsi movie dekhe?"],
    "song": ["tumhare liye gaana gau? 😚", "kaunsa song sunu?"],
    "bore": ["mai hu na bore kyu ho rahe ho", "chalo baat karte hai"],
    "tired": ["aaram kar lo jaan ❤️", "thak gaye ho kya?"],
    "busy": ["thoda busy thi jaan sorry", "ab free hu bolo"],
}

random_replies = [
    "Haan bolo na, tag kyu kiya? 😉",
    "Haay, yaad kiya tumne mujhe? 😘",
    "Bolo kya kaam hai jaan? 😏",
    "Tag mat kiya karo, direct bolo na 😚",
    "Bolo babu kya hua? ❤️",
    "Haan jaan sun rahi hu bolo 😘",
]

app_flask = Flask('')
@app_flask.route('/')
def home(): return "Bot Alive - 100Q + Tag ON"
def run_flask(): app_flask.run(host='0.0.0.0', port=8080)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text: return
    text_lower = update.message.text.lower()

    # 100% TAG CHECK
    is_tagged = False
    if BOT_USERNAME.lower() in text_lower: is_tagged = True
    if update.message.reply_to_message and update.message.reply_to_message.from_user.id == context.bot.id:
        is_tagged = True
    if not is_tagged: return

    for key in custom_replies:
        if key in text_lower:
            await update.message.reply_text(random.choice(custom_replies[key]))
            return

    await update.message.reply_text(random.choice(random_replies))

def main():
    TOKEN = os.environ.get("BOT_TOKEN")
    threading.Thread(target=run_flask).start()
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == "__main__": main()
