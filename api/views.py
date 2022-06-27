from django.http import JsonResponse
from accounts.models import Profile
from .serializers import GetUserSerializer, PostUserRegisterSerializer, PostLoginSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_403_FORBIDDEN
from django.contrib.auth.models import User
import json

@api_view(['GET'])
def get_user(request, user):
    if request.method == 'GET':
        try:
            if Profile.objects.filter(user=user).exists():
                user = Profile.objects.filter(user=user)
                serializer = GetUserSerializer(user, many=True)
                # return Response(json.dumps(serializer.data))  # на выходе json, киррилица в кодировке
                return Response(serializer.data)  # на выходе массив, с отображением кириллицы
                # return JsonResponse(json.dumps(serializer.data), safe=False)
            return Response(status=HTTP_404_NOT_FOUND)
        except:
            return Response("введите ID (число)", status=HTTP_404_NOT_FOUND)


@api_view(['POST'])
def post_register(request):
    if request.method == 'POST':
        serializer = PostUserRegisterSerializer(data=request.data)
        try:
            serializer.initial_data['username'] = serializer.initial_data['login']
            del serializer.initial_data['login']
        except: pass
        try:
            serializer.initial_data['first_name'] = serializer.initial_data['name']
            del serializer.initial_data['name']
        except: pass
        if serializer.is_valid():
            serializer.save()
            user_id = {'id': User.objects.get(username=serializer.data['username']).id}
            return Response(user_id, status=HTTP_201_CREATED)
        else: return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_login(request):
    if request.method == 'POST':
        serializer = PostLoginSerializer(data=request.data)
        try: serializer.initial_data['username'] = serializer.initial_data['login']
        except: return Response('Нет обязательного поля: login ', status=HTTP_404_NOT_FOUND)
        try: serializer.initial_data['password']
        except: return Response('Нет обязательного поля: password ', status=HTTP_404_NOT_FOUND)

        if serializer.is_valid():
            print('serializer.initial_data', serializer.initial_data)
            if User.objects.filter(username=serializer.initial_data['username']).exists():
                print('Добрались до пароля')
                if serializer.initial_data['password'] == User.objects.get(username=serializer.initial_data['username']).password:
                    print('пароли совпали')
                    user_id = {'user id': User.objects.get(username=serializer.initial_data['username']).id}
                    return Response(user_id, status=HTTP_200_OK)
                else:
                    print('пароли не совпали')
                    return Response('Неверный пароль', status=HTTP_403_FORBIDDEN)
            else:
                return Response('Пользователь с таким именем не найден', status=HTTP_404_NOT_FOUND)
