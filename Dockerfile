# Базовый образ
FROM python:3.9

# Установка переменной среды PYTHONUNBUFFERED на значение 1
ENV PYTHONUNBUFFERED 1

# Создание и переход в рабочую директорию /app
WORKDIR /app

# Копирование файла зависимостей requirements.txt в рабочую директорию
COPY requirements.txt /app/

# Установка зависимостей, указанных в requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копирование текущего каталога (содержащего файлы проекта Django) в рабочую директорию
COPY . /app/

# Выполнение команды для создания миграций и сбора статических файлов при запуске контейнера
# RUN python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput

# Открытие порта 8000 контейнера для обработки входящих запросов
EXPOSE 8000

# Запуск сервера Django при запуске контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
