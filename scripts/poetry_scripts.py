import argparse
import os


def django_makemigrations_and_migrate():
    """Django makemigrations and migrate"""
    os.system("poetry run python src/manage.py makemigrations")
    os.system("poetry run python src/manage.py migrate")


def django_runserver():
    """Fire up the Django server"""
    os.system("poetry run python src/manage.py runserver")


def django_test():
    """Test Django server"""
    parser = argparse.ArgumentParser(
        description="Select specific Django application to test"
    )
    parser.add_argument(
        "--app",
        dest="selected_apps",
        default="openADR2b_vtn",
        help='The Django applications you want to test separated by space (e.g. --app="openADR2b_vtn other_app").',
    )
    args = parser.parse_args()
    os.system(f"poetry run python src/manage.py test {args.selected_apps}")
