from django.contrib import admin
from .models import Industry,State,Job,ApplyJob
admin.site.register(State)
admin.site.register(Industry)
admin.site.register(Job)
admin.site.register(ApplyJob)
