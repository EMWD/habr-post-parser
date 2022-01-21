# Парсер контента сайтов / режим для чтения

## Задание
Написать программу, которая по переданному URL парсит веб-страницу, выделяет полезный контент и возвращает его в виде текста с шириной строки `N` символов.

## Требования
- Программа может работать в режиме скрипта, тогда параметры передаются через опции командной строки, результат выводится в консоль и/или сохраняется в файл;
- либо — в режиме web-сервиса, тогда параметры передаются через query-параметры GET запроса, а результат возращается в формате .txt.
- Если на странице сайта есть изображения, то они в зависимости от переданного параметра добавляются в текст в виде ссылок или игнорируются.
- Программа должна работать корректно на любом сайте, если же удасться добиться работы только на некоторых, то нужно приложить их список.
- Текст на выходе должен быть "читаемым" в этом режиме, основным критерием является перенос по словам в строках.
  
### Входные параметры
- URL страницы;
- ширина строки текста на выходе;
- сохранять ссылки на картинки в тексте или нет;
- сохранять результат в файл или нет (для режима скрипта).

### На выходе
- Полезный контент со страницы в виде читаемого текста.

## Опционально
- Кэширование результатов предыдущих запросов.
- Реализация дополнительной функциональности, управляемой через параметры (например: таймаут выполнения).

## Технологии
Любые, но реализация — на python3.

## Результат
Итоговый исходный код должен запускаться в docker-контейнере без дополнительных манипуляций и установок зависимостей на хостовой машине.
Еще нужна инструкция по эксплуатации: как запустить программу в режиме сервиса или как скрипт и т.д. Иными словами, не должно возникнуть вопросов при проверке.