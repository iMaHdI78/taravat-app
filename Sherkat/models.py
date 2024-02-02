from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels
from django.core.validators import FileExtensionValidator
from django.forms import ModelForm, PasswordInput

# Create your models here.

# این کلاس برای  دیتا بیس اطلاعات عمومی شرکت ها ایجاد شده است

class File(models.Model):
    def __str__(self) -> str:
        return self.name

    name = models.CharField(
        max_length=100, verbose_name="نام مدرک", blank=True, null=True)
    file = models.FileField(upload_to='karmandan/files/', blank=True, null=True, verbose_name='فایل',
                            validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])])

    class Meta:
        verbose_name = "بارگذاری مدارک"
        verbose_name_plural = "بارگذاری مدارک"
        db_table = 'File'

        
class general_company_information(models.Model):
    TYPE_ACTIVITY_CHOICES = (
        ('sa', 'سهامی عام',),
        ('sakh', 'سهامی خاص',),
        ('m', 'مسئولیت محدود',),
        ('n', 'نسبی',),
        ('t', 'تضامنی',),
        ('s', 'سهامی',),
        ('ghs', 'غیر سهامی',),
        ('ttm', 'تعاونی تولید و مصرف',),

    )

    TYPE_COMPANY_CHOICES = (
        ('T', 'تولیدی'),
        ('B', 'بازرگانی'),
        ('KH', 'خدماتی'),
        ('P', 'پیمانکاری'),
    )
    
    sarmaye = models.CharField(max_length=100,
         verbose_name='سرمایه شرکت', blank=True, null=True)
    title = models.CharField(max_length=100, unique=True,
                             verbose_name='نام شرکت / موسسه', null=True)
    national_id = models.CharField(
        max_length=20, verbose_name='شناسه ملی', null=True)
    tel = models.CharField(
        max_length=12, verbose_name='شماره تماس', blank=True, null=True)
    tel_fax = models.CharField(
        max_length=12, verbose_name='شماره فکس', blank=True, null=True)
    type_activity = models.CharField(
        max_length=4, choices=TYPE_ACTIVITY_CHOICES, verbose_name='نوع شرکت', null=True)
    company_activity = models.CharField(
        max_length=2, choices=TYPE_COMPANY_CHOICES, verbose_name='فعالیت شرکت', null=True)

    company_registration_date = jmodels.jDateField(
        verbose_name='تاریخ ثبت شرکت', blank=True, null=True)

    postal_code = models.CharField(
        max_length=20, verbose_name='کد پستی دفتر', blank=True, null=True)

    office_address = models.TextField(
        max_length=100, verbose_name='آدرس دفتر', blank=True, null=True)

    postal_code_factory = models.CharField(
        max_length=20, verbose_name='کد پستی کارخانه', blank=True, null=True)
    office_factory = models.TextField(
        max_length=100, verbose_name='آدرس کارخانه', blank=True, null=True)

    
    docs = models.ManyToManyField(
        File,
        blank=True,
        related_name='sherkat',
        verbose_name='مدارک'
    )

    class Meta:
        verbose_name = 'اطلاعات عمومی شرکت'
        verbose_name_plural = 'اطلاعات عمومی شرکت ها'
        db_table = 'general_company_information'

    def __str__(self) -> str:
        try:
            return self.title
        except:
            return 'بدون عنوان'


# این کلاس برای  دیتا بیس اطلاعات بیمه ای شرکت ها ایجاد شده است
class company_insurance_information(models.Model):
    name_sherkat = models.ForeignKey(
        general_company_information, null=True, related_name='company_insurance_information', verbose_name='نام شرکت / موسسه', on_delete=models.SET_NULL)
    username = models.CharField(
        max_length=20, verbose_name='نام کاربری', blank=True, null=True)
    password = models.CharField(
        max_length=20, verbose_name='رمز عبور', blank=True, null=True)
    # password = forms.CharField(widget=PasswordInput())
    name_office_insurance_branch = models.CharField(
        max_length=30, verbose_name='نام شعبه ی بیمه دفتر', blank=True, null=True)
    office_insurance_workshop_code = models.CharField(
        max_length=20, unique=True, verbose_name='کد کارگاهی بیمه دفتر', blank=True, null=True)
    name_factory_insurance_branch = models.CharField(
        max_length=30, verbose_name='نام شعبه ی بیمه کارخانه', blank=True, null=True)
    factory_insurance_workshop_code = models.CharField(
        max_length=20, unique=True, verbose_name='کد کارگاهی بیمه کارخانه', blank=True, null=True)

    
    docs = models.ManyToManyField(
        File,
        blank=True,
        verbose_name='مدارک'
    )

    class Meta:
        verbose_name = 'اطلاعات بیمه ای شرکت'
        verbose_name_plural = 'اطلاعات بیمه ای شرکت ها'
        db_table = 'company_insurance_information'

    def __str__(self) -> str:
        try:
            return self.Company_insurance_information.title
        except:
            return 'بدون عنوان'

# این کلاس برای  دیتا بیس اطلاعات مالیاتی شرکت ها ایجاد شده است


