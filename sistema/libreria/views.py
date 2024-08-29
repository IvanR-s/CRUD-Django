from django.shortcuts import render

def inicio(request):
    return render( request, 'paginas/inicio.html')

def producto(request):
    return render(request,'paginas/producto.html')

def venta(request):
    return render(request,'paginas/venta.html')

def compra(request):
    return render(request,'paginas/compra.html')

def Provedor(request):
    return render(request,'paginas/Provedor.html')

def Usuario(request):
    return render(request,'paginas/Usuario.html')

def tablausuarios(request):
    return render(request, 'paginas/tablausuarios.html')

def iniciosesion(request):
    return render(request, 'paginas/iniciosesion.html')
# Create your views h.ere.

def Crearproducto(request):
    return render(request, 'paginas/Crearproducto.html')