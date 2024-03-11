from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializers,UserSerializers
from .models import Task
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
# Create your views here.
class Taskviewset(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset=Task.objects.all().order_by('-date_created')
	serializer_class=TaskSerializers

class CreateUserview(CreateAPIView):
	model=get_user_model()
	permission_classes = (AllowAny,)
	serializer_class = UserSerializers
class DueTaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
	serializer_class = TaskSerializers

class CompletedTaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
	serializer_class = TaskSerializers