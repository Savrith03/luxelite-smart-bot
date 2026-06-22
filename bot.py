import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# AI Knowledge Base for Luxelite Group Hospitality Properties
AI_KNOWLEDGE = {
    "booking": "You can book a room directly at Palace Gate Hotel & Resort via our website, or reply with your preferred dates, and our AI will check availability.",
    "checkin": "Standard check-in time at Palace Gate Residence is 2:00 PM, and check-out is at 12:00 PM.",
    "pool": "Yes, our swimming pool at Eden Beach Resort is open daily from 6:00 AM to 10:00 PM for all in-house guests.",
    "restaurant": "Royal Dim Sum and our main restaurants open from 6:00 AM for breakfast until 11:00 PM."
}

# Intent classifier simulating Natural Language Processing (NLP)
def ai_intent_classifier(user_text: str) -> str:
    text = user_text.lower()
    if any(word in text for word in ["book", "reservation", "room", "stay", "price"]):
        return AI_KNOWLEDGE["booking"]
    elif any(word in text for word in ["check in", "check out", "time", "early"]):
        return AI_KNOWLEDGE["checkin"]
    elif any(word in text for word in ["pool", "swim", "gym", "beach"]):
        return AI_KNOWLEDGE["pool"]
    elif any(word in text for word in ["food", "restaurant", "dim sum", "eat", "breakfast"]):
        return AI_KNOWLEDGE["restaurant"]
    else:
        return "Thank you for your message. I am transferring your request to our Palace Gate Guest Service team to assist you personally right away."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Welcome to Luxelite Group Smart Guest Service. I am your AI Assistant."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ai_response = ai_intent_classifier(update.message.text)
    await update.message.reply_text(ai_response)

def main() -> None:
    # Replace with official bot token during live deployment
    application = Application.builder().token("YOUR_TELEGRAM_BOT_TOKEN").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
