from django.shortcuts import render, HttpResponse

from .celery_serializer import CelerySerializer
from . import models

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


from celery.result import AsyncResult
from .tasks import add, mul


def celery_res(task_id):
    res = AsyncResult(id=task_id)
    return res.get()


def add_test():
    task = add.delay(4, 22)
    return task.id

def mul_test():
    task = mul.delay(4, 22)
    return task.id


class CeleryViewSet(viewsets.ModelViewSet):
    """save celery task id and result to database"""
    serializer_class = CelerySerializer
    queryset = models.CeleryTask.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def perform_create(self, serializer):
        """
        create task id and save it to CeleryTask model
        """
        function = serializer.validated_data['function']
        if function == 1:
            res = add_test()
        else:
            res = mul_test()
        serializer.save(task=res)

    @action(methods=['GET'], detail=True, url_path='get-result')
    def Get_Result(self, request, pk=None):

        celery_obj = self.get_object()
        print(celery_obj)
        serializer = self.get_serializer(celery_obj, data=request.data)

        if serializer.is_valid():
            task_id = celery_obj.task
            print(task_id)

            try:
                res = celery_res(task_id)
                print(res)
            except Exception as e:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer.save(task=task_id, result=res)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
    )
