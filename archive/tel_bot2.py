# This program is for integrating telegram with python. This is sample two.

from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

#Add the bot token inside the below quote to get started
TOKEN: Final = ''
BOT_USERNAME: Final = '@ai_deploy_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello This Is DeepDeploy, What Do You Want To Deploy Today?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("What is this Bot about? What You Can Achieve With It?")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Post Deploy Support!")

# Responses
def handler_response(text: str) -> str:
    processed: str = text.lower()
    c = ['aws','gcp','azure']

    if 'hello' in processed:
        a = processed
        print(a)
        return 'Hey there! Lets Deploy Something! Ok?'
    elif 'hi' in processed:
        a = processed
        print(a)
        return 'Hello there! Lets Deploy Your App! Ok?'
    # if 'ok' in processed:
    #     return 'What Type Of Application Do you want to Deploy? - Compute Intensive, Memory Intensive, Balanced or Not Sure'
    # if 'Compute Intensive' or 'Memory Intensive' or 'Balanced' or 'Not Sure' in processed:
    #     return 'Which Tech Stack Are You Using - MEAN, MERN, Python, Ruby, PHP'
    # if 'MEAN' or 'MERN' or 'Python' or 'Ruby'  or 'PHP' in processed:
    #     return 'Is it a static or a dynamic website?'
    elif 'static' in processed:
        return 'What is your Code or Container Source - Github, DockerHub, or Code Commit'
    elif 'Github' or 'dockerhub' in processed:
        return 'Who is your preffered cloud provider? AWS or GCP'
    for i in c:
        if i == 'aws' or 'gcp' or 'azure' in processed:
            return 'What is your preferred CI/CD Pipeline? Jenkins or CodePipeline or GitHub Actions'
    # if 'Jenkins' or 'CodePipeline' or 'GitHub Actions' in processed:
    #     return 'What is your Number of Expected Concurrent Users per hour? 0-100 or 100-1000, 1000-100,000 or 100,000-1,000,000'
    # if 'how are you' in processed:
    #     return 'I am good! Lets Deploy Something! Ok?'
    # if 'I love python' in processed:
    #     return 'Even I! Lets Deploy Something! Ok?'
    return 'Try Again and select the precise option'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type 
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handler_response(new_text)
        else:
            return
    else:
        response: str = handler_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error (update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    # Commands
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors

    app.add_error_handler(error)

    # Polls the bot
    print("Polling...")
    app.run_polling(poll_interval=3)
