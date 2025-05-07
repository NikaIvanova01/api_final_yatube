# Yatube Social Network API

## Описание
REST API для социальной сети блогов с полным циклом функций:
- Публикация и комментирование постов
- Группировка записей по тематическим сообществам
- Система подписок на авторов
- JWT-аутентификация
- Пагинация и фильтрация
- Пермишены с гибким управлением доступа

**Технологический стек**:
- Python 3.11
- Django 4.2
- Django REST Framework 3.14
- Simple JWT 5.3
- PostgreSQL (опционально)

## Установка и запуск

### Базовые требования:
- Python 3.11+
- Git
- Установленный virtualenv

```bash
# 1. Клонирование репозитория
git clone https://github.com/NikaIvanova01/api_final_yatube.git
cd api_final_yatube

# 2. Настройка виртуального окружения
python -m venv venv

# Активация окружения
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate.bat # Windows

# 3. Установка зависимостей
pip install -r requirements.txt

# 4. Настройка БД (SQLite по умолчанию)
python manage.py migrate

# 5. Создание суперпользователя (опционально)
python manage.py createsuperuser

# 6. Запуск сервера
python manage.py runserver
```

## Примеры API-запросов

### Аутентификация
```bash
# Получение JWT-токена
curl -X POST http://localhost:8000/api/v1/jwt/create/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'

# Ответ:
{"refresh":"...","access":"..."}
```

### Работа с постами
```bash
# Создание поста
curl -X POST http://localhost:8000/api/v1/posts/ \
  -H "Authorization: Bearer ваш_токен" \
  -H "Content-Type: application/json" \
  -d '{"text": "Новый пост", "group": 1}'

# Фильтрация по группе
curl -X GET "http://localhost:8000/api/v1/posts/?group=1"
```

### Комментарии
```bash
# Добавление комментария
curl -X POST http://localhost:8000/api/v1/posts/1/comments/ \
  -H "Authorization: Bearer ваш_токен" \
  -H "Content-Type: application/json" \
  -d '{"text": "Отличный пост!"}'
```

### Подписки
```bash
# Подписка на автора
curl -X POST http://localhost:8000/api/v1/follow/ \
  -H "Authorization: Bearer ваш_токен" \
  -H "Content-Type: application/json" \
  -d '{"following": "target_username"}'
```

## Тестирование
Запуск всех тестов:
```bash
python manage.py test tests/
```

Проверка конкретного модуля:
```bash
python manage.py test tests.test_posts
```

## Документация
- Интерактивная документация: http://localhost:8000/redoc/
- OpenAPI Schema: http://localhost:8000/swagger/

## Особенности реализации
- **Пагинация**: Лимит/смещение через параметры `?limit=10&offset=20`
- **Поиск**: Фильтрация подписок по username (`/follow/?search=username`)
- **Пермишены**: 
  - Чтение доступно всем
  - Запись только для аутентифицированных
  - Редактирование только для авторов
- **Валидация**:
  - Минимальная длина текста: 1 символ
  - Запрет самоподписки
  - Уникальность подписок

## Лицензия
MIT License. Подробности в файле LICENSE.
