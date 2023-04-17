# Rest-Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Project
from apps.main.center.models import Center
from apps.main.teacher.models import Teacher
from apps.main.courses.models import Course
from apps.main.address.models import Address
from apps.main.center.serializers import CenterCreateSerializer


class CenterCreateAPIView(APIView):
    model = Center
    queryset = Center.objects.all()
    serializer_class = CenterCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get('name')
        top_teachers = serializer.validated_data['top_teachers']
        courses = serializer.validated_data['courses']

        center_address, created = Address.objects.get_or_create(**serializer.validated_data['center_address'])

        check_center = Center.objects.filter(name=name)
        if check_center.exists():
            return Response({
                'status_code': 400,
                'message': 'Center Exists'
            }, status=status.HTTP_400_BAD_REQUEST)

        center = Center.objects.create(
            name=name,
            slug=serializer.validated_data.get('slug'),
            center_address=center_address,
            main_course=serializer.validated_data.get('main_course'),
            image=serializer.validated_data.get('image'),
            is_public=serializer.validated_data.get('is_public', False)
        )
        center.save()

        for item in top_teachers:
            teacher, created = Teacher.objects.get_or_create(
                name=item.get('name'),
                description=item.get('description'),
                experience_year=item.get('experience_year'),
                image=item.get('image', None),
                number_students=item.get('number_students'),
            )
            center.top_teachers.add(teacher)

        for item in courses:
            course = Course.objects.get(name=item.name)
            center.courses.add(course.id)

        center.save()

        return Response({
            'status_code': 201,
            'message': 'Created',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
