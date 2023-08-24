from django.contrib import admin
from .models import ApplicationFormModel


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "date", "occupation")
    search_fields = ("first_name", "last_name", "occupation")
    list_filter = ("date", "occupation")
    readonly_fields = ("occupation",)


admin.site.register(ApplicationFormModel, ApplicationAdmin)
