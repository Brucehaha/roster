from employee.employee_serializer import EmployeeSerializer
from core import models
from rest_framework import generics, authentication, permissions, mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class EmployeeViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin):
    """Manage ingredients in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeSerializer
