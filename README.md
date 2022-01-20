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
```

In a separate terminal window, create your schedule in the database, then start the Q Cluster

```bash
.\venv\Scripts\activate
python manage.py shell
# Create a repeating schedule using Django Shell. Copy and paste the path below
exec(open('../hacker-news-api/items/tasks.py').read())
# Exit the Django shell
exit()
# Then run the Q cluster
python manage.py qcluster
```

## Click on the Postman Link Below to test it out
[![Run in Postman](https://s3.amazonaws.com/postman-static/run-button.png)](https://www.postman.com/warped-crater-394879/workspace/hackernewsapi/collection/13203401-3b2d0ff0-d23d-430c-b6a5-7bbc2d7d9eb8)