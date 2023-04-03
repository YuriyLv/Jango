## use virtualenv
```
pip install django
```
```
django-admin startproject DevOpsHelPer
```
```
python manage.py startapp blog
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
```
python manage.py runserver
```

for docker
```
pip freeze > requirements.txt
```
```
sudo docker build -t my-django-app .
```
```
sudo docker run -p 8000:8000 my-django-app
```
```
localhost:8000
```