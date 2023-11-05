# Class that represents an incoming update from Telegram to the bot every time a user interacts with him.
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from joke_extractor import extract_joke
import os
from online_translation import get_translation, get_language_code

# Token to acess HTTP API (recived from Telegram BotFather)
TOKEN = os.getenv('TELEGRAM_TOKEN')
BOT_USERNAME = os.getenv('BOT_USERNAME')
user_data = {}  # This will hold the language and joke_number for each user


# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    # Initialize user data if it doesn't exist for this user
    if user_id not in user_data:
        user_data[user_id] = {"language": None, "joke": None}

    await update.message.reply_text(
        f'Welcome to ChuckBot, {update.effective_user.first_name}! Please set your language using the /set_language command.'
    )


async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_data[user_id]["awaiting_language"] = True  # Set the flag to True
    await update.message.reply_text("Please type the language you want to set.")


# Handle incoming messages after /set_language command is called
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text  # Incomimg text from the user that need to process

    # If the user has not set a language yet
    if user_data[user_id].get("awaiting_language"):
        language_code = get_language_code(text)
        if language_code is not None:
            user_data[user_id]["language"] = language_code
            user_data[user_id]["awaiting_language"] = False  # Reset the flag
            replay_text = f"Language set to {text}. Now please send me a joke number between 1 and 101."
            replay_translate_text = get_translation(
                user_data[user_id].get("language"), replay_text)
            await update.message.reply_text(replay_translate_text)
        else:
            await update.message.reply_text("I didn't recognize that language. Please try again.")
        return

    # If the language is set, we then expect a joke number
    elif user_data[user_id].get("joke") is None:
        try:
            joke_number = int(text)
            if 1 <= joke_number <= 101:
                replay_text = f"Joke number {joke_number} was selected, please wait until i'll get this joke"
                replay_translate_text = get_translation(
                    user_data[user_id].get("language"), replay_text)
                await update.message.reply_text(replay_translate_text)
                joke_extract = extract_joke(joke_number)
                joke = get_translation(
                    user_data[user_id].get("language"), joke_extract)
                user_data[user_id]["joke"] = joke
                # Here you would call a function to get the joke and send it to the user
                await update.message.reply_text(f"{joke_number}: {joke}")

                # If the user want more jokes
                user_data[user_id]["joke"] = None  # Reset the joke state
                replay_text = "If you want another joke, just send me a new number between 1 and 101!"
                replay_translate_text = get_translation(
                    user_data[user_id].get("language"), replay_text)
                await update.message.reply_text(replay_translate_text)
            else:
                replay_text = "Please choose a number between 1 and 101."
                replay_translate_text = get_translation(
                    user_data[user_id].get("language"), replay_text)
                await update.message.reply_text(replay_translate_text)
        except ValueError:
            replay_text = "That doesn't seem like a number. Please send a number between 1 and 101."
            replay_translate_text = get_translation(
                user_data[user_id].get("language"), replay_text)
            await update.message.reply_text(replay_translate_text)


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Handler for the /start command
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Handler for the /set_language command
    set_language_handler = CommandHandler('set_language', set_language)
    application.add_handler(set_language_handler)

    # Handler for regular text messages (non-command)
    message_handler = MessageHandler(filters.TEXT, handle_message)
    application.add_handler(message_handler)

    # Start the bot's polling loop
    application.run_polling()


if __name__ == '__main__':
    main()
