# Python Developer Case Study

A guide to starting up the project on your pc - requires python

#### In one terminal window set up Django

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# Visit localhost:8000
```