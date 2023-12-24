import telebot
from NLPproccessor import NLPproccessor
from log_in_info import TOKEN

class BotTestCase:
    TOKEN = TOKEN
    tests_passed = True

    @classmethod
    def setUp(self):
        try:
            self.bot = telebot.TeleBot(self.TOKEN)
            self.bot.get_me()
            print("Setting up is good", self.bot)
        except Exception as e:
            self.tests_passed = False
            print("Setting up failed:", e)

    @classmethod
    def test_translation(self):
        test_text = "Привет, мир!"
        try:
            translations_en_ru = NLPproccessor.Translation(text=test_text, source="en", target="ru")
            translations_ru_en = NLPproccessor.Translation(text=test_text, source="ru", target="en")
            print("Translation is good", translations_en_ru, translations_ru_en)
        except Exception as e:
            self.tests_passed = False
            print("Translation test failed:", e)

    @classmethod
    def test_summary(self):
        test_text = "Привет, мир!"
        try:
            summarization = NLPproccessor.Summary(payload={"inputs": test_text})
            print("Summarization is good", summarization)
        except Exception as e:
            self.tests_passed = False
            print("Summarization test failed:", e)

    @classmethod
    def test_genre(self):
        test_text = "Привет, мир!"
        try:
            genre = NLPproccessor.Genre(payload={"inputs": test_text})
            print("Genre classification is good", genre)
        except Exception as e:
            self.tests_passed = False
            print("Genre classification test failed:", e)

    @classmethod
    def test_spellcheck(self):
        test_text = "Привед, о дивный новий мир!"
        try:
            spellcheck = NLPproccessor.SpellCheck(payload={"inputs": test_text})
            print("Spellcheck is good", spellcheck)
        except Exception as e:
            self.tests_passed = False
            print("Spellcheck test failed:", e)
            
    @classmethod
    def test_sentiment_analysis(self):
        test_text = "ну ты и гнида"
        try:
            sentiment_analysis = NLPproccessor.SentimentAnalysis(payload={"inputs": test_text})
            print("Sentiment analysis is good", sentiment_analysis)
        except Exception as e:
            self.tests_passed = False
            print("Sentiment analysis test failed:", e)


