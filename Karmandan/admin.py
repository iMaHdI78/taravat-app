from django.contrib import admin
from .models import employee_information, File
from .models import phone_book
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class File_informationAdmin(admin.ModelAdmin):
    list_display = ('name', 
                    'file'
                    )
    search_fields = ('name', 
                     'file'
                     )

    fields = ('name', 
              'file',
              ),

class phone_bookkAdmin(ImportExportModelAdmin):
    list_display = ('name_sherkat', 
                    'name_phonebook', 
                    'family_name_phonebook', 
                    'tel_phonebook',
                    'fax_phonebook', 
                    'dakheli_phonebook', 
                    'mobile_phonebook', 
                    'semat_phonebook', 
                    'email_phonebook', 
                    'rabet_name_phonebook', 
                    'address_phonebook', 
                    'postal_code_phonebook'
                    )
    
    search_fields = ('name_sherkat',
                     'name_phonebook',
                       'family_name_phonebook', 
                       'tel_phonebook', 
                       'mobile_phonebook',
                       'email_phonebook',
                       'rabet_name_phonebook'
                    )

    fields = (
        ('name_phonebook', 
         'family_name_phonebook', 
         'tel_phonebook', 
         'mobile_phonebook',
         ),

        ('name_sherkat', 
         'semat_phonebook', 
         'dakheli_phonebook',
         'fax_phonebook',
         ),

        ('email_phonebook', 
         'rabet_name_phonebook',
         ),

        ('address_phonebook',
         'postal_code_phonebook'
         ),
        
        
    )

class employee_informationAdmin(ImportExportModelAdmin):
    list_display = ('image_tag', 
                    'sherkat', 
                    'name', 
                    'family_name', 
                    'national_code',
                    'shenasname_code',
                    'birth_date',
                    'mahale_faliat',
                    'semat',
                    'start_date', 
                    'check_box',
                    'bimeh_code',
                    'noe_gharardad',
                    'madrak_tahsili',
                    'reshte_tahsili',
                    'marital_status',
                    'sex',
                    'tedade_farzand',
                    'mobile',
                    'birth_place',
                    'father_name',
                    'address',
                    'tel',
                    'postal_code',
                    )
    
    search_fields = ('name', 
                     'family_name', 
                     'national_code', 
                     'birth_date',
                     )

    fieldsets = (
        (
            None,
            {
                'fields': [
                    (
                'sherkat',
                'profile_photo',

                    )

                ]
            },
        ),
        (
            'اطلاعات عمومی پرسنل',
            {
                'fields': [
                    (
                        'name',
                        'family_name',
                        'father_name',
                        'national_code',
                        'cartmeli_file',
                        'shenasname_code',
                        'shenasname_file',
                        'sex',
                        'madrak_tahsili',
                        'madrak_file',
                        'reshte_tahsili',
                        'tel',
                        'mobile',
                        'birth_date',
                        'birth_place', 
                        'marital_status',
                        'tedade_farzand',
                        'check_box',

                    ),
                    (
                        'postal_code',
                        'address',
                    ),
                ]
            },
        ),
        (
            'اطلاعات حوزه ی فعالیت',
            {
                'fields': [
                    (
                        'semat',
                        'noe_gharardad',
                        'gharardad_file',
                        'mahale_faliat',
                        'bimeh_code',
                        'bimeh_file',
                        'start_date',
                        'end_date_of_work',
                        
                    )
                ]
            },
        ),

        (
            'مدارک پرسنل',
            {
                'fields': [
                    (
                        'docs',
                    )
                ]
            },
        ),
    )


admin.site.register(employee_information, employee_informationAdmin)
admin.site.register(File, File_informationAdmin)
admin.site.register(phone_book, phone_bookkAdmin)