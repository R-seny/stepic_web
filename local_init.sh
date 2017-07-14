sudo nginx
gunicorn -c ./etc/qa_conf.py ask.wsgi:application

#mysql -uroot -e "create database qadb" ## Password is 123


#source /home/bi/.virtualenvs/djangodev/bin/activate # To activate the virtualenv
#python manage.py makemigrations qa
#python manage.py migrate
