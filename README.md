# api_final


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