from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sqlite3
import random

conn_theory = sqlite3.connect('theory.sql')
conn_practice = sqlite3.connect('practice.sql')
cursor_theory = conn_theory.cursor()
cursor_practice = conn_practice.cursor()


def start(update, context):
    update.message.reply_text("Привет! Какой предмет ты хочешь изучить?")
    update.message.reply_text("1. Физика\n2. Алгебра\n3. Геометрия\n4. Английский")


def choose_subject(update, context):
    subject = update.message.text.lower()
    if subject == 'физика':
        subjects = ['механика', 'термодинамика', 'электричество']
    elif subject == 'алгебра':
        subjects = ['уравнения', 'функции', 'графики']
    elif subject == 'геометрия':
        subjects = ['планиметрия', 'стереометрия', 'тригонометрия']
    elif subject == 'английский':
        subjects = ['грамматика', 'лексика', 'чтение']
    else:
        update.message.reply_text("Некорректный выбор предмета. Пожалуйста, выберите из списка.")
    return update.message.reply_text("Выбери тему:")

    for i, s in enumerate(subjects, 1):
        update.message.reply_text(f"{i}. {s}")
def choose_mode(update, context):
    chosen_subject = update.message.text
    cursor = conn_theory.execute("SELECT * FROM theory WHERE subject = ?", (chosen_subject,))
    theory_info = cursor.fetchall()
    cursor = conn_practice.execute("SELECT * FROM practice WHERE subject = ?", (chosen_subject,))
    practice_info = cursor.fetchall()


    update.message.reply_text("Выбери режим:")
    update.message.reply_text("1. Теория\n2. Практика")
def handle_answer(update, context):
    chosen_mode = update.message.text
    if chosen_mode == '1':
        for row in theory_info:
            update.message.reply_text(row[2])
    elif chosen_mode == '2':
        random_practice = random.choice(practice_info)
        update.message.reply_text(random_practice[2])
    else:
        update.message.reply_text("Некорректный выбор режима. Пожалуйста, выберите из списка.")
    return update.message.reply_text("Желаешь выбрать другую тему? (да/нет)")

def end(update, context):
    response = update.message.text.lower()
    if response == 'да':
        return start(update, context)
    elif response == 'нет':
        update.message.reply_text("Работа завершена. До свидания!")
    else:
        update.message.reply_text("Некорректный ответ. Пожалуйста, введите 'да' или 'нет'.")

def main():
    updater = Updater("YOUR_TOKEN", use_context=True)
    dp = updater.dispatcher


    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, choose_subject))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, choose_mode))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_answer))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, end))
    
    updater.start_polling()
    updater.idle()
    
    
if __name__ == 'main':
    main()
