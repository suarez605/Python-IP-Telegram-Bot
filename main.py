#!/bin/python3
import os
from telegram import  Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging
import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger()

TOKEN = os.getenv("TELEGRAM_TOKEN")

def get_public_ip(update: Update, callback: CallbackContext) -> None:
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code != 200:
        logger.error("Error getting the ip address from the provider.")
        update.message.reply_text("Error getting the ip address from the provider.")
    update.message.reply_text(response.json()["ip"])


def get_temperature_cpu(update: Update, callback: CallbackContext) -> None:
    process = os.popen('vcgencmd measure_temp')
    line = process.readline()
    update.message.reply_text(f"{line[4:]} C")


def main() -> None:
    """Start the bot."""

    logger.info('Starting the bot.')
    logger.info(f"TOKEN: {TOKEN}")
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    logger.info('Updater created.')
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("get_public_ip", get_public_ip))
    dispatcher.add_handler(CommandHandler("get_temperature_cpu", get_temperature_cpu))
    dispatcher.add_handler(CommandHandler("help", help))

    # Start the Bot
    updater.start_polling()
    

if __name__ == "__main__":
    if TOKEN == "ERROR" or TOKEN is None:
        logger.error("Error, telegram token is not set.")
        exit(-1)
    main()
