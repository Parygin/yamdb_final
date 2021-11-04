# Учебный проект: запуск docker-compose

[![Sprint 16 project](https://github.com/Parygin/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master)](https://github.com/Parygin/yamdb_final/actions/workflows/yamdb_workflow.yml)

Это учебный проект. Задача — изучить CI/CD с помощью GitHub Actions.
Приложение разворачивается в трёх контейнерах: (а) nginx, (б) web, (в) postgres.

## Установка и настройка
- склонировать репозиторий и запустить виртуальную среду:
```zsh
git clone https://github.com/Parygin/infra_sp2.git
python3 -m venv venv
source venv/bin/activate
```
- установить зависимости:
```zsh
pip install -r requirements.txt
```
- переименовать и отредактировать `.env.example`:
```zsh
mv .env.example .env
```
- запустить приложение:
```zsh
sudo docker-compose up -d --build
```
- собрать и выполнить миграции:
```zsh
docker-compose exec web python manage.py makemigrations --noinput
docker-compose exec web python manage.py migrate --noinput
```
- создать суперпользователя:
```zsh
docker-compose exec web python manage.py createsuperuser
```
- собрать статику:
```zsh
docker-compose exec web python manage.py collectstatic --no-input
```
Проект доступен по адресу: `http://127.0.0.1/admin/`

## Остановка и удаление
```zsh
docker-compose down
docker system prune --volumes
```


## Notes
Проект подготовил Евгений Парыгин по 
[учебной заготовке](https://github.com/yandex-praktikum/infra_sp2) 
Яндекс.Практикум.  
Ревью проекта провёл Артём Гребенюк.  
  
Stack: Python3.9, Django, Django REST framework, Docker, PostgresSQL
  
MIT
