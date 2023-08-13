from django.core.management import BaseCommand

from main.models import Students


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'first_name': 'Ivan', 'last_name': 'Ivanov'},
            {'first_name': 'Cemen', 'last_name': 'Semenov'},
            {'first_name': 'Dmitry', 'last_name': 'Dmitriev'}
        ]

        for student in student_list:
            Students.objects.create(**student)