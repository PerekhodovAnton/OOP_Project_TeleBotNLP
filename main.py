import telebot
import time
from NLPproccessor import NLPproccessor
from units_tests import BotTestCase
from log_in_info import TOKEN


bot = telebot.TeleBot(TOKEN)

# unit tests
def run_tests():
    Result = 'Success'
    testCase = BotTestCase()
    testCase.setUp()
    testCase.test_translation()
    testCase.test_summary()
    testCase.test_genre()
    testCase.test_spellcheck()
    testCase.test_sentiment_analysis()

    if testCase.tests_passed:
        print("All tests passed successfully!")
    else:
        Result = 'Failed'
        print(f"Some tests are failed. Result = {Result}")

    return Result
    
result = run_tests()


# If tests are passed - Bot works here
if result == 'Success':

    is_started = False
    
    
    @bot.message_handler(commands=['start'])
    def hello(message):
        global is_started
        is_started = True
        name = message.from_user.first_name
        bot.send_message(message.chat.id, f"Привет, {name}!")
        time.sleep(1)
        bot.send_message(message.chat.id, f"Я бот, который предлагает NLP процессор для разных задач!")
        show_options(message.chat.id)

    @bot.message_handler(commands=['help'])
    def help(message):
        name = message.from_user.first_name
        bot.send_message(message.chat.id, f"{name}, у меня простой функционал, пиши /start !")
            

    def show_options(chat_id):
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
        btn1 = telebot.types.KeyboardButton('Перевод(any) на русский')
        btn2 = telebot.types.KeyboardButton('Перевод(ru) на английский')
        btn3 = telebot.types.KeyboardButton('Суммаризация')
        btn4 = telebot.types.KeyboardButton('Определить тематику')
        btn5 = telebot.types.KeyboardButton('Ошибки написания')
        btn6 = telebot.types.KeyboardButton('Токсичность текста')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(chat_id, "Выберите опцию:", reply_markup=markup)

    @bot.message_handler(func=lambda message: is_started)
    def process_option(message):
        global selected_option
        if message.text == 'Перевод(any) на русский':
            selected_option = 'Перевод на русский'
            bot.send_message(message.chat.id, "Введите текст для перевода:")
        elif message.text == 'Перевод(ru) на английский':
            selected_option = 'Перевод на английский'
            bot.send_message(message.chat.id, "Введите текст для перевода:")
        elif message.text == 'Суммаризация':
            selected_option = 'Суммаризация'
            bot.send_message(message.chat.id, "Введите текст для суммаризации:")
        elif message.text == 'Определить тематику':
            selected_option = 'Определить тематику'
            bot.send_message(message.chat.id, "Введите текст для определения тематики:")
        elif message.text == 'Ошибки написания':
            selected_option = 'Ошибки написания'
            bot.send_message(message.chat.id, "Введите текст для определения ошибок написания (от 5 слов):")
        elif message.text == 'Токсичность текста':
            selected_option = 'Токсичность текста'
            bot.send_message(message.chat.id, "Введите текст для определения токсичности текста:")
        else:   
            if selected_option == 'Перевод на русский':
                translations = NLPproccessor.Translation(text=message.text, source='en', target='ru')
                bot.send_message(message.chat.id, ', '.join(translations))
            if selected_option == 'Перевод на английский':
                translations = NLPproccessor.Translation(text=message.text, source='ru', target='en')
                bot.send_message(message.chat.id, ', '.join(translations))
            elif selected_option == 'Суммаризация':
                summarization = NLPproccessor.Summary(payload={"inputs": str(message.text)})
                bot.send_message(message.chat.id, summarization[0]['summary_text'])
            elif selected_option == 'Определить тематику':
                Genre = NLPproccessor.Genre(payload={"inputs": str(message.text)})
                bot.send_message(message.chat.id, str(Genre[0][0]))
            elif selected_option == 'Ошибки написания':
                Spell = NLPproccessor.SpellCheck(payload={"inputs": str(message.text)})
                bot.send_message(message.chat.id, str(Spell[0]['generated_text']))
            elif selected_option == 'Токсичность текста':
                Toxic = NLPproccessor.SentimentAnalysis(payload={"inputs": str(message.text)})
                bot.send_message(message.chat.id, str(Toxic[0]))
            selected_option = None
            show_options(message.chat.id)

    print('Bot is in progress')

    bot.polling(none_stop=True)

else:
    print(result)