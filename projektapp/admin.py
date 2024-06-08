from django.contrib import admin
from .models import Ctenar, Pujcka, Knihovna, Knihovnik, Rezervace

admin.site.register(Ctenar)
admin.site.register(Pujcka)
admin.site.register(Knihovna)
admin.site.register(Knihovnik)
admin.site.register(Rezervace)