# 📦 Встановлення та робота з Alembic

## 1. 💠 Ініціалізація Alembic

```bash
alembic init alembic
```

---

## 2. ⚙️ Налаштування Alembic

### У файлі `alembic/env.py` додайте:

```python
from database.models import Base
from database.db import url

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

target_metadata = Base.metadata
config.set_main_option("sqlalchemy.url", url)
```

---

## 3. 🗂 Налаштування `alembic.ini`

- Перемістіть файл `alembic.ini` у корінь проєкту.
- Змініть шлях до міграцій:

```ini
script_location = %(here)s/alembic/migrations
```

---

## 4. 🧱 Створення та застосування міграцій

### 4.1 Створення нової міграції

```bash
alembic revision -m "initial commit"
```

### 4.2 Застосування останніх міграцій

```bash
alembic upgrade head
```

### 4.3 Повернення до попередньої версії (rollback)

```bash
alembic downgrade -1
```

### 4.4 Перегляд історії міграцій

```bash
alembic history
```
