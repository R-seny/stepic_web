sudo unlink /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

mysql -uroot -e "create database qadb"

cd ~/web/ask

python manage.py makemigrations qa
python manage.py migrate

cd ~/web
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo gunicorn -c /etc/gunicorn.d/hello.py hello:application &
sudo gunicorn -c ./etcmy/qa_conf_stepic.py  ask.wsgi:application &



