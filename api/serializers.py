from rest_framework import serializers
from accounts.models import Profile
from django.contrib.auth.models import User
import re
from datetime import date, timedelta


class GetUserSerializer(serializers.ModelSerializer):
    login = serializers.CharField(source="user.username")
    id = serializers.CharField(source="user.id")
    name = serializers.CharField(source="user.first_name")
    email = serializers.CharField(source="user.email")

    class Meta:
        model = Profile
        fields = ('id', 'phone', 'login', 'name', 'birth', 'tg', 'email')


class PostUserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'email']

    def validate(self, data):
        try: self.initial_data['username']
        except: raise serializers.ValidationError("Нет обязательного поля: login")
        try: self.initial_data['first_name']
        except: raise serializers.ValidationError("Нет обязательного поля: name")
        try:
            if not re.fullmatch(r'\+\d{11,15}', self.initial_data['phone']):
                raise serializers.ValidationError("Номер телефона задан не верно")
        except: raise serializers.ValidationError("Нет обязательного поля: phone")
        try:
            if not re.fullmatch(r'\d{4}\-\d{2}\-\d{2}', self.initial_data['birth']):
                raise serializers.ValidationError("Дата рождения задана не верно")
        except: raise serializers.ValidationError("Нет обязательного поля: birth")
        today = date.today()
        birth = self.initial_data['birth']
        dt = date(int(birth[0:4]), int(birth[5:7]), int(birth[8:]))
        if (today - dt) < timedelta(6574):  # 6574 дней = 18 лет
            raise serializers.ValidationError("Вам менее 18 лет")
        return data

    def create(self, validated_data):
        profile = self.initial_data
        del profile['username']
        del profile['password']
        try: del profile['first_name']
        except: pass
        try: del profile['email']
        except: pass
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile)
        return user

class PostLoginSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ('username', 'password')
