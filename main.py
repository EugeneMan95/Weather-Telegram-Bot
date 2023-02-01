"""
    This is my pet project of telegram weather bot.
    Just for fun and experience.
"""

import telegram
from telegram.ext import *
import responses as resp
import re


print('Bot started...')

with open('Telegram_API_TOKEN.txt', 'r') as telegram_token:
    TELETOKEN = telegram_token.read()


def start_command(update, context):
    update.message.reply_text('🇺🇸<b>Hello!</b>\n'
                              '🇺🇦<b>Привіт!</b>', parse_mode=telegram.ParseMode.HTML)


def help_command(update, context):
    update.message.reply_text('🇺🇸I can show the weather in the specified city. '
                              'Just indicate the city in which you want to know the weather.\n'
                              '🇺🇦Я можу показати погоду у вказаному місті. '
                              'Просто вкажи місто, в якому хочеш дізнатись погоду.')


def end_command(update, context):
    sticker_cat = open('cat_sticker.webp', 'rb')
    context.bot.send_sticker(chat_id=update.message.chat_id, sticker=sticker_cat)
    update.message.reply_text('<b>Нехай проблеми та невзгоди не роблять вам в житті погоди!\n'
                              'Бувай, не забувай!</b>', parse_mode=telegram.ParseMode.HTML)


def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))



# reply from bot message
def handle_message(update, context):
    text = str(update.message.text).lower()
    # context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    if has_cyrillic(text):
        response = resp.ukr_responses(text)
    else:
        response = resp.eng_responses(text)
    update.message.reply_text(response)


def error(update, context):
    ukr_message = 'Неправильна назва міста, спробуй ще.'
    eng_message = 'Incorrect city, try again.'
    error_message = ukr_message if has_cyrillic(update.message.text) else eng_message
    update.message.reply_text(error_message)
    print(f'Update {update} caused error {context.error}')


def main():
    updater = Updater(TELETOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('end', end_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
