# NLPF
# Django windows
Installer python 3+  
pip install django  
pip install mysqlclient  
pip install django-bootstrap3  

# Commandes utiles
python manage.py runserver => site sur localhost/url  
python manage.py makemigrations => migrations des models  
python manage.py migrate => migration DB  
python manage.py sqlmigration 0001 => créer un fichier de migration 0001  

# pour créer la database
CREATE DATABASE fortunedb;
GRANT ALL PRIVILEGES ON fortunedb.* TO 'polls'@'localhost';
GRANT ALL PRIVILEGES ON fortunedb.* TO 'ODBC'@'localhost';
FLUSH PRIVILEGES;

# Pour Robin
Le projet contient un tutoriel dans le répertoire /sondage qui nous a permis de prendre en main django et d'apprendre le python. Et dans l'autre répertoire /mysite où nous avons codé le projet Fortune.
