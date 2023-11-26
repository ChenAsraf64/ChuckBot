# ChuckBot

ChuckBot is a Telegram bot that entertains users with Chuck Norris jokes. Users can set their preferred language for jokes, request jokes by number, and receive them translated into their chosen language.
![תמונה של WhatsApp‏ 2023-11-06 בשעה 14 09 19_cfdeeb1c](https://github.com/ChenAsraf64/ChuckBot/assets/92244408/8903849c-0918-44eb-9b49-ee5b6242b22b)

## Features

- Set preferred language for jokes.
- Request specific jokes by number.
- Jokes translated using an online translation service.

## Prerequisites

Before running this project, make sure you have the following installed:
- Python 3.8 or higher
- `pip` for installing Python packages.

## Installation

Clone the project to your local machine:

```bash
git clone https://github.com/ChenAsraf64/ChuckBot.git
cd ChuckBot
```

Set up a virtual environment (optional but recommended):
- `python -m venv venv`
- `source venv/bin/activate`  # For Unix or MacOS
`venv\Scripts\activate`  # For Windows

Install the required packages by running:
- `pip install -r requirements.txt`


## Configuration
To run the bot, you need to set up the following configuration:

1. Creare config.py file and fill the necessary information like this example: 
```python
# Create config.py fill and fill in the following details

# Azura translator configuration
AZURE_TRANSLATOR_KEY = 'your-azure-translator-key'
AZURE_TRANSLATOR_ENDPOINT = 'your-azure-translator-endpoint'
AZURE_TRANSLATOR_LOCATION = 'your-azure-translator-location'

# Telegram bot configuration
TELEGRAM_TOKEN = 'your-telegram-bot-token'
BOT_USERNAME = 'your-telegram-bot-username'

# Web scraper configuration (if applicable)
ZENROWS_API_KEY = 'your-zenrows-api-key'
```

2. Fill in your Telegram Bot token and username that you got from BotFather.
3. Fill in the Microsoft Azure Translator Text API key, endpoint, and location.
4. From `https://www.zenrows.com/` get your ZENROWS_API_KEY information. 


## Running the Bot
After the configuration file is set up, run your virtual environment (usually `evviorment_name`\Scripts\activate) and then you can run the bot using the following command:
`python chuckbot.py`

To interact with your bot on Telegram:
1. Open your Telegram application.
2. Use the search bar to find your bot with the username you set when you created the bot with BotFather (e.g., @YourBotUsername).
3. Start a conversation with your bot by clicking the “Start” button or sending a /start command.

This bot should now be up and running, ready to receive commands and interact with users.

Make sure to replace `chuckbot.py` with the actual entry file name if it's different in your clone.


## Usage
Users can start interacting with the bot by sending the /start command.

To set the language for jokes, users should use the /set_language command and follow the prompts.

Users can request jokes by sending a message with the number of the joke they want to hear.
