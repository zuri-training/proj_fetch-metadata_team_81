To deploy a the server you first need to clone the repository.

Next you create and activate a virtual environmemnt by running the following commands:
```
$ virtualenv {'env' the desired name of your environment goes here}
$ env\Scripts\activate
```
Next you pip install all the required packages to the virtualenv. (you will be prumpted on all the packages you need to install when you try to run the server if there is anyone missing).
```
$ pip install django
$ pip install hachoir
$ pip install pillow
$ pip install six
$ pip install pikepdf
$ pip install tinytag
$ pip install mutagen
$ pip install ffmpeg-python
$ pip install whitenoise
```
Next you run migrations by running the command:
```
python manage.py migrate 
```
After that you create a superuser:
```
python manage.py createsuperuser
```
then finally you run the server
```
python manage.py runserver
```

<br>

**If you wish to host this website on any platform you We used the django framework default(Monolithic) template . You can find the pages in the templates folder, stylesheets in the static folder. Clone the repository, then continue the hosting using the documentation of the hosting platform.**