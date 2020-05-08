# kodland-blog
Backend and minimal fronend


Шаги по запуску:

1. `git clone https://github.com/kohek-lab/kodland-blog.git`
2. `python -m venv venv`
3. `pip install -r requirements.txt`
4. Создайте свою PostgreSQL базу данных с доступами, которые указанны в файле settings.py 
(или же с другими доступами, но тогда нужно будет указать их в файле settings.py).  

Текущие доступы: `{
        'NAME': 'kodland',
        'USER': 'kodland_user',
        'PASSWORD': 'kodland_db_pass'
        }`
        
5. `python manage.py runserver`
6. Сайт должен стать доступным по адресу `http://localhost:8000/`.  
Страничка для добавления новых постов: `http://localhost:8000/posts/new`.
