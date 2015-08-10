from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=64, verbose_name='Name', unique=True)

    class Meta:
        verbose_name_plural = 'Cities'
        ordering = ['name']

    def __str__(self):
        return self.name


class ZipCode(models.Model):
    city = models.ForeignKey(City, verbose_name='City')
    zip_code = models.CharField(max_length=8, verbose_name='Zip code', unique=True)

    class Meta:
        verbose_name_plural = 'Zip Codes'
        ordering = ['zip_code']

    def __str__(self):
        return str(self.city) + ', ' + self.zip_code


class Owner(models.Model):
    serial = models.BigIntegerField(verbose_name='Serial')
    name = models.CharField(max_length=255, verbose_name='Name')
    address = models.CharField(null=True, blank=True, max_length=128, verbose_name='Address')
    address_line2 = models.CharField(null=True, blank=True, max_length=128, verbose_name='Address line 2')
    zip_code = models.ForeignKey(ZipCode, null=True, blank=True, verbose_name='Zip code')

    class Meta:
        verbose_name_plural = 'Owners'
        ordering = ['name']

    def __str__(self):
        return self.name

    def extended_name(self):
        final_string = self.name
        final_address = self.address
        if final_address and self.zip_code:
            final_address += ', ' + str(self.zip_code)

        if final_string and final_address:
            final_string += ' - ' + final_address

        if not final_string:
            final_string = _('None')
        return final_string


class Repository(models.Model):
    serial = models.BigIntegerField(verbose_name='Serial')
    name = models.CharField(max_length=255, verbose_name='Name')
    marketing = models.BooleanField(default=False, verbose_name='Marketing')
    status = models.CharField(max_length=16, null=True, verbose_name='Status')
    date = models.CharField(max_length=16, null=True, blank=True, verbose_name='Date')

    owner = models.ForeignKey(Owner, null=True, blank=True, verbose_name='Owner')
    owner_serial = models.BigIntegerField(verbose_name='Owner Serial')
    owner_name = models.CharField(max_length=255, verbose_name='Owner name')
    city = models.CharField(max_length=64, verbose_name='City')
    street = models.CharField(max_length=64, null=True, blank=True, verbose_name='Street')
    house = models.CharField(max_length=8, null=True, blank=True, verbose_name='House')
    pob = models.CharField(null=True, blank=True, max_length=8, verbose_name='P.O.B')
    zip_code = models.CharField(max_length=8, verbose_name='Zip code')

    class Meta:
        verbose_name_plural = 'Repositories'
        ordering = ['name']

    def __str__(self):
        return self.name
