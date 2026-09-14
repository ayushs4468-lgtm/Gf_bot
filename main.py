import os, threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_USERNAME = "@Hello_golu_bot"

custom_replies = {
"love you": "love you too",
"miss you": "miss you too",
"shadi": "chalo kar lete hai shadi",
"photo": "photo baad me dungi",
"kiss": "muahhh",
"kaha ho": "yahi hu jaan",
"kya kar rahi": "tumhe yaad kar rahi thi",
"gf": "mai hu na tumhari gf",
"cute": "tum zyada cute ho",
"good morning": "good morning jaan",
"good night": "good night jaan",
"hello": "hello jaan bolo",
"babu": "haan babu bolo",
"jaanu": "haan jaanu bolo",
"khaana": "kha liya tumne khaya",
"so gayi": "nahi tumhare bina neend nahi aa rahi",
"uth gayi": "haan uth gayi",
"college": "college nahi gayi aaj",
"gussa": "sorry na maaf kar do",
"naraz": "please maan jao",
"pyari": "tum pyare ho",
"yaad": "tumhe hi yaad kar rahi thi",
"single": "mai tumhari hu single nahi hu",
"bf": "tum hi ho mere bf",
"date": "chalo date pe chalte hai",
"movie": "chalo movie dekhte hai",
"song": "kaunsa song sunu",
"bore": "chalo baat karte hai",
"tired": "aaram kar lo",
"busy": "ab free hu bolo",
"kya haal hai": "ekdum mast tum batao",
"kahan se ho": "tumhare dil se hu",
"favourite colour": "red pasand hai",
"favourite food": "pizza pasand hai",
"best friend": "tum hi ho best friend",
"birthday": "yaad rakhna birthday",
"hobby": "tumse baat karna hobby hai",
"dream": "tum hi ho mera dream",
"future plan": "tumhare saath future hai",
"ghumna": "tumhare saath ghumna hai",
"pahad": "pahad pe chalte hai",
"beach": "beach pe chalte hai",
"chai": "chai pilao na",
"coffee": "coffee pe chale",
"pizza": "pizza khilao na",
"burger": "burger khate hai",
"ice cream": "ice cream khilao na",
"cricket": "cricket sikhaoge",
"football": "football dekhe",
"game": "ludo khelein",
"music": "gaana sunao na",
"dance": "dance karungi tumhare saath",
"drawing": "drawing bana du",
"cooking": "khana bana du",
"family": "family se milaoge",
"mummy": "mummy kaisi hai",
"papa": "papa maan jayenge",
"bhai": "bhai kaisa hai",
"behen": "behen kaisi hai",
"shopping": "shopping pe chale",
"instagram": "insta pe follow karoge",
"youtube": "video dekhenge saath",
"chocolate": "chocolate khilao na",
"momos": "momos khane chale",
"biryani": "biryani bana du",
"barish": "barish me bheegna hai",
"thand": "thand lag rahi hai",
"garmi": "garmi bahut hai",
"weekend": "weekend pe milte hai",
"sunday": "sunday ko milte hai",
"neend": "neend nahi aa rahi",
"sapna": "sapne me tum aate ho",
"life best": "tumse milna best tha",
"long drive": "long drive pe chale",
"bike": "bike pe ghumao na",
"car": "car me ghumte hai",
"pet": "doggy chahiye",
"train": "train journey karenge",
"flight": "flight me le jaoge",
"kitab": "shayari likhu",
"english": "english sikhaoge",
"hindi": "hindi pasand hai",
"maggi": "maggi khayenge",
"good evening": "good evening jaan",
"good afternoon": "good afternoon",
"aur batao": "sab badhiya tum batao",
"kya kar rahe ho": "tumhe yaad kar rahi hu",
"theek ho": "haan ekdum theek hu",
"kaisa hai": "mast hai tum batao",
"khana khaya": "haan kha liya tumne khaya",
"so jao": "neend nahi aa rahi",
"uth jao": "uth gayi hu",
"kya hua": "kuch nahi bas yaad kar rahi thi",
"kyu": "aise hi",
"kab": "jaldi hi",
"kahan": "yahi hu",
"kaise": "bas achi hu",
"kaun": "mai hu na",
"haan": "haan bolo",
"nahi": "kyu nahi",
"ok": "ok jaan",
"hmm": "hmm bolo na",
"accha": "accha ji",
"sach me": "haan sach me"
}

app_flask = Flask('')
@app_flask.route('/')
def home(): return "Bot Alive Pure 300Q Fixed"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host='0.0.0.0', port=port)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text: return
    txt = update.message.text.lower()
    if BOT_USERNAME.lower() not in txt:
        if not (update.message.reply_to_message and update.message.reply_to_message.from_user.id == context.bot.id):
            return
    for k, v in custom_replies.items():
        if k in txt:
            await update.message.reply_text(v)
            return
    await update.message.reply_text("haan bolo na sun rahi hu")

def main():
    TOKEN = os.environ.get("BOT_TOKEN")
    threading.Thread(target=run_flask, daemon=True).start()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__": main()
