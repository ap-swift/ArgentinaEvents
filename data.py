import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import time


# Загрузка страницы
url = "https://turismo.buenosaires.gob.ar/es/article/que-hacer-esta-semana"
response = requests.get(url)
html = response.content

def parcing():
    # Создание объекта BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    # Поиск элемента по атрибуту класса
    elements = soup.find_all(class_="evento")
    cuantity = len(elements)
    titleArray_es = []
    descriptionArray_es = []
    linkArray = []
    for item in range(cuantity):
        element_title_es = elements[item].find(class_="h3-bg", string=True).text
        element_description_es = elements[item].find_all('p')[1].text
        element_link = elements[item].find('a')['href']
        titleArray_es.append(element_title_es)
        descriptionArray_es.append(element_description_es)
        linkArray.append(element_link)
    return titleArray_es, descriptionArray_es, linkArray, cuantity

titleArray_es, descriptionArray_es, linkArray, cuantity = parcing()


# Создание объекта Translator
translator = Translator()

def translate_text(titleArray_es, descriptionArray_es, cuantity):
    titleArray_ru = []
    descriptionArray_ru = []
    titleArray_en = []
    descriptionArray_en = []
    titleArray_pt = []
    descriptionArray_pt = []
    
    for item in range(cuantity):
        titleArray_ru.append(translator.translate(titleArray_es[item], src='es', dest='ru').text)
        descriptionArray_ru.append(translator.translate(descriptionArray_es[item], src='es', dest='ru').text)

        time.sleep(10)

        titleArray_en.append(translator.translate(titleArray_es[item], src='es', dest='en').text)
        descriptionArray_en.append(translator.translate(descriptionArray_es[item], src='es', dest='en').text)

        time.sleep(10)

        titleArray_pt.append(translator.translate(titleArray_es[item], src='es', dest='pt').text)
        descriptionArray_pt.append(translator.translate(descriptionArray_es[item], src='es', dest='pt').text)

        time.sleep(10)
    
    return titleArray_ru, descriptionArray_ru, titleArray_en, descriptionArray_en, titleArray_pt, descriptionArray_pt

titleArray_ru, descriptionArray_ru, titleArray_en, descriptionArray_en, titleArray_pt, descriptionArray_pt = translate_text(titleArray_es, descriptionArray_es, cuantity)

print(titleArray_ru)
