from rest_framework import viewsets
from .models import Employee, Department, Performance
from .serializers import EmployeeSerializer, DepartmentSerializer, PerformanceSerializer
from django.http import JsonResponse
from django.db.models import Count
from attendance.models import Attendance
from employees.models import Department, Employee
from datetime import datetime
from django.db.models.functions import TruncMonth

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = ['department', 'date_joined']
    ordering_fields = ['date_joined', 'name']

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

def employees_per_department(request):
    data = (
        Department.objects
        .annotate(emp_count=Count('employees'))
        .values_list('name', 'emp_count')
    )
    labels, counts = zip(*data) if data else ([], [])
    return JsonResponse({'labels': labels, 'data': counts})


def monthly_attendance(request):
    qs = (
        Attendance.objects
        .filter(date__year=datetime.now().year)
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    labels = [item['month'].strftime('%B') for item in qs]
    data = [item['count'] for item in qs]
    return JsonResponse({'labels': labels, 'data': data})
