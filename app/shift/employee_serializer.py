from rest_framework import serializers

from core import models


class EmployeeSerializer(serializers.ModelSerializer):
    """Serialize the employee object"""

    class Meta:
        model = models.Empolyee
        fields = ('first_name', 'last_name')

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return models.Empolyee.objects.create_or_get(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        employee = super().update(instance, validated_data)

        return employee

