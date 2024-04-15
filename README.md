><h5> Stack:</h5>DRF<br>pyjwt<br>drf-yasg<br>gunicorn<br>django-cors-headers<br>psycopg2<br>

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Тестовое задание на должность Python Backend Developer

<H3>Описание</H3>

Тестовое задание предполагает создание сервера авторизации и новостей с комментариями и лайками на Django с использованием Django Rest Framework.


- Кастомная модель пользователя User(AbstractBaseUser,PermissionsMixin).

- CustomUserManager (BaseUserManager)

- Счетчик Like под новостью.

- Авторизация: Кастомный класс для JWT авторизации наследуемый от BaseAuthentication.


- Новости: Каждый пользователь может создавать новости, получать списки всех новостей с пагинацией, удалять и изменять свои новости. Админ может удалять и изменять любые новости.


- Комментарии: Автор может удалять комментарии к своим новостям, админ может удалять любые комментарии.


- Контейнеризация: Использование Docker-compose для контейнеризации приложения.


- Gunicorn: Использование gunicorn в качестве WSGI HTTP-сервера для развертывания приложения.


- Nginx для обработки статических файлов и обеспечения эффективной работы приложения.


- Swagger: Использование Swagger для документирования API.


- .env файл: Использование .env файла для хранения информации о подключении к базе данных.

---

<h5>Модели:</h5> Users, News, Comments.

<h5>Роуты:</h5> 

![image](https://github.com/NovaCript/ItFox_TPB/assets/114811823/c767185f-bb0d-48c3-a83f-b59c3df78a05)


  
---

<h2>Установка и запуск (Локально)</h2>

- Клонировать репозиторий:
>git clone https://github.com/NovaCript/ItFox_TPB.git

- Перейти в директорию проекта:
>cd ItFox_TPB

- Установить зависимости:
>pip install -r requirements.txt

- Запустить миграции: 
>python manage.py migrate

- Запустить сервер:
>python manage.py runserver
___

<h2>Сборка Docker образа</h2>

- Клонировать репозиторий:
>git clone https://github.com/NovaCript/ItFox_TPB.git

- Перейти в директорию проекта:
>cd ItFox_TPB

- Создать файл .env.dev:

```
DEBUG=0
SECRET_KEY=secret_key
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
POSTGRES_DB=имя_твоей_бд
POSTGRES_ENGINE=django.db.backends.postgresql
POSTGRES_USER=имя_твоего_пользователя
POSTGRES_PASSWORD=пароль_бд
POSTGRES_HOST=db
POSTGRES_PORT=5432
```
- В консоли выролните команду:

В будущем для запуска проекта --build можно не писать
>docker-compose up --build

- Откройте новую консоль, введите команду:
>docker ps

- Зайдите в контейнер с проектом Django:
>docker exec -it ItFox_TPB_web bash

- Выполните ряд команд:
```
python manage.py collectstatic
python manage.py createsuperuser
```

___

<h2>API</h2>
<h5>Для получения подробной информации о доступных API-endpoint и их
использовании, пожалуйста, обратитесь к Swagger документации.</h5>

>Локально http://127.0.0.1:8000/api/v1/swagger/

>Docker http://localhost/api/v1/swagger/


<h1>Хорошего дня! 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" 
height="32"/></h1>
