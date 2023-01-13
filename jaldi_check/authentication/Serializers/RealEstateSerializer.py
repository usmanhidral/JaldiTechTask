from rest_framework import serializers
from authentication.models import RealEstate


class RealEstateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        fields = ("id",  "description", "price", "real_estate_address")


class RealEstateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    email = serializers.CharField(source='user.email')
    class Meta:
        model = RealEstate
        fields = ("description", "price", "real_estate_address", "name", "email")


class AddRealEstateSerializer(serializers.ModelSerializer):

    class Meta:
        model = RealEstate
        fields = ("description", "price", "real_estate_address")

    def create(self, validate_data):
        validated_data = self.initial_data
        user_id = validated_data.pop('user', None)
        instance = RealEstate.objects.create(user_id=user_id, **validated_data)
        return instance

    def update(self, instance, validate_data):
        validated_data = self.initial_data
        user_id = validated_data.pop('user', None)
        RealEstate.objects.filter(id=instance.id).update(user_id=user_id, **validated_data)
        instance = RealEstate.objects.get(id=instance.id)

        return instance
