import os


def django_makemigrations_and_migrate():
    """Django makemigrations and migrate"""
    os.system("poetry run python src/manage.py makemigrations")
    os.system("poetry run python src/manage.py migrate")


def django_runserver():
    """Fire up the Django server"""
    os.system("poetry run python src/manage.py runserver")
