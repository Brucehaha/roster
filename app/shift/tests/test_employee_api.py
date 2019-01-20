from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Employee

from shift.employee_serializer import EmployeeSerializer


EMPLOYEE_URL = reverse('shift:employee-list')


class PublicEmployeesApiTests(TestCase):
    """Test the publicly available employees API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login required for retrieving employees"""
        res = self.client.get(EMPLOYEE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateEmployeesApiTests(TestCase):
    """Test the authorized user employees API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@test.com',
            'password123'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_employees(self):
        """Test retrieving employees"""
        Employee.objects.create(first_name="fem1", last_name='lem1')
        Employee.objects.create(first_name="fem2", last_name="lem2")
        res = self.client.get(EMPLOYEE_URL)
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_employee_successful(self):
        """Test creating a new tag"""
        payload = {'first_name': "fem4", 'last_name': 'lem4'}
        self.client.post(EMPLOYEE_URL, payload)

        exists = Employee.objects.filter(
            first_name='fem4',
            last_name='lem4'
        ).exists()
        self.assertTrue(exists)

    def test_create_tag_invalid(self):
        """Test creating a new tag with invalid payload"""
        payload = {'first_name': ''}
        res = self.client.post(EMPLOYEE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
