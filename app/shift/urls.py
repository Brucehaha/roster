from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shift import views


router = DefaultRouter()
router.register('employees', views.EmployeeViewSet)
router.register('shifts', views.ShiftViewSet)
router.register('uploads', views.UploadViewSet, base_name='upload')

app_name = 'shift'

urlpatterns = [
    path('', include(router.urls)),

]
