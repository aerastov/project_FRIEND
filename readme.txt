
База использована SQLite
Файл конфига БД DATABASE_config.py

python: 3.9.7
django: 4.0.3
клонируем проект из репозитория в созданное виртуальное окружение (python + django)

git clone https://github.com/aerastov/project_FRIEND.git

инсталлируем необходимые для работы проекта пакеты:

pip install djangorestframework
pip install django-cors-headers

В консоли переходим в директорию проекта и стартуем проект:
python manage.py runserver

API проекта будет доступно по адресам:
http://127.0.0.1:8000/v1/<id>
http://127.0.0.1:8000/v1/auth/register
http://127.0.0.1:8000/v1/auth/login

