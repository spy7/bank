from rest_framework import serializers
from .models import Account, Extract


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class ExtractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extract
        fields = '__all__'


class AccountExtractSerializer(serializers.ModelSerializer):
    extracts = ExtractSerializer(many=True)

    class Meta:
        model = Account
        fields = '__all__'
