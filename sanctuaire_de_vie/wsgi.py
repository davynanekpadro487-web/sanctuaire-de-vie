import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sanctuaire_de_vie.settings')

django.setup()

# Auto-migrate au démarrage
from django.core.management import call_command
call_command('migrate', '--run-syncdb')

application = get_wsgi_application()
