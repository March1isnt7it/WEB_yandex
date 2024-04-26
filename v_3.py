import logging
import sys
from telegram.ext import Application, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '7114097304:AAEGEa474yGqhO-M0CMM1lBjJBzIzxcrMkQ'
URL = 'https://api.telegram.org/bot'

reply_mode = [['/theory', '/practice']]
markup_mode = ReplyKeyboardMarkup(reply_mode, one_time_keyboard=False)

reply_phys = [['/mech', '/term'],
              ['/elect']]

markup_phys = ReplyKeyboardMarkup(reply_phys, one_time_keyboard=False)

reply_algebra = [['/eq', '/func'],
                 ['/graf']]

markup_algebra = ReplyKeyboardMarkup(reply_algebra, one_time_keyboard=False)

reply_geom = [['/plain', '/stereo'],
              ['/trygon']]

markup_geom = ReplyKeyboardMarkup(reply_geom, one_time_keyboard=False)

reply_english = [['/grammar', '/lex'],
                 ['/reading']]

markup_english = ReplyKeyboardMarkup(reply_english, one_time_keyboard=False)

markup_go = ReplyKeyboardMarkup([['/go']], one_time_keyboard=False)


mode = 'не установлен'
topic = 'не установлен'


async def start(update, context):
    user = update.effective_user

    await update.message.reply_html(
        rf'''Привет {user.mention_html()}! Я стади-бот, помогу тебе с учебой!! Текущий режим: "{mode}"
Пришли одну из команд ниже:
/help - список всех команд
/phys - выбрать режим физика
/algebra - выбрать режим алгебра
/geom - выбрать режим геометрия
/english - выбрать режим английский язык''',

        reply_markup=ReplyKeyboardMarkup([['/help', '/phys', '/english'],
                  ['/algebra', '/geometry']],
                                         one_time_keyboard=True)
    )


async def help_0(update, context):
    await update.message.reply_text(f'''Вот список всех команд:
/help - список всех команд
/phys - выбрать режим физика
/algebra - выбрать режим алгебра
/geom - выбрать режим геометрия
/english - выбрать режим английский язык
/current - посмотреть текущие настройки
/clear - удалить текущие настройки''',
                                    reply_markup=ReplyKeyboardMarkup([['/help', '/phys', '/english'],
['/algebra', '/geometry']],
                                                                     one_time_keyboard=False))


async def phys(update, context):
    global mode
    mode = 'физика'

    await update.message.reply_text(f'''Вы выбрали предмет "физика", текущая тема: "{topic}". Если вы хотите сменить
тему, пришлите одну из следующих команд:
/mech - урок на тему механика
/term - урок на тему термодинамика
/elec - урок на тему электричество''',
                                    reply_markup=ReplyKeyboardMarkup([['/mech', '/term'],
                  ['/elec']], one_time_keyboard=False))


async def mech(update, context):
    global topic
    topic = 'механика'
    await update.message.reply_text(f'''Понял тебя, урок на тему {topic}!
чтобы начать, отправь команду /go''',
                                    reply_markup=markup_go)


async def term(update, context):
    global topic
    topic = 'термодинамика'
    await update.message.reply_text(f'''Понял тебя, урок на тему {topic}!
чтобы начать, отправь команду /go''',
                                    reply_markup=markup_go)


async def elec(update, context):
    global topic
    topic = 'электричество'
    await update.message.reply_text(f'''Понял тебя, урок на тему {topic}!
чтобы начать, отправь команду /go''',
                                    reply_markup=markup_go)


async def algebra(update, context):
    global mode
    mode = 'алгебра'
    await update.message.reply_text(f'''Вы выбрали предмет "алгебра", текущая тема: "{topic}". Если вы хотите сменить
        тему, пришлите одну из следующих команд:
/equ - урок на тему уравнения
/func - урок на тему функции
/graf - урок на тему графики''',
                                    reply_markup=ReplyKeyboardMarkup([['/equ', '/func'],
                                          ['/graf']],
                                     one_time_keyboard=False))


async def equ(update, context):
    global topic
    topic = 'уравнения'
    await update.message.reply_text(f'''Понял тебя, урок на тему {topic}!
чтобы начать, отправь команду /go''',
                                    reply_markup=markup_go)


async def func(update, context):
    global topic
    topic = 'функции'
    await update.message.reply_text(f'''Понял тебя, урок на тему {topic}!
чтобы начать, отправь команду /go''', reply_markup=markup_go)


