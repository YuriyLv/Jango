# Використовуємо базовий образ Python 3.8
FROM python:3.8

# Зберігаємо робочу директорію у змінну середовища
ENV APP_HOME=/usr/src/app
WORKDIR $APP_HOME

# Копіюємо вміст проекту у контейнер
COPY . .

# Встановлюємо залежності проекту
RUN pip install -r requirements.txt

# Збираємо статичні файли проекту


# Встановлюємо змінні середовища
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Вказуємо, який порт слід відкрити для контейнера
EXPOSE 8000

# Запускаємо додаток
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
