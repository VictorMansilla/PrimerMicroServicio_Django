from django.urls import path
from .views import imagen_compresion

urlpatterns = [
    path('imagen_compresion/', imagen_compresion),
]