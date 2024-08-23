# car_filter_api

# Тестовое задание: Разработка API для сбора и фильтрации данных об автомобилях на FastAPI

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/fastapi-005571?style=for-the-badge&logo=fastapi)
![Pydantic](https://img.shields.io/badge/Pydantic-black?style=for-the-badge&logo=pydantic&logoColor=red)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-%23D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=black&logoSize=auto)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

Проект представляет собой RESTful API для сбора данных об автомобилях и реализации фильтров по различным параметрам.

<details>

<summary>
<h4>Описание задания:</h4>
</summary>

API должно поддерживать следующие функции:

1. Добавление нового автомобиля:
   - Марка
   - Модель
   - Год выпуска
   - Тип топлива (бензин, дизель, электричество, гибрид)
   - Тип КПП (механическая, автоматическая, вариатор, робот)
   - Пробег
   - Цена
2. Получение списка автомобилей с фильтрами:
   - По марке
   - По модели
   - По году выпуска
   - По типу топлива
   - По типу КПП
   - По пробегу (диапазон)
   - По цене (диапазон)
3. Получение деталей конкретного автомобиля по ID.

### Требования:

- Использовать Python и фреймворк Django или FastAPI.
- Использовать базу данных SQLite или PostgreSQL.
- Реализовать валидацию данных.
- Обеспечить обработку ошибок и возвращение соответствующих HTTP статусов.

## Доп. задание

1. Реализовать аутентификацию и авторизацию для защиты API.
2. Добавить возможность обновления и удаления автомобилей.
3. Реализовать пагинацию для списка автомобилей.
4. Предоставить документацию по API (например, с использованием Swagger).

</details>

## **Установка на локальном компьютере**

1. Клонируйте репозиторий:
   ```
   git clone git@github.com:JustLight1/car_filter_api.git
   ```
2. Установите и активируйте виртуальное окружение:
   ```
   python -m venv venv
   source venv/Scripts/activate  - для Windows
   source venv/bin/activate - для Linux
   ```
3. Установите зависимости:
   ```
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. Перейдите в папку product и выполните миграции:
   ```
   cd car_filter_api
   alembic upgrade head
   ```
5. Запустите проект:
   ```
   uvicorn app.main:app --reload
   ```

### **OpenAPI документация**

- Swagger: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

### **Примеры эндпоинтов:**

<details><summary> POST: http://127.0.0.1:8000/api/cars/  - Добавление автомобиля.</summary>

    200 OK:
    ```json
    [
        {
            "brand": "Toyota",
            "model": "Camry",
            "year": 2020,
            "fuel_type": "бензин",
            "transmission": "автоматическая",
            "mileage": 50000,
            "price": 25000
        },
    ]
    ```

</details>

<details><summary> GET: http://127.0.0.1:8000/api/cars/?brand=Toyota&model=Camry&year=2020&fuel_type=бензин&transmission=автоматическая&mileage_min=40000&mileage_max=60000&price_min=20000&price_max=30000
  - Получение списка автомобилей по фильтрам.</summary>

    200 OK:
    ```json
     [
        {
            "brand": "Toyota",
            "model": "Camry",
            "year": 2020,
            "fuel_type": "бензин",
            "transmission": "автоматическая",
            "mileage": 50000,
            "price": 25000
        },
    ]
    ```

</details>

### Технологии

- **Python**
- **FastAPI**: Веб-фреймворк для создания API на Python.
- **SQLAlchemy**: Библиотека для работы с базами данных.
- **Pydantic**: Для валидации данных и сериализации моделей.
- **Alembic**: Инструмент для управления миграциями баз данных.
- **Uvicorn**: - ASGI веб-сервер для python.

# Автор:

**Форов Александр**

[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88)
[![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)