class tax_information(models.Model):
    Tax_information = models.ForeignKey(general_company_information, null=True,
                                        related_name='tax_information', verbose_name='نام شرکت / موسسه', on_delete=models.SET_NULL)
    file_number = models.CharField(
        max_length=100, unique=True, verbose_name='کلاسه(شماره پرونده)', blank=True, null=True)
    tax_center = models.CharField(
        max_length=100, verbose_name='مرکز مالیاتی', blank=True, null=True)
    tax_branch = models.CharField(
        max_length=100, verbose_name='حوزه مالیاتی', blank=True, null=True)
    tax_tracking_code = models.CharField(
        max_length=100, verbose_name='کد رهگیری مالیاتی', blank=True, null=True)
    tax_address = models.TextField(
        max_length=100, verbose_name='آدرس حوزه مالیاتی', blank=True, null=True)

#اطلاعات مالیات بر ارزش افزوده
    username_value_information = models.CharField(
        max_length=100, unique=True, verbose_name='(نام کاربری)', blank=True, null=True)
    password_value_information = models.CharField(
        max_length=100, unique=True, verbose_name='(رمز عبور)', blank=True, null=True)

    #اطلاعات مالیات فصلی 169
    username_quarterly_tax_information = models.CharField(
        max_length=100, unique=True, verbose_name='(نام کاربری)', blank=True, null=True)
    password_quarterly_information = models.CharField(
        max_length=100, unique=True, verbose_name='(رمز عبور)', blank=True, null=True)

    docs = models.ManyToManyField(
        File,
        blank=True,
        verbose_name='مدارک'
    )

    class Meta:
        verbose_name = 'اطلاعات مالیاتی شرکت'
        verbose_name_plural = 'اطلاعات مالیاتی شرکت ها'
        db_table = 'tax_information'

    def __str__(self) -> str:
        try:
            return self.Tax_information.title
        except:
            return 'بدون عنوان'




class sahamdaran(models.Model):

    NOE_SHAKHS = (
        ('ho' , 'حقوقی'),
        ('ha', 'حقیقی'),
    )

    SEX = (
        ('f', 'زن'),
        ('m', 'مرد'),
    )

    shenasname_file_sahamdar = models.FileField(upload_to='karmandan/shenasname/', blank=True, null=True, verbose_name='فایل شناسنامه',
                                        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])])
    
    cartmeli_file_sahamdar = models.FileField(upload_to='karmandan/melicard/', blank=True, null=True, verbose_name='فایل کارت ملی',
                                        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])])

    sherkat_sahamdaran = models.ForeignKey(general_company_information, null=True,
        related_name='sahamdaran', verbose_name='نام شرکت / موسسه', on_delete=models.SET_NULL)
    name_sahamdaran = models.CharField(
        max_length=20, verbose_name='نام سهامدار', null=True)
    family_name_sahamdaran = models.CharField(
        max_length=20, verbose_name='نام خانوادگی سهامدار', null=True)
    national_code_sahamdaran = models.CharField(
        max_length=10, verbose_name='کد ملی سهامدار', blank=True, null=True)
    number_sahamdaran = models.CharField(
        max_length=100, verbose_name='مبلغ سرمایه گذاری/تعداد سهام', null=True)
    percent_sahamdaran = models.CharField(
        max_length=100, verbose_name='درصد سهام', blank=True, null=True)
    tel_sahamdaran = models.CharField(
        max_length=11, verbose_name='تلفن همراه' ,blank=True ,null = True)
    semat_sahamdaran = models.CharField(
        max_length=20, verbose_name='سمت' ,blank=True ,null = True)
    noe_masoliat = models.CharField(
        max_length=20, verbose_name='نوع مسئولیت' ,blank=True ,null = True)
    tarikh_ozviat = jmodels.jDateField(
        verbose_name='تاریخ عضویت', blank=True, null=True)
    tarikh_payan = jmodels.jDateField(
        verbose_name='پایان کار', blank=True, null=True)
    tarikh_tavalod = jmodels.jDateField(
        verbose_name='تاریخ تولد', blank=True, null=True)
    postal_code = models.CharField(
        max_length=20, verbose_name='کد پستی' ,blank=True ,null = True)
    address = models.TextField(
        max_length=100, verbose_name='آدرس' ,blank=True ,null = True)
    father_name = models.CharField(
        max_length=20, verbose_name='نام پدر' ,blank=True ,null = True)
    noe_tabeiat = models.CharField(
        max_length=20, verbose_name='تابعیت شخص' ,blank=True ,null = True)
    noe_shakhs = models.CharField(
        max_length=2, choices=NOE_SHAKHS, verbose_name='نوع شخص', null=True)
    sex = models.CharField(
        max_length=2, choices=SEX, verbose_name='جنسیت', null=True)
    check_box = models.BooleanField(
        default=1,verbose_name='دارای فعالیت',blank=True ,null = True)

    docs = models.ManyToManyField(
        File,
        blank=True,
        verbose_name='مدارک'
    )

    class Meta:
        verbose_name = 'اطلاعات سهامداران شرکت'
        verbose_name_plural = 'اطلاعات سهامداران شرکت ها'
        db_table = 'sahamdaran'

    def __str__(self) -> str:
        try:
            return self.sahamdaran.title
        except:
            return 'بدون عنوان'