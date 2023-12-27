## Integration test of GAR service
Тест разработанный для проверки соответствия API контракту и качеству отклика (подсказки) от сервиса.
***
#### Содержание
* [Описание](#Описание)
* [Структура и методы](#Структура-и-методы)  
* [Структура и методы](#Структура-и-методы)  
***
#### Описание
Небольшой тест, проверяющий правильность ответа от GAR сервиса. Пока это небольшой, несколько 
неправильный (с точки зрения тест-дизайна)
автоматизированый тест на Python и pytest. Однако он еще в стадии разработки. 
***
#### Структура и методы 
Тест разработан с помощью паттерна Page Obgect и содержит тесты в файле: test_gar_api_contract.py
В папке methods находятся файлы с методами и проверками, а в data адреса.
***
#### Запуск
1. Скачать или клонировать репозиторий с помощью ```git clone```
2. Перейти в корневую папку в терминале или IDE и установить пакеты ```pip install -r requirements.txt```
3. Запустить в том же терминале ```pytest```
4. Для сообщения об ошибках использовать флажки ```pytest -v -s```