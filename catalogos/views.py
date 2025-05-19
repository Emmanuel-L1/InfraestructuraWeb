from django.shortcuts import render, HttpResponse, redirect

from catalogos.models import Carrera, Plan, Materia

from catalogos.forms import CarreraForm, PlanForm, MateriaForm

from django.views import generic

from django.urls import reverse_lazy

# Create your views here.

def homecatalogos(request):
    return render (request, 'homecatalogos.html')

def homeinscripcion(request):
    pass

#Vistas basadas en funciones
def carreraRead(request):
    carreras =  Carrera.objects.all()
    data = {'carreras' : carreras}
    return render (request, 'carrerasRead.html', data)

def carreraCreate(request):
    if request.method == 'POST': # Se quiere guardar form lleno
        form = CarreraForm(request.POST) # Se envia form con metodo POST
        if form.is_valid(): # Si esta bien el formulario
            form.save() # Guarda en un registro en la tabla
            return redirect('carreraRead') # Redirige al listado de carreras
    else:
        form = CarreraForm() #Se pinta formulario al ingresar
    return render (request, 'carreraCreate.html', {'form':form})

def carreraUpdate(request, id):
    carrera = Carrera.objects.get(id=id)
    if request.method == 'GET':
        form = CarreraForm(instance= carrera)
    else:
        form = CarreraForm(request.POST, instance=carrera)
        if form.is_valid():
            form.save()
            return redirect('carreraRead')
    return render (request, 'carreraCreate.html', {'form':form})

def carreraDelete(request, pk):
    carrera = Carrera.objects.get(id=pk)
    if request.method == 'POST':
        carrera.delete()
        return redirect('carreraRead')
    return render (request, 'carreraDelete.html', {'carrera':carrera})

#Vistas basadas en clases
class CarreraView(generic.ListView):
    model = Carrera
    queryset = Carrera.objects.all()
    template_name = 'carrerasRead.html'
    context_object_name = 'carreras'

class CarreraCreate(generic.CreateView):
    model = Carrera
    template_name = 'carreraCreate.html'
    context_object_name = 'carreras'
    form_class = CarreraForm
    success_url = reverse_lazy('carreraView')

class CarreraUpdate(generic.UpdateView):
    model = Carrera
    template_name = 'carreraCreate.html'
    context_object_name = 'carreras'
    form_class = CarreraForm
    success_url = reverse_lazy('carreraView')

class CarreraDelete(generic.DeleteView):
    model = Carrera
    template_name = 'carreraDelete.html'
    context_object_name = 'carreras'
    success_url = reverse_lazy('carreraView')

#Fin vistas basadas en clases

def planRead(request):
    planes =  Plan.objects.all()
    data = {'planes' : planes}
    return render (request, 'planesRead.html', data)

def planCreate(request):
    if request.method == 'POST': # Se quiere guardar form lleno
        form = PlanForm(request.POST) # Se envia form con metodo POST
        if form.is_valid(): # Si esta bien el formulario
            form.save() # Guarda en un registro en la tabla
            return redirect('planRead') # Redirige al listado de carreras
    else:
        form = CarreraForm() #Se pinta formulario al ingresar
    return render (request, 'planCreate.html', {'form':form})

def planUpdate(request, id):
    plan = Plan.objects.get(id=id)
    if request.method == 'GET':
        form = PlanForm(instance= plan)
    else:
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('planRead')
    return render (request, 'planCreate.html', {'form':form})

def planDelete(request, pk):
    plan = Plan.objects.get(id=pk)
    if request.method == 'POST':
        plan.delete()
        return redirect('planRead')
    return render (request, 'planDelete.html', {'plan':plan})

def materiaRead(request):
    materias =  Materia.objects.all()
    data = {'materias' : materias}
    return render (request, 'materiasRead.html', data)

def materiaCreate(request):
    if request.method == 'POST': # Se quiere guardar form lleno
        form = MateriaForm(request.POST) # Se envia form con metodo POST
        if form.is_valid(): # Si esta bien el formulario
            form.save() # Guarda en un registro en la tabla
            return redirect('materiaRead') # Redirige al listado de carreras
    else:
        form = MateriaForm() #Se pinta formulario al ingresar
    return render (request, 'materiaCreate.html', {'form':form})

def materiaUpdate(request, id):
    materia = Materia.objects.get(id=id)
    if request.method == 'GET':
        form = MateriaForm(instance= materia)
    else:
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('materiaRead')
    return render (request, 'materiaCreate.html', {'form':form})

def materiaDelete(request, pk):
    materia = Materia.objects.get(id=pk)
    if request.method == 'POST':
        materia.delete()
        return redirect('materiaRead')
    return render (request, 'materiaDelete.html', {'materia':materia})