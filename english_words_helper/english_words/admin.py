from django.contrib import admin
from .models import Words, Topics, Levels, IrregularVerbs

admin.site.register(Words)
admin.site.register(Topics)
admin.site.register(Levels)
admin.site.register(IrregularVerbs)
