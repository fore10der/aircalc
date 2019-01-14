from django.contrib import admin
from .models import FH, Failture, Included, Removal
# Register your models here.
admin.site.register(FH)
admin.site.register(Failture)
admin.site.register(Included)
admin.site.register(Removal)

