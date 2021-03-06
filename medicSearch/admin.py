from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'birthday',)
    list_display_links = ('user', 'role',)
    empty_value_display = 'Vazio'

admin.site.register(Profile, ProfileAdmin)
admin.site.register(State) 
admin.site.register(City) 
admin.site.register(Neighborhood) 
admin.site.register(Address) 
admin.site.register(DayWeek) 
admin.site.register(Rating) 
admin.site.register(Speciality)
