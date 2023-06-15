from googletrans import Translator

def translate(matn):
    translator = Translator()
    #detecting  langugae of the text
    language = translator.detect(matn).lang
    if language == 'eng':
        return translator.translate(matn, dest == 'uz').text
    else:
        return translator.translate(matn. dest == 'eng').text

