from django.contrib import admin

from . models import Place
from . models import Team
from . models import Argent

# Register your models here.
admin.site.register(Place)
admin.site.register(Team)
admin.site.register(Argent)