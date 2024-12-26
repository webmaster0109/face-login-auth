from django.shortcuts import render
import base64
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from .models import FaceLoginAuth

@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        face_image_data = request.POST['face_image']
        face_image_data = face_image_data.split(",")[1]
        face_login_image = ContentFile(base64.b64decode(face_image_data), name=f'{username}_.jpg')

        user = None
        try:
            user = User.objects.create(username=username)
        except Exception as e:
            JsonResponse({
                'status': 'error',
                'message' : 'Username is already taken'
            })
        FaceLoginAuth.objects.create(user=user, face_login=face_login_image)
        return JsonResponse({
            'status': 'success',
            'message': 'User registered successfully'
        })
    
    return render(request, template_name="register.html")