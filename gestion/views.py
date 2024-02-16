from django.shortcuts import render

# Create your views here.
def vistaPrueba(request):
    return render(request=request, template_name='prueba.html')