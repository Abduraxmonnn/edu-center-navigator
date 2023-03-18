# Rest-Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

# Project
from apps.main.teacher.models import Teacher
from apps.main.teacher.serializers.teacher_serializer import TeacherSerializer


class TeacherCreateViewSet(viewsets.GenericViewSet,
                           mixins.CreateModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminUser]


class TeacherListViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]


class TeacherRetrieveViewSet(viewsets.GenericViewSet,
                             mixins.RetrieveModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeacherUpdateViewSet(viewsets.GenericViewSet,
                           mixins.UpdateModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminUser]


class TeacherDestroyViewSet(viewsets.GenericViewSet,
                            mixins.DestroyModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminUser]
