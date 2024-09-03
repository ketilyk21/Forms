from django.contrib import admin
from django.urls import path
from matricula import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cadastrados/', views.pessoas, name='cadastrados')
]

