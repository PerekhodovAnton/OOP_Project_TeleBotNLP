import requests
from deep_translator import GoogleTranslator
from log_in_info import API_URL_Summary, API_URL_Genre, API_URL_Spell, API_URL_SentimentAnalysis, headers


class NLPproccessor:
    
    API_URL_Summary = API_URL_Summary
    API_URL_Genre = API_URL_Genre
    API_URL_Spell = API_URL_Spell
    API_URL_SentimentAnalysis = API_URL_SentimentAnalysis

    headers = headers

    @classmethod
    def SentimentAnalysis(cls, payload):
        response = requests.post(cls.API_URL_SentimentAnalysis, headers=cls.headers, json=payload)
        return response.json()

    @classmethod
    def Summary(cls, payload):
        response = requests.post(cls.API_URL_Summary, headers=cls.headers, json=payload)
        return response.json()
    
    @classmethod
    def Genre(cls, payload):
        response = requests.post(cls.API_URL_Genre, headers=cls.headers, json=payload)
        return response.json()
    
    @classmethod
    def SpellCheck(cls, payload):
        response = requests.post(cls.API_URL_Spell, headers=cls.headers, json=payload)
        return response.json()

    def Translation(text, source, target):

        def split_text(text, max_length):
            text_length = len(text)
            num_of_chunks = int(text_length / max_length)
            if text_length % max_length != 0:
                num_of_chunks += 1
            chunks = []
            for i in range(num_of_chunks):
                start_index = i * max_length
                end_index = min(text_length, (i + 1) * max_length)
                chunks.append(text[start_index:end_index])
                
            return chunks
        
        texts_ru = []
        for piece in split_text(text, 4000):
            texts_ru.append(GoogleTranslator(source=source, target=target).translate(piece))
        
        return texts_ru