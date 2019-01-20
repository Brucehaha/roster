from .employee_serializer import EmployeeSerializer, ShiftSerializer, UploadSerializer
from .utils import ShiftFilter
from core import models

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.conf import settings
from django.db import transaction

import os
import csv


class EmployeeViewSet(viewsets.ModelViewSet):
    """Manage ingredients in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeSerializer


class ShiftViewSet(viewsets.ModelViewSet):
    """Manage ingredients in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.Shift.objects.all()
    serializer_class = ShiftSerializer

    def create(self, request, *args, **kwargs):
        """
        rewrite create method for CreateModelMixin, to create valid shift for a employee
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        status_code = status.HTTP_406_NOT_ACCEPTABLE
        data = {}

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = ShiftFilter(serializers=serializer).respond()
        is_passed = response['status']
        data['error_message'] = response['error_message']
        print(response)
        headers = None
        if is_passed:
            self.perform_create(serializer)
            data = serializer.data
            status_code = status.HTTP_201_CREATED
            headers = self.get_success_headers(serializer.data)
        return Response(data, status=status_code, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class UploadViewSet(viewsets.ModelViewSet):
    """upload employee file to database"""
    serializer_class = UploadSerializer
    queryset = models.Task.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        """
        rewrite create method for CreateModelMixin, get return value data, and status code
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data, status_code = self.perform_create(serializer)
        print(status_code)
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status_code, headers=headers)

    def perform_create(self, serializer):
        """
         post-save employee to employee table after upload empolyee.csv
        :param serializer: save and get isntance
        :return: message and status code
        """
        data = serializer.data
        status_code = status.HTTP_201_CREATED
        instance = serializer.save()
        path = os.path.join(settings.MEDIA_ROOT, str(instance.doc))
        employees_list =[]
        employees = models.Employee.objects.all()

        with open(path, newline='') as file:
            chunk = csv.reader(file, delimiter=',')
            next(file) # skip header
            for row in chunk:
                fname, lname = row
                is_existed = employees.filter(first_name=fname, last_name=lname)
                if not is_existed:
                    employees_list.append(models.Employee(first_name=fname, last_name=lname))
        try:
            with transaction.atomic():
                models.Employee.objects.bulk_create(employees_list)
        except Exception as e:
            print(e)
            data = {"message": str(e)}
            status_code=status.HTTP_406_NOT_ACCEPTABLE
        return data, status_code

