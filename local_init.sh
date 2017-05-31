sudo nginx
sudo gunicorn -c ./etc/qa_conf.py app.wsgi:application
