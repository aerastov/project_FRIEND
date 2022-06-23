from rest_framework import serializers
from accounts.models import Profile
from django.contrib.auth.models import User


class GetUserSerializer(serializers.ModelSerializer):
    login = serializers.CharField(source="user.username")
    id = serializers.CharField(source="user.id")
    name = serializers.CharField(source="user.first_name")
    email = serializers.CharField(source="user.email")

    class Meta:
        model = Profile
        fields = ('id', 'phone', 'login', 'name', 'birth', 'tg', 'email')


class PostUserRegisterSerializer(serializers.ModelSerializer):
    # login = serializers.CharField(source="user.username", read_only=True)
    # password = serializers.CharField(source="user.password", read_only=True)
    # name = serializers.CharField(source="user.first_name", read_only=True)
    # email = serializers.CharField(source="user.email", read_only=True)
    # username = serializers.CharField(source='login')
    # first_name = serializers.CharField(source='name')
    # username = serializers.SerializerMethodField('login')
    # first_name = serializers.SerializerMethodField('name')
    # class Meta:
    #     model = User
    #     fields = ('phone', 'login', 'password', 'name', 'birth', 'tg', 'email')
    username = serializers.CharField(source="login")
    # username = serializers.CharField(source="login")
    # print(username)
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'email')

    def save(self):
        print("44444444", self.validated_data['username'])
        # username = self.validated_data['login']
        # first_name = self.validated_data['name']


    # def create(self, validated_data):
    #     user = User(
    #         username=validated_data['login']
    #     )
    #     user.phone(validated_data['phone'])
    #     user.birth(validated_data['birth'])
    #     user.tg(validated_data['tg'])
    #     user.save()
    #     return user



# class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    # username = serializers.CharField(source="user.username")
    # user_id = serializers.CharField(source="user.id")

    # class Meta:
    #     model = UserProfile
    #     fields = ('id', 'name', 'avatar', 'avatar_small', 'room')

    # def create(self, validated_data):
    #     print(validated_data['username'])
    #     # user = User(username=validated_data['username'])
    #     # user.set_password(validated_data['password'])
    #     # user.save()
    #     return validated_data
