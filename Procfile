web: gunicorn --pythonpath="$PWD/mobius_api" wsgi:application
worker: python mobius_api/manage.py rqworker default