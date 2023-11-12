# Предсказание поломок

Это репозиторий содержит backend-часть предсказательного сервиса

task2_catboost_best_63 - ноутбук разработки моделей


## Установка local

1. Клонируйте репозиторий:

```shell
git clone <URL-репозитория>
```

2. Перейдите в директорию проекта:

```shell
cd <директория-проекта>
```

3. Установите зависимости:

```shell
pip install -r requirements.txt
```

## Запуск

1. Запустите backend-сервер:

```shell
uvicorn app.main:app --reload
```

2. После запуска сервер будет доступен по адресу `http://localhost:8000`.
3. Документация swagger доступна по адресу `http://localhost:8000/docs/`.


## Установка docker

1. Клонируйте репозиторий:

```shell
git clone <URL-репозитория>
```

2. Перейдите в директорию проекта:

```shell
cd <директория-проекта>
```

3. Соберите докер контейнер:
```shell
docker build -t models_service .
```

4. Поднимите докер контейнер:
```shell
docker run -d -p 80:8000 models_service
```

5. Для остановки контейнера:
```shell
docker stop 'id контейнера из docker ps'
```
