Язык: Русский

1) Чтобы создать бд необходимо в терминале ввести:
sudo -i -u postgres
postgres# CREATE USER db_user PASSWORD 'my_passwd';
postgres# CREATE DATABASE db_name OWNER db_user;
psql <db_name>
CREATE EXTENSION postgis;

2) В виртуальном окружении:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Language: English

1) In order to create a db type following commands:
sudo -i -u postgres
postgres# CREATE USER db_user PASSWORD 'my_passwd';
postgres# CREATE DATABASE db_name OWNER db_user;
psql <db_name>
CREATE EXTENSION postgis;

2) In the vertual environment:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
