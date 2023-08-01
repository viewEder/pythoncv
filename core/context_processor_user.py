from datetime import datetime
# Decorador:
from django.contrib.auth.decorators import login_required
# Modelos:
from curriculum.models import Skills, Stack, Academy, HobbiesExtras, EmploymentHistory, ProjectDev

# Procesador de contexto para calcular la edad:
def age_processor(request):
    
    if request.user.is_authenticated:
        usuario = request.user
        fecha_nacimiento = usuario.birthday
        try:
            if datetime.now().month <= fecha_nacimiento.month and datetime.now().day <= fecha_nacimiento.day:
                # Si el mes y el día actual es menor o igual al del nacimiento
                edad = (datetime.now().year-1) - fecha_nacimiento.year
            else:
                edad = datetime.now().year - fecha_nacimiento.year
        except:
            edad = 'No es posible calcular la edad'

        return {
                "edad": edad,
                "usuario" : usuario
                }
    else:
        return { 'mensaje': 'Usuario no conectado' }


# Procesador de contexto para los skills:
@login_required()
def skill_procesor(request):
    # Query para traer todos los skills del usuario:
    user_skills = Skills.objects.filter(user=request.user)
    return {
            "skills_user": user_skills
            }


# Procesador de contexto para los educación:
@login_required()
def academy_processor(request):
    # Traigo todas las instituciones en donde estudié:
    education_user = Academy.objects.filter(user=request.user)
    return {
            "education_user": education_user
            }