from django.urls import path

from catalogos.views import homecatalogos, carreraRead, carreraCreate, carreraUpdate, carreraDelete, planRead, planCreate, planUpdate, planDelete, materiaRead, materiaCreate, materiaUpdate, materiaDelete
from catalogos.views import  CarreraView, CarreraCreate, CarreraUpdate, CarreraDelete

urlpatterns = [
    path('', homecatalogos, name='homecatalogos'),

    path('carrera/read/', carreraRead, name='carreraRead'),
    path('carrera/create/', carreraCreate, name='carreraCreate'),
    path('carrera/update/<int:id>', carreraUpdate, name='carreraUpdate'),
    path('carrera/delete/<int:pk>', carreraDelete, name='carreraDelete'),

    path('carreraView', CarreraView.as_view(), name='carreraView'),
    path('carreraCreate', CarreraCreate.as_view(), name='carreraCreatte'),
    path('carreraUpdate/<int:pk>', CarreraUpdate.as_view(), name='carreraUpdatte'), #Para vistas genericas siempre poner PK en vez de int
    path('carreraDelete/<int:pk>', CarreraDelete.as_view(), name='CarreraDelette'),

    path('plan/read/', planRead, name='planRead'),
    path('plan/create/', planCreate, name='planCreate'),
    path('plan/update/<int:id>', planUpdate, name='planUpdate'),
    path('plan/delete/<int:pk>', planDelete, name='planDelete'),

    path('materia/read/', materiaRead, name='materiaRead'),
    path('materia/create/', materiaCreate, name='materiaCreate'),
    path('materia/update/<int:id>', materiaUpdate, name='materiaUpdate'),
    path('materia/delete/<int:pk>', materiaDelete, name='materiaDelete'),
]