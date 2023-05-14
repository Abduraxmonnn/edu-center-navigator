# Rest-Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Project
from apps.main.branch.models import Branch
from apps.main.courses.models import Course
from apps.main.address.models import Address
from apps.main.branch.serializers import BranchCreateSerializer


class BranchCreateAPIView(APIView):
    model = Branch
    queryset = Branch.objects.all()
    serializer_class = BranchCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get('name')
        slug = serializer.validated_data.get('slug')
        center = serializer.validated_data.get('center')
        image = serializer.validated_data.get('image')
        courses = serializer.validated_data.get('courses')
        is_public = serializer.validated_data.get('is_public')

        branch_address, created = Address.objects.get_or_create(**serializer.validated_data.pop('branch_address'))

        check_branch = Branch.objects.filter(name=name, branch_address__street=branch_address.street)
        if check_branch.exists():
            return Response({
                'status_code: ': 400,
                'message': 'Branch Already Exists'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            branch = Branch.objects.create(
                name=name,
                slug=slug,
                center=center,
                branch_address=branch_address,
                image=image,
                is_public=is_public
            )
            branch.save()
        except Exception as ex:
            return Response({
                'status_code: ': 400,
                'message: ': 'Branch not Created, Please Make Sure All Field is Correct',
                'error_message: ': ex
            }, status=status.HTTP_400_BAD_REQUEST)

        for item in courses:
            course = Course.objects.get(name=item.name)
            center.courses.add(course.id)

        branch.save()
        return Response({
            'status_code: ': 201,
            'message: ': 'Created',
            'data: ': serializer.data
        }, status=status.HTTP_201_CREATED)
