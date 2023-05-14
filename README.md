# bigbrain

## File Structure

bigbrain/ </br>
├── .gitignore </br>
├── .git </br>
├── manage.py </br>
├── requirements.txt </br>
├── bigbrain/ </br>
│ ├── **init**.py </br>
│ ├── asgi.py </br>
│ ├── settings.py </br>
│ ├── urls.py </br>
│ └── wsgi.py </br>
├── app/ </br>
│ ├── **init**.py </br>
│ ├── admin.py </br>
│ ├── apps.py </br>
│ ├── models.py </br>
│ ├── tests.py </br>
│ └── views.py </br>

## Virtualenv

### To create and run virtualenv

python3 -m virtualenv env
source ./env/Scripts/activate

### When new packages are installed

pip freeze > requirements.txt

### To install existing packages

pip install -r requirements.txt
