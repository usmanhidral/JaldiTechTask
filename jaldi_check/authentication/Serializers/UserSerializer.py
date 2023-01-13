
from rest_framework import serializers
from authentication.models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "email")

class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'address')


class AddUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")

    def validate_username(self, value):
        if ' ' in value:
            raise serializers.ValidationError("Spaces cannot be in username")

        return value

    def create(self, validate_data):
        validated_data = self.initial_data
        email = validated_data.get("email")
        username = validated_data.get("username")
        user_email = User.objects.filter(email=email).first()
        user_username = User.objects.filter(username=username).first()
        password = validated_data.get("password")
        confirm_password = validated_data.get("confirm_password")
        if confirm_password:
            validated_data.pop("email")
            validated_data.pop("username")
            validated_data.pop("password")
            validated_data.pop("confirm_password")

        if user_email:
            raise serializers.ValidationError({"detail": "User with same email already exist"})
        elif user_username:
            raise serializers.ValidationError("Username already exist")
        elif password is None:
            raise serializers.ValidationError("Password required")
        elif password != confirm_password:
            raise serializers.ValidationError("Password does not matched")
        else:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            user = User.objects.filter(id=new_user.id).update(**validated_data)

        return new_user

    def update(self, instance, validated_data):
        validated_data = self.initial_data
        try:
            email = validated_data.pop("email", None)
            username = validated_data.pop("username", None)
            password = validated_data.pop("password", None)

            User.objects.filter(id=instance.id).update(**validated_data)

        except Exception as e:
            print(e)

        return instance
