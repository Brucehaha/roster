from rest_framework import serializers
from core import models


class ShiftSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize the employee object"""
    employee = serializers.PrimaryKeyRelatedField(
        queryset=models.Employee.objects.all(),
    )

    class Meta:
        model = models.Shift
        fields = ('id', 'date', 'break_time', 'shift_type', 'store_type', 'employee')
        read_only_fields = ('id',)


class EmployeeSerializer(serializers.ModelSerializer):
    """Serialize the employee object"""
    shifts = ShiftSerializer(many=True, read_only=True)

    class Meta:
        model = models.Employee
        fields = ('id', 'first_name', 'last_name', 'shifts')
        read_only_fields = ('id',)

    def create(self, validated_data):
        employee = models.Employee.objects.create(**validated_data)
        return employee


class UploadSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize the doc object"""
    doc = serializers.FileField(max_length=None)
    # url = serializers.HyperlinkedIdentityField(view_name="shift:upload-detail")
    class Meta:
        model = models.Task
        fields = ('id', 'doc')