async def graf(update, context):
    global topic
    topic = 'графики'
    await update.message.reply_text(f'''Понял тебя, урок на тему {topic}!
чтобы начать, отправь команду /go''', reply_markup=markup_go)


async def geom(update, context):
    global mode
    mode = 'геометрия'
    await update.message.reply_text(f'''Вы выбрали предмет "алгебра", текущая тема: "{topic}". Если вы хотите сменить
             тему, пришлите одну из следующих команд:
/plan - урок на тему планиметрия
/ster - урок на тему стереометрия
/tryg - урок на тему тригонометрия''',
                                    reply_markup=ReplyKeyboardMarkup([['/plan', '/ster'],
                                                                      ['/tryg']],
                                                                     one_time_keyboard=False))


async def plan(update, context):
    global topic
    topic = 'планиметрия'
    await update.message.reply_text(f'''Понял тебя, урок на тему {topic}!
чтобы начать, отправь команду /go''',
                                    reply_markup=markup_go)


async def ster(update, context):
    global topic
    topic = 'стереометрия'
    await update.message.reply_text(f'''Понял тебя, урок на тему {topic}!
чтобы начать, отправь команду /go''',
                                    reply_markup=markup_go)


async def tryg(update, context):
    global topic
    topic = 'тригонометрия'
    await update.message.reply_text(f'''Понял тебя, урок на тему {topic}!
чтобы начать, отправь команду /go''',
                                    reply_markup=markup_go)


async def english(update, context):
    global mode
    mode = 'английский'

    await update.message.reply_text(f'''Вы выбрали предмет "английский", текущая тема: "{topic}". Если вы хотите сменить
тему, пришлите одну из следующих команд:
/gram - урок на тему грамматика
/lex - урок на тему лексика
/rea - урок на тему чтение''',
                                    reply_markup=ReplyKeyboardMarkup([['/gram', '/lex'],
                                                                 ['/rea']],
                                                                     one_time_keyboard=False))


async def gram(update, context):
    global topic
    topic = 'грамматика'

    await update.message.reply_text(f'''Понял тебя, урок на тему {topic}!
чтобы начать, отправь команду /go''',
                                    reply_markup=markup_go)


async def lex(update, context):
    global topic
    topic = 'лексика'

    await update.message.reply_text(f'''Понял тебя, урок на тему {topic}!
чтобы начать, отправь команду /go''',
                                    reply_markup=markup_go)


async def rea(update, context):
    global topic
    topic = 'чтение'

    await update.message.reply_text(f'''Понял тебя, урок на тему {topic}!
чтобы начать, отправь команду /go''',
                                    reply_markup=markup_go)


async def current(update, context):
    await update.message.reply_text(f'''Текущий режим: {mode}
Текущая тема: {topic}''',
                                    reply_markup=ReplyKeyboardMarkup([['/help', '/phys', '/english'],
                                                                      ['/algebra', '/geometry']],
                                                                     one_time_keyboard=True))


