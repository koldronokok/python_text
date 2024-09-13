# give file view: file_word, file_figures, file_sentence, file_weight
# Program read text with file. Program read text stile when True all conditions()
# translate file TEXT.txt (uk->en)
# create new file and update new text in file
from pathlib import Path
from googletrans import Translator
doc = []
with open('TEXT.txt', 'r') as file:
    data = file.read()
size = Path('TEXT.txt').stat().st_size
i=0; n=0; io=0
def TransLate(str, lang):
    try:
        text_1='Translate: '+(transl.translate(str,dest=lang).text)
    except:
        text_1='Помилка роботи'
    return text_1
transl = Translator()
def LangDentec(text):
    text_2=(transl.detect(text)).lang
            #+ str((transl.detect(text)).confidence * 100) + "%")
    return text_2
figures_last=''
# get word need haven't '.' ',' '_' 'enter' + add in massif 'doc'
for figures in data:
    try:
        data[i+1]
        if (figures == '.') & (data[i + 1] != ' '):
            doc.append(data[io:i])
            io = i + 2
        elif figures == ' ':
            if (data[i - 1] == '.') | (data[i - 1] == ','):
                doc.append(data[io:i - 1])
            else:
                doc.append(data[io:i])
            io = i + 1
        i = 1 + i
    except:
        doc.append(data[io:i])
sentence = []
io=0
i=0
for figures in data:
    try:
        data[i+1]
        if (figures == '.') & (data[i + 1] != ' '):
            sentence.append(data[io:i])
            io = i + 2
        elif figures == ' ':
            if (data[i - 1] == '.'):
                sentence.append(data[io:i - 1])
                io = i + 1

        i = 1 + i
    except:
        sentence.append(data[io:i])
# give file view: word, figures, sentence, weight, langauge
file_figures=len(data)
print("Даний текст на мові ", LangDentec(data))
print("Текстовий файл важить ",size, 'байт')
print("Кількість символів ",len(data))
print("Кількість слів ", len(doc))
print("Скільки речень", len(sentence))
# Program read text with file. Program read text stile when True all conditions()
# amount sentence, word, figures
class conditions(object):
    def __init__(self, sentence=len(sentence), word=len(doc), figures=len(data)):
        self.sentence = sentence
        self.word = word
        self.figures = figures
    def main(self):
        i=0
        io=0
        textin = ""
        for figur in data:
            try:
                data[i + 1]
                if (figur == '.') & (data[i + 1] != ' '):
                    io = i + 2
                    self.sentence = self.sentence - 1
                    self.word = self.word - 1
                elif figur == ' ':
                    if data[i - 1] == '.':
                        print("",end='')
                        self.sentence = self.sentence - 1
                    elif data[i - 1] == ',':
                        print("",end='')
                    io = i + 1
                    self.word = self.word - 1
                i = 1 + i

            except:
                self.word = self.word - 1
                self.sentence = self.sentence - 1
            self.figures = self.figures - 1
            if(self.sentence ==0)|(self.figures == 0)|(self.word == 0):
                print("\nОсталось речень",self.sentence, "Осталось слів ",self.word , "Осталось символів ", self.figures)
                return textin
            textin=textin+data[i]
print("Введіть кількість потрібних речень,слів,символі хочете бачити(якщо невели, то максимальна)")
amount_sent = input("Кількість речень: ")
if amount_sent == "": amount_sent=len(sentence)
amount_wod = input("Кількість слів: ")
if amount_wod == "": amount_wod=len(doc)
amount_fig = input("Кількість символів: ")
if amount_fig == "": amount_fig=len(data)
try:
    con = conditions(int(amount_sent),int(amount_wod),int(amount_fig))
except:
    print("EROR\n Неправельно ведено")
textin = con.main()
# translate file TEXT.txt (uk->en)
lang = input("Ведіть мову на яку ви хочете поміняти(Латинськими)\n lang=")
try:
    text = TransLate(textin, lang)
except:
    print("Не вірно ведено мова")
grom = input("Надати текст?(yes/no or y/n):")
more = str(LangDentec(data)) + "->" + str(lang)
if (grom == 'yes')|(grom == 'y'):
    print(textin)
    print(more)
    text = TransLate(textin, lang)
    print(text)
# create new file and update new text in file
grm = input("Записати "+lang+" у файл?(yes/no or y/n):")
if (grm == 'yes')|(grm == 'y'):
    with open('text'+more+'.txt', 'w') as file:
        file.write(text)
    print("Виконано")
print("Програма завершеня")
