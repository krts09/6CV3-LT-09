import os
import django

# Configura la variable de entorno para Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ServerLa_Aeneta.settings')

# Inicializa Django
django.setup()

from TESCOM_MAIN.models import Alumno

# Ahora puedes interactuar con los modelos de Django
for alumno in Alumno.objects.all():
    print(alumno.alumno_id, alumno.nombre)
