from django.contrib import admin
from django.contrib.admin import register, ModelAdmin, SimpleListFilter
from .forms import OrganisationAdminForm
from .models import Address, EmailUser, EmailUserProfile, Organisation


@register(Address)
class AddressAdmin(ModelAdmin):
    list_filter = ('state', )
    search_fields = ('line1', 'line2', 'locality', 'postcode')


@register(EmailUser)
class EmailUserAdmin(ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')


class IdSuppliedListFilter(SimpleListFilter):
    """A custom list filter to return True/False, depending on whether an
    identification file has been uploaded on a profile.
    """
    title = 'ID supplied'
    parameter_name = 'id_supplied'

    def lookups(self, request, model_admin):
        return (('true', 'True'), ('false', 'False'))

    def queryset(self, request, queryset):
        if self.value() == 'true':
            return queryset.exclude(identification='')
        if self.value() == 'false':
            return queryset.filter(identification='')


class IdVerifiedListFilter(SimpleListFilter):
    """A custom list filter to return True/False, depending on whether the
    id_verified field contains a date or not.
    """
    title = 'ID verified'
    parameter_name = 'id_verified'

    def lookups(self, request, model_admin):
        return (('true', 'True'), ('false', 'False'))

    def queryset(self, request, queryset):
        if self.value() == 'true':
            return queryset.filter(id_verified__isnull=False)
        if self.value() == 'false':
            return queryset.filter(id_verified__isnull=True)


@register(EmailUserProfile)
class EmailUserProfileAdmin(ModelAdmin):
    list_display = ('emailuser', 'dob', 'id_supplied', 'id_verified', 'home_phone', 'work_phone', 'mobile')
    list_filter = (IdSuppliedListFilter, IdVerifiedListFilter)
    search_fields = ('emailuser__email', 'emailuser__first_name', 'emailuser__last_name')

    def id_supplied(self, obj):
        if obj.identification:
            return True
        return False


@register(Organisation)
class OrganisationAdmin(ModelAdmin):
    filter_horizontal = ('delegates', )
    form = OrganisationAdminForm
    list_display = ('name', 'abn')
    search_fields = ('name', 'abn')
