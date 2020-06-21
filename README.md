mkdir djreact && cd djreact

mkdir frontend
mkdir backend
cd backend
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r src/requirements.txt

django-admin startproject project1
mv project1 src
cd src



python manage.py migrate
python manage.py createsuperuser

django-admin startapp waiters

create model
register with admin

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

