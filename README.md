# api_yatube ###### (учебный проект, не коммерческий и не рекламный продукт)

## Описание проекта

api yatube - это программный интерфейс для yatube
служит для запроса данных(примеры ниже) из проекта yatube
yatube - социальная сеть блогеров (учебный проект, не коммерческий и не рекламный продукт)


### Технологии
+ Python 3.9
+ Django 3.2
+ Django REST Framework

Автор: [Anton Bogdanov](https://github.com/Xawek/)

## Процесс развертывания

## Клонируйте репозиторий \ Clone repository

```
git clone git@github.com:Xawek/api_final_yatube.git
```

## Перейти в директорию проекта \ Go to project directory
```
cd api_final_yatube
```

## Создать и активировать виртуальное окружение \ Create and activate virtual environment


 + #### Создать \ Create
  + ##### для \ for - Windows
```
python -m venv venv
```
  + ##### для \ for - Linux
```
python3 -m venv venv
```

 + #### Активировать \ Activate
  + ##### для \ for - Windows
```
source venv/Scripts/activate
```
  + ##### для \ for - Linux
```
source venv/Bin/activate
```

## Обновить установшик пакетов \ Update pip installer
  + ##### для \ for - Windows
```
python -m pip install --upgrade pip
```
  + ##### для \ for - Linux
```
python3 -m pip install --upgrade pip
```

## Установить модули и пакеты для проекта из файла requirements.txt \ Install modules and packages for project from file requirements.txt

 + ### Установка \ Installation
  + #### для \ for - Windows
```
pip install requirements.txt
```
  + #### для \ for - Linux
```
pip install requirements.txt
```

## Перейти в директорию со скриптом управления проектом(manage.py) \ Go to the directory with the project management script(manage.py)

```
cd yatube_api
```

## Выполнить миграции \ Run migrations
 + ##### для \ for - Windows
```
python manage.py migrate
```
 + ##### для \ for - Linux
```
python3 manage.py migrate
```

## Запустить проект \ Start project
 + ##### для \ for - Windows
```
python manage.py runserver
```
 + ##### для \ for - Linux
```
python3 manage.py runserver
```
Проект будет запушен на вашем компьютере \ The project will be launched on your computer

##### Примечание \ Note

_При переходе по ссылке http://127.0.0.1:8000/ (по умолчанию) после запуска сервера, вы увидите страницу с ошибкой. Не предусмотрено графическое отображение._
_If you follow link http://127.0.0.1:8000/ (default) after starting the server, you will see an error page. Graphic display is not provided._

## Документация к API проекта Yatube (v1) \ Yatube project API documentation (v1)
http://127.0.0.1:8000/redoc/

## Остановить веб-сервер \ Stop web server
Чтобы остановить веб-сервер нажми CTRL + C — кнопки Control и C вместе (в Windows может потребоваться нажать клавиши Ctrl + Break).

To stop the web server, press CTRL + C - the Control and C buttons together (on Windows, you may need to press the Ctrl + Break keys).

# Примеры работы с api_yatube \ Examples working api_yatube

## Для не авторизованных пользователей работа API ограничена - только чтение \ For unauthorized users API operation limited - read only

+ ### Получение списка публикаций \ Getting list publications (GET):
```
http://127.0.0.1:8000/api/v1/posts/
```
+ ### Получение определённой публикации \ Get accurate publication (GET):
```
http://127.0.0.1:8000/api/v1/posts/post_id/
```
где \ where:
  + post_id - идентификатор(цифровой) запрашиваемой публикации
  + post_id - identifier (integer) requested publication

+ ### Получение комментариев публикации \ getting post comments (GET):
```
http://127.0.0.1:8000/api/v1/posts/post_id/comments/
```
где \ where:
  + post_id - идентификатор(цифровой) запрашиваемой публикации
  + post_id - identifier (integer) requested publication

+ ### Получение комментариев поста \ Getting comments post (GET):
```
http://127.0.0.1:8000/api/v1/posts/post_id/comments/comments_id
```
где \ where:
  + post_id - идентификатор(цифровой) запрашиваемой публикации
  + post_id - identifier (integer) requested publication
  + comments_id - идентификатор(цифровой) запрашиваемого комментария
  + comments_id - identifier (integer) requested commentary

+ ### Получение списка групп публикаций \ Getting publications groups list (GET):
```
http://127.0.0.1:8000/api/v1/groups/
```
+ ### Получение информации о группе публикаций \ Get information about publications in one group (GET):
```
http://127.0.0.1:8000/api/v1/groups/group_id/
```
где \ where:
  + group_id - идентификатор(PK - указывается при создании в админ-зоне) запрашиваемой группы публикаций
  + group_id - identifier (PK - specified when creating in the admin area) the requested group publications


## Для авторизованных пользователей работа API доступна в полном обьёме \ For authorized users API is available in full

+ ### создание групп \ creating a group
создание доступно через интерфейс администрирования (админ-зону Django) \ creating available through the administration interface (Django)

для создания суперпользователя выполните команду \ create superuser by command
```
python manage.py createsuperuser
```
создайте учётную запись суперпользователя \ create superuser account
##### Примечание \ Note
  + _если вы забудете имя пользователя или пароль, то при наличии доступа к серверу вы всегда можете создать нового суперпользователя_
  + _if you have forgotten your login or password and if you have access to server, you can always create new superuser_

при запушенном проекте перейдите по адресу http://127.0.0.1:8000/admin/ 
вы увидите страницу авторизации,
авторизуйтесь использовав данные указанные при создании суперпользователя,
вам станет доступна панель администрирования Django где вы можите управлять проектом в том числе станет доступно создание групп

when project is running at http://127.0.0.1:8000/admin/
you will see login page,
log in as superuser,
Django administration panel becomes available to you, where you can manage project, including creating a group becomes available

+ ### получить JWT-токен(срок активности токена по умолчанию 24 часа) \ get JWT-token (token is active by default 24 hours)
```
http://127.0.0.1:8000/api/v1/jwt/create/
```
в теле запроса передать \ in body of the request pass:
```
{
  "username": "пример/example",
  "password": "пример/example"
}
```
где в графу "пример" \ where in field "example":
  + поля "username": "пример/example" необходимо передать логин
  + in field "username": "пример/example" must contain login
  + поля "password": "пример/example" необходимо передать пароль
  + in field "username": "пример/example" must contain password

 Пример ответа \ Response Example
```
{
    "refresh": "xxxxxxxxx",
    "access": "yyyyyyyyy"
}
```
где \ where:
  + в поле "xxxxxxxxx" строки "refresh": "xxxxxxxxx" данные для обновления токена
  + in field "xxxxxxxxx" in "refresh": "xxxxxxxxx" data of update token
  + в поле "yyyyyyyyy" строки "access": "yyyyyyyyy" JWT-токен
  + in field "xxxxxxxxx" in "refresh": "xxxxxxxxx" data is token

+ ### обновить JWT-токен \ refresh JWT-token
если ваш токен утрачен, украден или каким-то иным образом скомпрометирован, вам понадобится отключить его и получить новый
if your token is lost, stolen or otherwise compromised, you will need to turn it off and get a new one

```
http://127.0.0.1:8000/api/v1/jwt/refresh/
```
в теле запроса передать \ pass in body of the request:
```
{
  "refresh": "xxxxxxxxx"
}
```
  + в поле "xxxxxxxxx" строки "refresh": "xxxxxxxxx" указать данные для обновления токена полученные ранее
  + in field "xxxxxxxxx" in "refresh": "xxxxxxxxx" data of update token (received earlier)

+ ### проверить JWT-токен \ validate JWT-token
```
http://127.0.0.1:8000/api/v1/jwt/verify/
```

+ ### Создание публикации \ Create post (POST):
```
http://127.0.0.1:8000/api/v1/posts/
```
в теле запроса передать \ pass in body of the request:
```
{
"text": "пример/example",
"image": "пример/example",
"group": пример/example
}
```
где в графу "пример" \ where in field "example"
  + поля "text": "пример", необходимо передать текст поста
  + field "text": "example" must contain post text
  + поля "image": "пример", необходимо передать закодированное в виде строки изображение или ничего
  + field "image": "example" must contain string-encoded image or nothing
  + поля "group": пример/example" необходимо передать id сообщества или ничего
  + field "group": "example" must contain community id or nothing


+ ### Создание коментария \ Create comment (POST):
```
http://127.0.0.1:8000/api/v1/posts/post_id/comments/
```
где \ where:
  + post_id - номер запрашиваемого поста
  + where post_id - is post number

в теле запроса передать \ pass in body of the request:
```
{
"text": "пример/example"
}
```
пример/example - текст комментария \ comment text

+ ### Обновление публикации \ Post update (PUT)/Частичное обновление публикации \ post part update (PATCH)/Удаление публикации \ Delete post (DELETE):
```
http://127.0.0.1:8000/api/v1/posts/post_id/
```
где \ where:
  + post_id - идентификатор(цифровой) нужной публикации
  + post_id - identifier (integer) of desired publication

+ ### Обновление коментария \ Comment update (PUT)/Частичное обновление коментария \ comment part update (PATCH)/Удаление комментария \ Delete comment (DELETE):
```
http://127.0.0.1:8000/api/v1/posts/post_id/comments/comments_id
```
где \ where:
  + post_id - идентификатор(цифровой) нужной публикации
  + post_id - identifier (integer) of desired publication
  + comments_id - идентификатор(цифровой) нужного комментария
  + comments_id - identifier (integer) of desired comment

+ ### Получение списка подпискок пользователя, сделавшего запрос \ Get list of subscriptions that request for user (GET)
```
http://127.0.0.1:8000/api/v1/follow/
```
+ ### Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса \ subscription from user who made request to user for follow (POST)
```
http://127.0.0.1:8000/api/v1/follow/
```
+ ### Дополнительная информация \ Additional Information:
  + Возможен поиск по подпискам по параметру search \ You can search by subscriptions by parameter search
  + Используется пагинация(LimitOffsetPagination) при указании параметров limit и offset при получение публикаций \ LimitOffsetPagination pagination is used in project, when receiving publications specifying you can use limit and offset parameters
