from rest_framework import serializers

from .models import Notifications


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notifications
        fields = "__all__"

    def create(self, validated_data):
        return Notifications.objects.create_notice(**validated_data)

    def update(self, instance, validated_data):
        instance.type_notice = validated_data.get("type_notice", instance.type_notice)
        instance.name = validated_data.get("name", instance.name)
        instance.message = validated_data.get("message", instance.message)
        instance.save()

        return instance
