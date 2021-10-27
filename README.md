# Django Project Password Generator

<img src="https://api.iconify.design/logos/django.svg" width="200" />

This project is a simple Django app that generates a random password for you.


### How to run

You can run the app by executing the following command:

```
__python manage.py migrate__ and then __python manage.py runserver__
```

### Using Docker

You can use Docker to run the app. (This is the recommended way to run the app.)

```
docker build --tag python-django .
docker run --publish 8000:8000 --name python-django python-django
```



