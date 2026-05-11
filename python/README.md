# Python часть проекта

Реализация структуры данных (например, стек) на Python.

Используются:
- `unittest` для тестов
- `coverage.py` для анализа покрытия
- `venv` для изоляции окружения

## Запуск тестов
```bash
source venv/bin/activate
pip install -r requirements.txt 
```
```bash
python -m unittest
```
Coverage
```bash
coverage run -m unittest
coverage html
```
Открыть отчёт:
```bash
htmlcov/index.html
```