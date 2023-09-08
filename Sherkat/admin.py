from django.contrib import admin
from .models import general_company_information
from .models import company_insurance_information
from .models import tax_information
# Register your models here.


class general_company_informationAdmin(admin.ModelAdmin):
    list_display = ('title', 'national_id', 'tel', 'type_activity',
                    'company_activity', 'company_registration_date',)
    search_fields = ('title', 'national_id', 'tel', 'type_activity',)

    fields = (
        ('title', 'national_id', 'tel', 'tel_fax',),
        ('type_activity', 'company_activity', 'company_registration_date',),
        ('postal_code', 'office_address', 'postal_code_factory', 'office_factory',),
        ('docs',)
    )


class company_insurance_informationAdmin(admin.ModelAdmin):
    list_display = ('Company_insurance_information', 'username', 'password',
                    'office_insurance_workshop_code', 'factory_insurance_workshop_code',)
    search_fields = ('Company_insurance_information',
                     'office_insurance_workshop_code', 'factory_insurance_workshop_code',)
    fields = (
        ('Company_insurance_information', 'username', 'password',),
        ('name_office_insurance_branch', 'office_insurance_workshop_code',),
        ('name_factory_insurance_branch', 'factory_insurance_workshop_code',),
        ('docs',)
    )


class tax_informationAdmin(admin.ModelAdmin):
    list_display = ('Tax_information',)
    search_fields = ('Tax_information', 'tax_center', 'tax_branch',
                     'username_value_information', 'username_quarterly_tax_information',)
    # fields = (
    #     ('tax_tracking_code', 'tax_address'),
    #     ('username_value_information', 'password_value_information',),
    #     ('username_quarterly_tax_information', 'password_quarterly_information')
    # )
    fieldsets = (
        (
            None,
            {
                'fields': [
                    'Tax_information',
                ]
            },
        ),
        (
            'ثبت مالیاتی',
            {
                'fields': [
                    (
                        'tax_center',
                        'tax_branch',
                    ),
                    (
                        'tax_tracking_code',
                        'tax_address',
                    ),
                ]
            },
        ),
        (
            'اطلاعات مالیات بر ارزش افزوده',
            {
                'fields': [
                    (
                        'username_value_information',
                        'password_value_information',
                    )
                ]
            },
        ),
        (
            'اطلاعات مالیات فصلی',
            {
                'fields': [
                    (
                        'username_quarterly_tax_information',
                        'password_quarterly_information',
                    )
                ]
            },
        ),
        (
            'مدارک مالیاتی بمولا',
            {
                'fields': [
                    (
                        'docs',
                    )
                ]
            },
        ),
    )


admin.site.site_header = 'برنامه مدیریت اطلاعات شرکت و کارمندان آرشا'

admin.site.register(general_company_information,
                    general_company_informationAdmin)
admin.site.register(company_insurance_information,
                    company_insurance_informationAdmin)
admin.site.register(tax_information, tax_informationAdmin)
