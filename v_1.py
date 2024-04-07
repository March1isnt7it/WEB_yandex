import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf'''Привет {user.mention_html()}! Я стади-бот, помогу тебе с учебой!! Пришли одну из команд ниже:
/help - список всех команд
/physics - выбрать режим физика
/algebra - выбрать режим алгебра
/geometry - выбрать режим геометрия
/english - выбрать режим английский язык''',
    )


async def help_0(update, context):
    await update.message.reply_text(rf'''Вот список всех команд:
/help - список всех команд
/phys - выбрать режим физика
/algebra - выбрать режим алгебра
/geom - выбрать режим геометрия
/english - выбрать режим английский язык''')


async def phys(update, context):
    await update.message.reply_text('coming soon...')


async def algebra(update, context):
    await update.message.reply_text('coming soon...')


async def geom(update, context):
    await update.message.reply_text('coming soon...')


async def english(update, context):
    await update.message.reply_text('coming soon...')


def main():
    application = Application.builder().token('7114097304:AAEGEa474yGqhO-M0CMM1lBjJBzIzxcrMkQ').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_0))
    application.add_handler(CommandHandler("algebra", algebra))
    application.add_handler(CommandHandler("geom", geom))
    application.add_handler(CommandHandler("phys", phys))
    application.add_handler(CommandHandler("english", english))

    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()