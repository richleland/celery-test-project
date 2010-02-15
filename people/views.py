from django.http import HttpResponse
from people.tasks import CanDrinkTask

def call_celery_delay(request, person_id):
    CanDrinkTask.delay(person_id)
    return HttpResponse("Task set to execute.")