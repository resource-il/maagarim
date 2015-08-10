from django.db import models
from django.contrib.auth.admin import User
from repository.models import Repository, Owner

# Create your models here.
class Type(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return self.type


class Status(models.Model):
    status = models.CharField(max_length=32, verbose_name='Status')
    published = models.BooleanField(default=False, verbose_name='Published')

    class Meta:
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.status


class Comment(models.Model):
    subject = models.CharField(max_length=255, verbose_name='Subject')
    content = models.TextField(verbose_name='Content')
    type = models.ForeignKey(Type, verbose_name='Type')
    status = models.ForeignKey(Status, verbose_name='Status')
    full_name = models.CharField(max_length=128, verbose_name='Full Name')
    email = models.EmailField(verbose_name='Email')
    ip_address = models.CharField(max_length=64, verbose_name='IP Address')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')
    updated_by = models.ForeignKey(User, null=True, blank=True, verbose_name='Updated By')
    edited_flag = models.BooleanField(default=False, verbose_name='Edited Flag')

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.subject


class RepositoryComment(Comment):
    repository = models.ForeignKey(Repository, verbose_name='Repository', related_name='+')

    class Meta:
        verbose_name_plural = 'Repository Comments'


class OwnerComment(Comment):
    owner = models.ForeignKey(Owner, verbose_name='Owner', related_name='+')

    class Meta:
        verbose_name_plural = 'Owner Comments'
