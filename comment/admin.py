from django.contrib import admin
from .models import OwnerComment, RepositoryComment, Type, Status

# Register your models here.
admin.site.register(RepositoryComment)
admin.site.register(OwnerComment)
admin.site.register(Type)
admin.site.register(Status)
