from rest_framework import serializers

from .models import Outer

class OuterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Outer