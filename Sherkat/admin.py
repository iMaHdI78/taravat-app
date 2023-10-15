from django.contrib import admin
from .models import general_company_information
from .models import company_insurance_information
from .models import tax_information
from .models import sahamdaran
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class general_company_informationAdmin(ImportExportModelAdmin):
    list_display = ('title', 
                    'national_id', 
                    'type_activity', 
                    'company_activity', 
                    'tel', 
                    'tel_fax',
                    'sarmaye', 
                    'company_registration_date',
                    'postal_code', 'office_address', 
                    'postal_code_factory', 
                    'office_factory',
                    )
    
    search_fields = ('title', 
                     'national_id', 
                     'tel', 
                     'type_activity',
                    )

    fields = (
        ('title', 
         'national_id', 
         'tel', 
         'tel_fax',
        ),

        ('type_activity', 
         'company_activity', 
         'company_registration_date',
         'sarmaye',
        ),

        ('postal_code', 
         'office_address', 
         'postal_code_factory', 
         'office_factory',
        ),
        ('docs',
         
        )
    )


class company_insurance_informationAdmin(ImportExportModelAdmin):
    list_display = ('name_sherkat', 
                    'username', 
                    'password',
                    'name_office_insurance_branch',
                    'office_insurance_workshop_code', 
                    'factory_insurance_workshop_code',
                    'name_factory_insurance_branch',
                    )
    
    search_fields = (
                     'office_insurance_workshop_code', 
                     'factory_insurance_workshop_code',

                    )
    
    fieldsets = (
        (
            None,
            {
                'fields': [
                'name_sherkat',
                ]
            },
        ),
        (
            'نام کاربری و رمز عبور',
            {
                'fields': [
                    (
                        'username',
                        'password',

                    ),
                ]
            },
        ),
        (
            'اطلاعات شعبات بیمه',
            {
                'fields': [
                    (
                        'name_office_insurance_branch',
                        'office_insurance_workshop_code',
                        'name_factory_insurance_branch',
                        'factory_insurance_workshop_code',
                    )
                ]
            },
        ),
        (
            'مدارک بیمه',
            {
                'fields': [
                    (
                        'docs',
                    )
                ]
            },
        ),
    )



class tax_informationAdmin(ImportExportModelAdmin):
    list_display = ('Tax_information',
                    'file_number',
                    'tax_center',
                    'tax_branch',
                    'tax_tracking_code',
                    'tax_address',
                    )
    
    search_fields = (
                     'tax_center', 
                     'tax_branch',
                     'username_value_information',
                     'username_quarterly_tax_information',
                     )
    
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
                        'file_number',
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
            'مدارک مالیاتی',
            {
                'fields': [
                    (
                        'docs',
                    )
                ]
            },
        ),
    )



class sahamdaranAdmin(ImportExportModelAdmin):
    list_display = (
                    'sherkat_sahamdaran',
                    'name_sahamdaran',
                    'family_name_sahamdaran',
                    'national_code_sahamdaran',
                    'semat_sahamdaran',
                    'noe_masoliat',
                    'percent_sahamdaran',
                    'number_sahamdaran',
                    'tarikh_ozviat',
                    'check_box',
                    'tarikh_payan',
                    'tel_sahamdaran',
                    'noe_shakhs',
                    'tarikh_tavalod',
                    'noe_tabeiat',
                    'sex',
                    'father_name',
                    'postal_code',
                    'address',
                    
    )
    
    search_fields = (
                     'name_sahamdaran',
                     'family_name_sahamdaran',
                     'national_code_sahamdaran',
                    )
    

    fieldsets = (
        (
            None,
            {
                'fields': [
                'sherkat_sahamdaran',
                ]
            },
        ),
        (
            'اطلاعات عمومی سهامداران',
            {
                'fields': [
                    (
                        'name_sahamdaran',
                        'family_name_sahamdaran',
                        'national_code_sahamdaran',
                        'tel_sahamdaran',
                        'tarikh_tavalod',
                        'father_name',
                        'sex',
                        'noe_tabeiat',
                        'noe_shakhs',
                        'check_box',
                        'postal_code',
                        'address',

                    ),
                ]
            },
        ),
        (
            'اطلاعات سهامی',
            {
                'fields': [
                    (
                        'percent_sahamdaran',
                        'number_sahamdaran',
                        'semat_sahamdaran',
                        'noe_masoliat',
                        'tarikh_ozviat',
                        'tarikh_payan',

                    )
                ]
            },
        ),
        (
            'مدارک سهامداران',
            {
                'fields': [
                    (
                        'docs',
                    )
                ]
            },
        ),
    )

admin.site.register(general_company_information,
                    general_company_informationAdmin)
admin.site.register(company_insurance_information,
                    company_insurance_informationAdmin)
admin.site.register(tax_information, 
                    tax_informationAdmin)
admin.site.register(sahamdaran, 
                    sahamdaranAdmin)
