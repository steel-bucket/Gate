from rest_framework import serializers
from .models import GuestForm


class GuestFormSerializer(serializers.ModelSerializer):
    # name = serializers.CharField()
    # roll_id = serializers.CharField()
    # contact = serializers.CharField()
    # address = serializers.CharField()
    # purpose = serializers.CharField()
    # notes = serializers.CharField()
    class Meta:
        model = GuestForm
        fields = ["id", "name", "time", "entering", "roll_id", "contact", "address", "purpose", "notes"]
        extra_kwargs = {
            "id": {"read_only": True},
            "name": {"required": False},
            "entering": {"required": True},
            "roll_id": {"required": True},
            "contact": {"required": False},
            "notes": {"required": False}
        }
