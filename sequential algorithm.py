from requests import get   #импортируем метод get для запросов
from pymystem3 import Mystem #морфологический анализатор для русского языка
from nltk.tokenize import PunktSentenceTokenizer as PST  #Класс для выделения предложений
from nltk.tokenize import WordPunctTokenizer as WPT      #класс для разделения слов в предложении
from pymystem3 import Mystem #морфологический анализатор для русского языка

st = PST() #обозначение переменных как класс
wt = WPT() #обозначение переменных как класс


Names1 = {} #создаем словарь для имен из первого текста
Names2 = {} #создаем словарь для имен из второго текста
my_file1 = open("some1.txt", "r", encoding='utf-8') #открыть файл с именем some1.txt с кодировкой utf-8 на чтение
my_file2 = open("some2.txt", "r", encoding='utf-8') #открыть файл с именем some2.txt с кодировкой utf-8 на чтение
text1 = my_file1.read() #в переменную text1 запоминаем все данные из файла some1.txt
text2 = my_file2.read() #в переменную text2 запоминаем все данные из файла some2.txt

for sentence in st.sentences_from_text(text1):	#выделяем из текста1 предложение и бежим по нему
    for word in wt.tokenize(sentence):	#бежим по словам в выделенном тексте
        m = Mystem()
        analize = m.analyze(word) #Морфологический анализ слова
        for i in analize: #углубляемся в полученный словарь
            for j in i: 
                for k in i[j]:
                    for m in k:
                        if "gr" in k:
                            for o in k[m]:
                                if "муж" and "имя" in k[m]: #Проверяем есть ли параметры муж и имя
                                    if Names1.get(word) is None: #Если в словаре имен нет такого имени
                                        Names1.update({word: 1}) #добавляем его
                                    else:
                                        Names1[word] +=1 #Иначе инкрементируем индекс
                                    break #выходим из цикла разбора анализа

for sentence in st.sentences_from_text(text2):	#выделяем из текста2 предложение и бежим по нему
    for word in wt.tokenize(sentence):	#бежим по словам в выделенном тексте
        m = Mystem()
        analize = m.analyze(word) #Морфологический анализ слова
        for i in analize: #углубляемся в полученный словарь
            for j in i:
                for k in i[j]:
                    for m in k:
                        if "gr" in k:
                            for o in k[m]:
                                if "муж" and "имя" in k[m]: #Проверяем есть ли параметры муж и имя
                                    if Names2.get(word) is None: #Если в словаре имен нет такого имени
                                        Names2.update({word: 1}) #добавляем его
                                    else:
                                        Names2[word] +=1 #Ищем необходимые нам параметры
                                    break #выходим из цикла разбора анализа
print(Names1)
print(Names2)
