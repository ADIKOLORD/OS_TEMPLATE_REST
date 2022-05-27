TUTORIAL FOR DJANGO PROJECT

#################################--CREATE PROJECT--###########################################

1) create venv, activate

$ python3 -m venv venv
$ source venv/bin/activate


2) install django, rest-framework

$ pip install django
$ pip install djangorestframework


3) create project, apps

$ django-admin startproject name
$ cd name/
$ ls
you should see file manage.py
$ python3 manage.py startapp firstapp

3.0) create config.py in your project directory(where have settings.py, urls.py)
move SECRET_KEY to config.py

#######################--ATTENTION--#######################
All your private data should be in CONFIG.PY   !!!
#######################--END--#######################


3.1) add app in settings.py -> INSTALLED APPS
name.apps.NameConfig
example: firstapp.apps.FirstappConfig


3.2) add 'rest_framework' in settings.py -> INSTALLED APPS
'rest_framework'



4) create model in firstapp/models.py

class <NameModel>(models.Model):


4.1) if you have ImageField
$ pip install pillow


4.1.2) add MEDIA_URL, MEDIA_ROOT, SETTING_URL, SETTING_ROOT



5) create serializers.py in firstapp
from rest_framework.serializers import ModelSerializer

class <NameModel>Serializer(ModelSerializer):


6) create class in views.py
from rest_framework.viewsets import ModelViewSet

class <NameModel>APIViewSet(ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer



7) add <NameModel>APIViewSet to urls.py -> urlpatterns
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import <NameModel>APIViewSet

router = DefaultRouter()
router.register('your-url', <NameModel>APIViewSet)

urlpatterns = [
    ...
    path('api/v1/', include(router.urls)

]


8) in terminal doing migrate
$ python3 manage.py makemigrations
$ python3 manage.py migrate

8.1) you can see this in site
$ python3 manage.py runserver
in browser you can write http://127.0.0.1:8000/api/v1/your-url



9) add swagger to urls.py
$ pip install drf_yasg

9.0) add 'drf_yasg' in settings.py -> INSTALLED APPS
create swagger.py in project directory where have (urls, settings).py

9.1) add swagger setting(you can search in browser) in swagger.py

9.2) in urls.py
from .swagger import swagger_urlpatterns

urlpatterns += swagger_urlpatterns

############--ADD ADMIN PANEL--##############

1) in admin.py
from .models import <NameModel>

admin.site.register(<NameModel>)


2) in terminal
$ python3 manage.py createsuperuser


3) open browser
http://127.0.0.1:8000/admin


###########################--END BASE PROJECT--##############################


###########################--REGISTER--###########################

CREATE NEW APP FOR CUSTOM USER

import AbstractUser from django.contrib.auth.models

CREATE NEW MODEL MY USER(AbstractUser):
    my fields


before migrations add in Settings.py

AUTH_USER_MODEL = myapp.modeluser

add to admin.py


























#################################--ADD TO HEROKU--###########################################


!!! TRANSLATE THE TEXT !!!
NOT RELATED TO THE PROJECT
DON'T TORTURE YOUR BRAIN


0) installing all requirements
$ pip install gunicorn
$ pip install whitenoise
$ pip install psycopg2 or psycopg2-binary

  still need to be added ...


1) create Procfile, in write
web: gunicorn <nameproject>.wsgi --log-file -



2) create runtime.txt, in write
python-3.9.6



3) pip freeze > requirements.txt


3.1) change django version == 3.2.9



4) doing COLLECT STATIC
$ python3 manage.py collectstatic


5) adding to heroku

5.1) create heroku app in site heroku app, and give name

5.2) in terminal

5.2.1) login to heroku
$ sudo app install heroku  ?????????????maybe??????????????

$ heroku login

heroku opening for you browser, you should logining there

5.2.2) connect heroku
$ heroku git:clone -a <name app in heroku>

$ ls
you should see manage.py

$ git init
$ git add .
$ git commit -am "your comment"
$ git push heroku master

6) after the download is complete
open browser and write:
https://<name app in heroku>.herokuapp.com/swagger
