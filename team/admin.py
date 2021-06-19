from django.contrib import admin

# Register your models here.
from team.models import *

admin.site.register(Team)
admin.site.register(TeamMember)