from django.contrib import admin
from .models import Appointment, Doctor, News, Contact, Comment


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("headline,")}

admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(News)
admin.site.register(Contact)
admin.site.register(Comment)