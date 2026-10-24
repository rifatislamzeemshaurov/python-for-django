# 📄 Python for Django: Cheat Sheet
*by Rifat Islam Sourov · keep this open while you code!*

## 📦 Variables & Types
```python
name = "Rifat"            # str
age = 20                  # int
price = 99.5              # float
is_active = True          # bool
bio = None                # nothing yet
type(age)                 # <class 'int'>
int("5"), str(5), float("2.5"), bool("")   # conversions
```

## 🔤 Strings
```python
s = "  Hello Django  "
s.strip().lower()         # 'hello django'
s.replace(" ", "-")       # swap text
"a,b,c".split(",")        # ['a', 'b', 'c']
"-".join(["a", "b"])      # 'a-b'
s[0], s[-1], s[1:4]       # index & slice
f"Hi {name}, you are {age}"   # ⭐ f-string
```

## 📋 Lists · 📖 Dicts · 🔒 Tuples · 🚫👯 Sets
```python
nums = [3, 1, 2]
nums.append(4); nums.remove(1); nums.pop()
sorted(nums), len(nums), sum(nums), 2 in nums

user = {"name": "Rifat", "age": 20}
user["name"]; user.get("phone", "N/A")
user["city"] = "Dhaka"; del user["age"]
user.keys(), user.values(), user.items()

point = (10, 20); x, y = point     # unpack
unique = set(["a", "a", "b"])      # {'a', 'b'}
```

## 🚦 Conditions
```python
if age >= 18 and is_active:
    ...
elif age >= 13 or name == "Rifat":
    ...
else:
    ...
status = "Adult" if age >= 18 else "Child"
```

## 🔁 Loops
```python
for item in items: ...
for i in range(1, 6): ...                 # 1..5
for i, item in enumerate(items, start=1): ...
for a, b in zip(list1, list2): ...
for key, value in user.items(): ...
while count < 5: count += 1
break      # stop the loop
continue   # skip to the next round
```

## ⚡ Comprehensions
```python
[n * 2 for n in nums]
[p for p in posts if p["published"]]
{name: len(name) for name in names}
```

## 🧃 Functions
```python
def greet(name, greeting="Hello"):
    """Docstring explains the function."""
    return f"{greeting}, {name}!"

greet("Rifat"); greet(name="Sara", greeting="Hi")

def total(*args, **kwargs): ...           # any values / any named values
sorted(posts, key=lambda p: p["likes"], reverse=True)
```

## 🚑 Errors
```python
try:
    value = int(text)
except ValueError as error:
    print("Oops:", error)
else:
    print("Worked!")
finally:
    print("Always runs")

raise ValueError("Something is wrong")
```

## 🏭 Classes
```python
class Post:
    site = "My Blog"                       # class attribute (shared)

    def __init__(self, title, likes=0):
        self.title = title                 # instance attribute
        self.likes = likes

    def like(self):
        self.likes += 1

    def __str__(self):
        return self.title

class FeaturedPost(Post):                  # inheritance
    def __init__(self, title, badge):
        super().__init__(title)
        self.badge = badge
```

## 📦 Modules & Tools
```python
import math
from datetime import date, datetime, timedelta
import json as js
```
```bash
python -m venv venv
venv\Scripts\activate         # Windows
source venv/bin/activate      # Mac / Linux
pip install django
pip freeze > requirements.txt
```

## 🎁 Decorators
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper

@my_decorator
def view(request): ...
```

## 📂 Files · 🌐 JSON · 📅 Dates
```python
with open("notes.txt", "w", encoding="utf-8") as f:   # "r" read, "a" append
    f.write("Hello\n")

json.dumps(data)         # Python → JSON text
json.loads(text)         # JSON text → Python

date.today() + timedelta(days=7)
datetime.now().strftime("%d %b %Y")              # '24 Oct 2026'
datetime.strptime("24-10-2026", "%d-%m-%Y")
```

## 🌉 Python → Django in one table
| Python | Django |
|--------|--------|
| `def home(request): return ...` | a **view** |
| `class Post(models.Model):` | a **model** |
| `{"posts": posts}` | template **context** |
| `for post in posts:` | `{% for post in posts %}` |
| `if user:` | `{% if user.is_authenticated %}` |
| `urlpatterns = [...]` | URL routing |
| `@login_required` | protect a page |
| `try / except` | `get_object_or_404` |

<sub>Made with ❤️ by Rifat Islam Sourov</sub>
