from django.contrib import admin
from .models import employee_information, File


# Register your models here.
class File_informationAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')
    search_fields = ('name', 'file')

    fields = ('name', 'file',),


admin.site.register(File, File_informationAdmin)


class employee_informationAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'name', 'family_name', 'national_code', 'birth_date',
                    'semat', 'noe_gharardad',
                    'address',
                    'postal_code',)
    search_fields = ('name', 'family_name', 'national_code', 'birth_date',)

    fields = (
        ('sherkat', 'profile_photo',),

        (
            'name',
            'family_name',
            'father_name',
            'national_code',
            'shenasname_code',
            'madrak_tahsili',
        ),

        (
            'tel',
            'mobile',
            'birth_date',
            'birth_place',
            'postal_code',
            'address'

        ),
        (
            'semat',
            'noe_gharardad',
            'mahale_faliat',
            'bimeh_code',
        ),
        (
            'docs',
        ),
    )


admin.site.register(employee_information, employee_informationAdmin)
