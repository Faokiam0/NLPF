# NLPF
# Django windows
Installer python 3+
pip install django
pip install mysqlclient

# Commandes utiles
python manage.py runserver => site sur localhost/url
python manage.py makemigrations => migrations des models
python manage.py migrate => migration DB
python manage.py sqlmigration 0001 => je sais pas encore

# pour créer la database
CREATE DATABASE pollsdb;
CREATE USER 'polls'@'localhost';
CREATE USER 'ODBC'@'localhost';
GRANT ALL PRIVILEGES ON pollsdb.* TO 'polls'@'localhost';
GRANT ALL PRIVILEGES ON pollsdb.* TO 'ODBC'@'localhost';
FLUSH PRIVILEGES;