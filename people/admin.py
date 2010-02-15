from django.contrib import admin
from people.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'date_of_birth', 'can_drink', 'call_delay')

admin.site.register(Person, PersonAdmin)