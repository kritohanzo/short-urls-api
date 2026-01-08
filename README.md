# API коротких URL

## Позволяет:
- создать короткий URL
- посмотреть существующие короткие URL
- получить редирект на источник по короткому URL

### TODO:
- Dockerfile
- docker-compose.yml
- SQLite -> PostgreSQL
- Cache
- Schedule tasks (short url expiration)
- Validations
- README
- Config
- Environments
- Linters
- CI/CD
- ...

### Запуск:
- клонировать проект
- создать окружение
- - `python -m venv .venv` - native
- - `pip install uv && uv venv` - uv
- активировать окружение
- - `. ./.venv/Scripts/activate.ps1` - windows
- - `. ./.venv/bin/activate` - linux / macos
- установить зависимости
- - `pip install -r requirements.txt` - native
- - `uv pip install -r requirements.txt` - uv
- накатить миграции
- - `alembic upgrade head`
- запустить приложение
- - `python main.py`
- открыть сваггер
- - `http://localhost:8000/docs/`