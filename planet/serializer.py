from rest_framework import serializers

from .models import Inner

class InnerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Inner