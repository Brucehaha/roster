from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shift import views
from core.views import CeleryViewSet


router = DefaultRouter()
router.register('employees', views.EmployeeViewSet)
router.register('shifts', views.ShiftViewSet)
router.register('uploads', views.UploadViewSet, base_name='upload')
router.register('celery', CeleryViewSet)


app_name = 'shift'

urlpatterns = [
    path('', include(router.urls)),

]
