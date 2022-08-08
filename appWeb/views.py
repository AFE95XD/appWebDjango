from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola esta es mi primera aplicacion django")