async def go(update, context):

    await update.message.reply_text(f'Запускаю урок, предмет - {mode}, тема - {topic}')
    if mode == 'физика':

        if topic == 'механика':
            await update.message.reply_text('''Механическое движение — определение, формулы, примеры
•
Механическое движение описывает изменение положения тел в пространстве относительно других тел с течением времени.


•Для описания движения необходимы тело отсчета, система координат и часы, образующие систему отсчета.


•Кинематика отвечает на вопрос, как движется тело.


•Прямолинейное равномерное движение характеризуется постоянной скоростью.


•Векторное описание движения полезно для наглядности, но требует действий с проекциями векторов


•Равноускоренное прямолинейное движение характеризуется ускорением и
изменением скорости на равную величину за равные промежутки времени.


•Движение по вертикали является частным случаем равноускоренного движения, с ускорением свободного падения,
приблизительно равным 9,81 м/с2.

Vср = S/t
''')
            await update.message.reply_text('''Автомобиль проехал первые 100 км со скоростью 50 км/ч,
а следующие 150 км со скоростью 75 км/ч. Найдите среднюю путевую скорость автомобиля на всем протяжении пути. 
||62,5 км/ч||''')

        elif topic == 'термодинамика':

            await update.message.reply_text('''уравнение Клапейрона-Менделеева:
            PV = (m/M)*R*T
            Здесь m – масса газа, M – его молекулярная масса (находим по таблице Менделеева),
             R – универсальная газовая постоянная, равная 8,3144598(48) Дж/(моль*кг)
             Изотермический процесс протекает при постоянной температуре. Тут работает закон Бойля-Мариотта: в изотермическом процессе давление газа обратно пропорционально его объёму. В изотермическом процессе:

Изохорный процесс протекает при постоянном объеме. Для этого процесса характерен закон Шарля: При постоянном объеме давление прямо пропорционально температуре. В изохорном процессе все тепло, подведенное к газу, идет на изменение его внутренней энергии.

Изобарный процесс идет при постоянном давлении. Закон Гей-Люссака гласит, что при постоянном давлении газа его объём прямо пропорционален температуре. При изобарном процессе тепло идет как на изменение внутренней энергии, так и на совершение газом работы.

Адиабатный процесс. Адиабатный процесс – это такой процесс, который проходит без теплообмена с окружающей средой.''')

        elif topic == 'электричество':

            await update.message.reply_text('''Закон Кулона
            F = k*(q1*q2/r^2)
            
            q = I*t
            
            U = I*R''')

        else:
            await update.message.reply_text(f'''Некорректные настройки :(
            Проверьте входные данные: предмет - {mode}, тема - {topic}''')

    elif mode == 'алгебра':

        if topic == 'уравнения':
            await update.message.reply_text('''Уравнение - математическое равенство с неизвестными величинами, которые нужно найти. 

•Решение уравнения заключается в нахождении всех возможных корней или убеждении в их отсутствии. 

•Виды уравнений включают линейные и квадратные, а также другие типы, такие как кубические, уравнения четвертой степени и другие. 

•Решение простых линейных уравнений включает использование формулы и двух основных правил: переноса и деления. 

•Алгоритм решения линейных уравнений включает раскрытие скобок, группировку членов и приведение подобных членов. 

•Примеры линейных уравнений решаются с использованием описанных методов.''')

            await update.message.reply_text('''x + 3 = 5
            ||2||''')

        elif topic == 'функции':
            await update.message.reply_text('''Что такое Функция в Алгебре?

• Функция - это взаимосвязь между величинами, зависимость одной переменной от другой.

• Функция может быть определена как определенное действие над переменной или соответствие между двумя множествами.

• В математике функция может быть задана табличным, графическим, аналитическим или словесным способом.

• Табличный способ помогает быстро определить конкретные значения функции без дополнительных измерений или вычислений.

• Графический способ является самым наглядным и позволяет увидеть возрастание и убывание функции, а также наибольшие и наименьшие значения.

• Аналитический способ задания функции позволяет найти значение функции по конкретному значению аргумента.

• Функция может быть задана формулой, таблицей или графиком, каждый способ имеет свои особенности и преимущества.

''')

        elif topic == 'графики':
            await update.message.reply_text('''Что является графиком функции: y = x + 3?
            Ответ: ||прямая||''')

            await update.message.reply_text('''Что является графиком функции: y = x^2?
                        Ответ: ||парабола||''')

        else:
            await update.message.reply_text(f'''Некорректные настройки :(
            Проверьте входные данные: предмет - {mode}, тема - {topic}''')

    elif mode == 'геометрия':
        if topic == 'планиметрия':
            await update.message.reply_text('''сумма углов треугольна равна 180
            
            S = 1/2 * b * h
            
            a^2 = b^2 + c^2 - 2*b*c*cos(d)''')
            await update.message.reply_text('''сумма двух углов в треугольнике равна 150, чему равен третий угол?
            ||30||''')

        elif topic == 'стереометрия':
            await update.message.reply_text('''Стереометрия - раздел геометрии, изучающий пространственные фигуры и их свойства.

•Свойства фигур в стереометрии определяются через доказательства соответствующих теорем.

•Основные фигуры в пространстве - точка, прямая и плоскость.

•В стереометрии бесконечно много плоскостей, что требует расширения системы аксиом.

•Полная система аксиом стереометрии состоит из аксиом планиметрии и дополнительных аксиом стереометрии''')

        elif topic == 'тригонометрия':
            await update.message.reply_text('''ОТТ: sin^2(a) + cos^2(a) = 1
            tg(a) = sin(a)/cos(a)
            ctg(a) = cos(a)/sin(a)''')

            await update.message.reply_text('''Если sin(a) = 0.8, то cos(a) = ?
            ||0.6||''')

        else:
            await update.message.reply_text(f'''Некорректные настройки :(
            Проверьте входные данные: предмет - {mode}, тема - {topic}''')

    elif mode == 'английский':
        if topic == 'грамматика':
            await update.message.reply_text('''В английском языке есть три времени: настоящее, прошедшее и будущее. 

•Каждое время имеет четыре вида: Simple (Indefinite), Continuous (Progressive), Perfect и Perfect Continuous. 


•Всего получается 12 видовременных форм, из которых 6 используются активно, 3 - относительно активно, 3 - практически не используются. 


•Образуются временные формы изменением формы глагола и добавлением вспомогательных глаголов.''')

        elif topic == 'лексика':
            await update.message.reply_text('''1	adult	[ˈædʌlt]	взрослый
2	age	[eɪdʒ]	возраст
3	baby	[ˈbeɪbɪ]	малыш
4	birth	[bɜːθ]	рождение
5	boy	[bɔɪ]	мальчик
6	child	[tʃaɪld]	ребенок
7	childhood	[ˈtʃaɪldhʊd]	детство
8	girl	[ɡɜːl]	девочка
9	human	[ˈhjuːmən]	человек
10	kid	[kɪd]	ребенок
11	life	[laɪf]	жизнь
12	maiden name	[ˈmeɪdn neɪm]	девичья фамилия
13	man	[mæn]	мужчина
14	name	[neɪm]	имя
15	people	[ˈpiːpl]	люди
16	person	[ˈpɜːsn]	человек
17	personality	[ˌpɜːsəˈnæləti]	личность
18	surname	[ˈsɜːneɪm]	фамилия
19	teenager	[ˈtiːneɪdʒə(r)]	подросток
20	woman	[ˈwʊmən]	женщина
21	youth	[juːθ]	молодежь, молодость ''')

        elif topic == 'чтение':
            await update.message.reply_text('''My Wonderful Family
I live in a house near the mountains. I have two brothers and one sister, and I was born last.
My father teaches mathematics, and my mother is a nurse at a big hospital.
My brothers are very smart and work hard in school. My sister is a nervous girl, but she is very kind.
My grandmother also lives with us. She came from Italy when I was two years old.
She has grown old, but she is still very strong. She cooks the best food!

My family is very important to me. We do lots of things together.
My brothers and I like to go on long walks in the mountains. My sister likes to cook with my grandmother.
On the weekends we all play board games together. We laugh and always have a good time. I love my family very much.''')

        else:
            await update.message.reply_text(f'''Некорректные настройки :(
            Проверьте входные данные: предмет - {mode}, тема - {topic}''')

    else:
        await update.message.reply_text('Вы не установили тему, пожалуйста, сделайте это',
                                        reply_markup=ReplyKeyboardMarkup([['/help', '/phys', '/english'],
                ['/algebra', '/geometry']],
                                                                         one_time_keyboard=True))


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


