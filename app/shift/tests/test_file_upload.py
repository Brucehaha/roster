from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from core import models
from rest_framework import status
from rest_framework.test import APIClient
import os
import tempfile
from django.conf import settings

class UploadFileTests(TestCase):
    """Test the authorized  user could upload file"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@test.com',
            'password123'
            'name'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_upload_file(self):
        """
        Test if we can upload a photo
        """
        """Test uploading an image to recipe"""
        url = reverse('shift:upload-list')
        with tempfile.NamedTemporaryFile(suffix='.txt') as temp:
            temp.write(b'Hello world!')
            temp.seek(0)
            res = self.client.post(url, {'doc': temp}, format='multipart')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn('doc', res.data)
        name = os.path.basename(res.data['doc'])
        path = os.path.join(settings.BASE_DIR, 'media/doc/'+name)
        self.assertTrue(os.path.exists(path))

