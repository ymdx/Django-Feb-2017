# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TasksAPI(ListCreateAPIView):
    """
    Lists (GET) and creates (POST) Tasks
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
