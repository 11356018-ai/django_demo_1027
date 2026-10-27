# AGENTS.md

## Project
- Django 6.1.2 (Python >=3.14.7). Dependencies in `pyproject.toml` / `uv.lock`.
- Project module: `config` (settings at `config/settings.py`, URLs at `config/urls.py`, WSGI/ASGI present).
- `manage.py` uses `DJANGO_SETTINGS_MODULE='config.settings'`.

## Environment
- Use the repo venv: `.venv\` (Windows). On Unix-like shells equivalent.
- Install deps via `uv sync` (lockfile present). If you don't use uv, install from `pyproject.toml`.

## Common commands
- Run dev server: `python manage.py runserver`
- Migrate: `python manage.py migrate`
- Make migrations: `python manage.py makemigrations`
- Create superuser: `python manage.py createsuperuser`
- Shell: `python manage.py shell`
- Tests: `python manage.py test`

## Gotchas
- DB: SQLite at `db.sqlite3` (BASE_DIR). No custom DB config.
- Email in dev: `MAILERS['default']` uses `django.core.mail.backends.console.EmailBackend` (not `EMAIL_BACKEND`).
- No local apps registered in `INSTALLED_APPS` yet (only Django contrib).
- Debug/secret key are hardcoded in `config/settings.py` (dev defaults).
