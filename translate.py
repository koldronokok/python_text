from googletrans import Translator
import langcodes
from googletrans.models import Translated
from googletrans.urls import TRANSLATE
# Створити функцію TransLate(str, lang) для перекладу тексту. Для реалізації
# використати Google (або інші) Translation API.
transl = Translator()

print("Translate google")
def TransLate(str, lang):
    try:
        text_1='Translate: '+(transl.translate(str,dest=lang).text)
    except:
        text_1='Помилка роботи'
    return text_1
text = input("Ведіть текст який ви хочете перекласти\n text=")
lang = input("Ведіть мову на яку ви хочете поміняти(Латинськими)\n lang=")

def LangDentec(text):
    text_2="Ви надали текст з мовою : " + (transl.detect(text)).lang + " " + str(
        (transl.detect(text)).confidence * 100) + "%"
    return text_2
def CodeLang(lang):
    text_3 = "Перевело на мову : "+str(langcodes.Language.get(lang).display_name())
    return text_3
# TransLate(text,lang)
print(LangDentec(text))
print(TransLate(text,lang))
print(CodeLang(lang))