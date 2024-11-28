from django.urls import path
from .views import imagen_compresion, post_2

urlpatterns = [
    path('imagen_compresion/', imagen_compresion),
    path('post_2/', post_2),
]