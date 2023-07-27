from datetime import date, datetime
from users.models import User

# Procesador de contexto para calcular la edad:
def age_processor(request):
    fecha_nacimiento = request.user.birthday
    birthday = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    edad = datetime.now().year - birthday.year
    return edad