from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='calculator-home'),
    path('calc/', views.calc, name='calculator-calc'),

]
