import pytest
from PIL import Image
import io
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_funcion():
    client = APIClient()

    imagen = Image.new('RGB', (100,100), color='red')
    buffer = io.BytesIO()
    imagen.save(buffer, format='PNG')
    buffer.seek(0)

    archivo_simulado = SimpleUploadedFile('test_imagen.png', buffer.getvalue(), content_type='image/png')

    response = client.post('/MicroServicioDjango/imagen_compresion/', {'file':archivo_simulado}, format='multipart')

    assert response.status_code == 200
    assert response['Content-Type'] == 'image/jpeg'
    assert response['Content-Disposition'] == 'attachment; filename="imagen_comprimida.jpg"'