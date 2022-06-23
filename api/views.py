from django.http import JsonResponse
from accounts.models import Profile
from .serializers import GetUserSerializer, PostUserRegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


@api_view(['GET'])
def get_user(request, user):
    if request.method == 'GET':
        if Profile.objects.filter(user=user).exists():
            user = Profile.objects.filter(user=user)
            serializer = GetUserSerializer(user, many=True)
            # return JsonResponse(serializer.data, safe=False)
            return Response(serializer.data)
        else:
            response = [{"Error 404": "object not found"}]
            return JsonResponse(response, safe=False)


@api_view(['POST'])
def post_register(request):
    if request.method == 'POST':
        serializer = PostUserRegisterSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
