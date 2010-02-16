from datetime import date, timedelta
from celery.task import Task, PeriodicTask
from people.models import Person

class CanDrinkTask(Task):
    """
    A task that determines if a person is 21 years of age or older.
    """
    def run(self, person_id, **kwargs):
        logger = self.get_logger(**kwargs)
        logger.info("Running determine_can_drink task for person %s" % person_id)
    
        person = Person.objects.get(pk=person_id)
        now = date.today()
        diff = now - person.date_of_birth
        # i know, i know, this doesn't account for leap year
        age = diff.days / 365
        if age >= 21:
            person.can_drink = True
            person.save()
        else:
            person.can_drink = False
            person.save()
        return True
    
class FullNameTask(PeriodicTask):
    """
    A periodic task that concatenates fields to form a person's full name.
    """
    run_every = timedelta(seconds=60)

    def run(self, **kwargs):
        logger = self.get_logger(**kwargs)
        logger.info("Running full name task.")
        
        for person in Person.objects.all():
            person.full_name = " ".join([person.prefix, person.first_name,
                                         person.middle_name, person.last_name,
                                         person.suffix]).strip()
            person.save()
        return True