async def clear(update, context):
    global mode, topic

    mode = 'не установлен'
    topic = 'не установлен'

    await update.message.reply_text('Данные очищены!!',
                                    reply_markup=ReplyKeyboardMarkup([['/help', '/phys', '/english'],
                                                                      ['/algebra', '/geometry']],
                                                                     one_time_keyboard=True))


def main():
    application = Application.builder().token('7114097304:AAEGEa474yGqhO-M0CMM1lBjJBzIzxcrMkQ').build()

    application.add_handler(CommandHandler("close", close_keyboard))

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_0))
    application.add_handler(CommandHandler("algebra", algebra))
    application.add_handler(CommandHandler("geom", geom))
    application.add_handler(CommandHandler("phys", phys))
    application.add_handler(CommandHandler("english", english))

    application.add_handler(CommandHandler("elec", elec))
    application.add_handler(CommandHandler("mech", mech))
    application.add_handler(CommandHandler("term", term))

    application.add_handler(CommandHandler("equ", equ))
    application.add_handler(CommandHandler("func", func))
    application.add_handler(CommandHandler("graf", graf))

    application.add_handler(CommandHandler("plan", plan))
    application.add_handler(CommandHandler("ster", ster))
    application.add_handler(CommandHandler("tryg", tryg))

    application.add_handler(CommandHandler("gram", gram))
    application.add_handler(CommandHandler("rea", rea))
    application.add_handler(CommandHandler("lex", lex))

    application.add_handler(CommandHandler("english", english))

    application.add_handler(CommandHandler("current", current))

    application.add_handler(CommandHandler("go", go))

    application.add_handler(CommandHandler("clear", clear))

    application.run_polling()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    main()
