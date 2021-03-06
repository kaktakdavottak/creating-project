# Создание проекта

## Задание

Даны готовые шаблоны и статические файлы для приложения "Карта остановок наземного городского транспорта" 
и файл с данными по автобусным остановкам, загруженный с [портала открытых данных](https://data.mos.ru/datasets/752).

Необходимо: 
1) Создать проект, добавить в него приложение. Приложение выдает по имеющемуся шаблону страницу
с маршрутами для выбора из списка и информацией об остановках выбранного маршрута.
2) Добавить команду загрузки данных по остановкам из приложенного csv-файла и загрузить эти данные.

Команды по созданию проекта и приложения, по запуску импорта - должны быть уже изучены ранее.

## Реализация

* Создадим `django` проект `project`.
* Добавим модель для хранения данных об остановках. Предлагаю создать модель `Station` с такими полями:
  - `latitude` (FloatField), 
  - `longitude` (FloatField), 
  - `routes` (ManyToManyField) - рекомендую указать `related_name="stations"` для удобства выборки по маршруту, 
  - `name` (CharField)
* Добавим модель для хранения списка маршрутов. Предлагаю создать Модель `Route` с полем:
  - `name` (CharField)
* Добавим управляющую команду `import_stations`, которая загрузит из файла `moscow_bus_stations.csv` 
  данные об остановках в таблицу `station`, а список всех наименований маршрутов в модель `Route`.
  - Нам потребуются следующие данные из csv-файла:
    - `Station.latitude` <= `Latitude_WGS84`
    - `Station.longitude` <= `Longitude_WGS84`
    - `Station.routes` <= разбираем из поля `RouteNumbers`
    - `Station.name` <= `Name`
  - При разборе поля `RouteNumbers` для заполнения моделей учтите, что оно может содержать несколько
    маршрутов, разделенных символом `;` .
  - Обработав очередной маршрут в модели `Route` (найти или создать, если его еще нет), нужно добавить его
    и в поле `Station.routes` для соответствующей остановки.
  
* Добавим `view`, который обрабатывает GET-запрос, проверяет передан ли параметр `route` и возвращает
  страницу из заполненного шаблона `stations.html`. Для заполнения потребуются:
  - список маршрутов,
  - данные по остановкам выбранного маршрута,
  - координаты центра отображаемой карты, которые можно вычислить из координат крайних остановок.

## Документация по проекту

Для запуска проекта необходимо:

Установить зависимости:
```bash
pip install -r requirements.txt
```

После создания проекта, нужно будет выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py migrate
```

* Команда для загрузки данных из csv в БД
```bash
python manage.py import_stations
```

* Команда для запуска приложения
```bash
python manage.py runserver
```

* При создании моделей или их изменении необходимо выполнить следующие команды:
```bash
python manage.py makemigrations
python manage.py migrate
```
