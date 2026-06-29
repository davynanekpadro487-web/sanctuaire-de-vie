import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sanctuaire_de_vie.settings')

django.setup()

# Auto-migrate au démarrage
from django.core.management import call_command
call_command('migrate', '--run-syncdb')

# Création automatique du superuser s'il n'existe pas
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

application = get_wsgi_application()
