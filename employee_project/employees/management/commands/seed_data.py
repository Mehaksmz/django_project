from django.core.management.base import BaseCommand
from faker import Faker
import random
from employees.models import Employee, Department, Performance
from attendance.models import Attendance

fake = Faker()

class Command(BaseCommand):
    help = 'Seed database with dummy employees'

    def handle(self, *args, **kwargs):
        departments = ['HR', 'Engineering', 'Sales', 'Marketing']
        for dept in departments:
            Department.objects.get_or_create(name=dept)

        for _ in range(50):
            dept = Department.objects.order_by('?').first()
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                date_joined=fake.date_between(start_date='-2y', end_date='today'),
                department=dept,
            )
            # Attendance
            for _ in range(10):
                Attendance.objects.create(
                    employee=employee,
                    date=fake.date_between(start_date='-3mo', end_date='today'),
                    status=random.choice(['Present', 'Absent', 'Late'])
                )
            #Performance
            Performance.objects.create(
                employee=employee,
                rating=random.randint(1, 5),
                review_date=fake.date_between(start_date='-6mo', end_date='today')
            )
