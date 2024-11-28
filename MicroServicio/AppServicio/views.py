from PIL import Image
from io import BytesIO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse


@api_view(['POST'])
def imagen_compresion(request):
    if 'file' not in request.FILES:
        return Response('No se envió un archivo' ,status=status.HTTP_400_BAD_REQUEST)

    archivo = request.FILES['file']

    try:

        imagen = Image.open(archivo)

        if imagen.mode == 'RGBA':
            imagen = imagen.convert('RGB')    
        
        buffer = BytesIO()
        calidad = 50
        imagen.save(buffer, format='JPEG', optimize=True, quality=calidad)
        buffer.seek(0)

        return FileResponse(buffer, as_attachment=True, filename='imagen_comprimida.jpg', status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

