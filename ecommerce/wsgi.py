import os
from django.core.wsgi import get_wsgi_application

# Establece el módulo de configuración para Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

# Obtiene la aplicación WSGI.
application = get_wsgi_application()
