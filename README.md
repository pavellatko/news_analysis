# Telegram-бот для обсуждения новостей

# [Отчет](https://github.com/pavellatko/news_analysis/blob/master/REPORT.md)

### Проект Латышева Павла, 153 группа

## Существующие решения

Разработка чат-ботов является активно развивающейся темой. Существует большое количество эксперементальных проектов от различных компаний, таких как Google, Microsoft и других. Существуют научные работы, посвященные данной теме, например, [Building End-To-End Dialogue Systems Using Generative Hierarchical Neural Network Models](https://arxiv.org/abs/1507.04808).

## Описание проекта
Конечной целью проекта является разработка telegram-бота, предназначенного для обсужения новостей. Программа должна анализировать текст новости, выделять ее темы и главную мысль. Также программа должна быть способна поддерживать обсуждение новости на русском языке, то есть автоматически генерировать подходящие по смыслу фразы или выбирать наиболее уместную в данном контексе готовую фразу из базы. 

## Технологии
Для реализации генерации фраз будет использоваться LSTM-нейронная сеть. Для ее обучения могут использоваться фразы из комментариев к новостям, форумов и других источников. Для построения нейронной сети будет использоваться библиотека Tensorflow. Это современная библиотека с широким функционалам, позволяющая стоить нейронные сети любой сложности, с поддержкой вычислений на GPU. Для обработки текстов применяются библиотеки Pymorphy2 и Mystem. Для парсинга сайтов будет использоваться библиотека BeautifulSoap. Это библиотека для простого и быстрого парсинга веб-страниц.

## План работы
1. Изучение api Telegram.
2. Написание прототипа, способного отвечать, случайно выбирая заранее заготовленные ответы.
3. Написание парсера новостей.
4. Написание бота, способного отправлять пользователю свежие новости. (Ко второй контрольной точке)
5. Добавить возможность поддерживать диалог, используя шаблонные фразы. 
5. Написание бота, способного генерировать ответы на естественном языке.
