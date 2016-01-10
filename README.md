runner
============
Многопоточный менеджер запуска приложений

Позволяет запускать приложения с заданным интервалом (в секундах).

Настройка
-----------

В каталоге "tasks" хранятся настройки для запуска приложений. Для каждого приложения - отдельный файл.

{
	"application": "my_example_application.exe -param1 -param2", -- путь к приложению и параметры запуска"
	"timeout": 10, -- интервал запуска, срабатывает с момента завершения предыдущего выполнения
	"note": "" -- Примечание
	"log": "mylog.log", -- Имя файла с логами (пишутся в каталог logs)
	"logging-error": 1, -- Писать в лог ошибки
	"logging-success": 0 -- Писать в лог успешные запуски
}


Запуск
-----------

runner.py


Анализ ошибок
-----------

Формат лог файла:
1 Строка - Дата/Время
2 Строка - Имя настройки
3 Строка - Статус
4 Строка - Текст