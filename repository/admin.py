from django.contrib import admin
from .models import Repository, Owner, City, ZipCode


class RepositoryAdmin(admin.ModelAdmin):
    search_fields = ['name', 'owner_name']
    list_display = ('name', 'owner_name', 'owner', 'marketing', 'status',)
    list_filter = ('status', 'marketing', 'owner',)


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'address', 'zip_code',)
    list_filter = ('zip_code__city',)


# Register your models here.
admin.site.register(Repository, RepositoryAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(ZipCode)
admin.site.register(City)
