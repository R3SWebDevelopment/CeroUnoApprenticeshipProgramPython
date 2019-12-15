from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Country(models.Model):
    """
    Represents a country
    """
    name = models.CharField(max_length=100, unique=True)
    allow_billing = models.BooleanField(default=True, help_text='Allow billing from this country')
    allow_shipping = models.BooleanField(default=True, help_text='Allow shipping to this country')
    iso_code2 = models.CharField(max_length=2, unique=True, help_text='Two letter ISO code')
    iso_code3 = models.CharField(max_length=3, unique=True, help_text='Three letter ISO code')
    iso_numeric = models.IntegerField(help_text='Numeric ISO code')
    subject_to_vat = models.BooleanField(default=False, help_text='Is VAT applicable')
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    class Meta:
        ordering = ('display_order', 'name',)
        verbose_name_plural = 'Countries'

    def __unicode__(self):
        return self.name


class State(models.Model):

    """
    Represents a state
    """
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, help_text='Abbrevation')
    country = models.ForeignKey(Country)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    class Meta:
        ordering = ('display_order', 'name',)

    def __unicode__(self):
        return self.name


class Address(models.Model):
    """
    Represents a address for billing and shipping
    """
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name='your text')
    state = models.ForeignKey(State, null=True, blank=True)
    city = models.CharField(max_length=100)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, null=True, blank=True)
    zip_or_postal_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    fax_number = models.CharField(max_length=20, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __unicode__(self):
        address = '%s %s %s' % (self.first_name, self.last_name, self.address1)

        if self.address2:
            address += ' ' + self.address2

        address += ', ' + self.city

        if self.state:
            address += ', ' + unicode(self.state)

        if self.country:
            address += ', ' + unicode(self.country)

        return address

    def get_name(self):
        return '%s %s' % (self.first_name, self.last_name)
