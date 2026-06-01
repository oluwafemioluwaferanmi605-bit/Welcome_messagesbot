import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define the /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_text = (
        "Welcome to Welcome_messagesbot.\n\n"
        "I am your personal assistant for managing tasks, tracking packages, "
        "and setting reminders right here in Telegram."
    )
    await update.message.reply_text(welcome_text)

def main() -> None:
    # Get the token from environment variables (for security on Render)
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    
    if not TOKEN:
        logger.error("No TELEGRAM_TOKEN found in environment variables!")
        return

    # Build the application
    application = Application.builder().token(TOKEN).build()

    # Register the start command
    application.add_handler(CommandHandler("start", start))

    # Start the Bot using polling
    logger.info("Bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()
