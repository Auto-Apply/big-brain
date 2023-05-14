# big-brain

## File Structure

bigbrain/
├── .gitignore
├── .git
├── manage.py
├── requirements.txt
├── bigbrain/
│ ├── **init**.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── app/
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ └── views.py

## Virtualenv

### To create and run virtualenv

python3 -m virtualenv env
source ./env/Scriptse/activate

### When new packages are installed

pip freeze > requirements.txt

### To install existing packages

pip install -r requirements.txt
