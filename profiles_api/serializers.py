from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Testing the POST in our ApiView"""
    name = serializers.CharField(max_length=10)
