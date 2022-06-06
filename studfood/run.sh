python manage.py migrate
python manage.py collectstatic
gunicorn studfood.wsgi:application \
  --bind 0.0.0.0:80