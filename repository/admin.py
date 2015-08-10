from django.contrib import admin
from .models import Repository, Owner, City, ZipCode


class RepositoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['name']


# Register your models here.
admin.site.register(Repository, RepositoryAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(ZipCode)
admin.site.register(City)
