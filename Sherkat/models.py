from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels
from django.core.validators import FileExtensionValidator

# Create your models here.

# این کلاس برای  دیتا بیس اطلاعات عمومی شرکت ها ایجاد شده است

class File(models.Model):
    def __str__(self) -> str:
        return self.name

    # karmand = models.ForeignKey(employee_information, blank=True, null=True,
                                # related_name='files', verbose_name=' نام و نام خانوادگی ', on_delete=models.SET_NULL)
    name = models.CharField(
        max_length=100, verbose_name="نام مدرک", blank=True, null=True)
    file = models.FileField(upload_to='karmandan/files/', blank=True, null=True, verbose_name='فایل',
                            validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])])

    class Meta:
        verbose_name = "بارگذاری مدارک"
        verbose_name_plural = "بارگذاری مدارک"
        
        
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

    def __str__(self) -> str:
        try:
            return self.title
        except:
            return 'بدون عنوان'


# این کلاس برای  دیتا بیس اطلاعات بیمه ای شرکت ها ایجاد شده است
class company_insurance_information(models.Model):
    Company_insurance_information = models.ForeignKey(
        general_company_information, blank=True, null=True, related_name='company_insurance_information', verbose_name='نام شرکت / موسسه', on_delete=models.SET_NULL)
    username = models.CharField(
        max_length=100, verbose_name='نام کاربری', blank=True, null=True)
    password = models.CharField(
        max_length=100, verbose_name='رمز عبور', blank=True, null=True)
    name_office_insurance_branch = models.CharField(
        max_length=100, verbose_name='نام شعبه ی بیمه دفتر', blank=True, null=True)
    office_insurance_workshop_code = models.CharField(
        max_length=100, unique=True, verbose_name='کد کارگاهی بیمه دفتر', blank=True, null=True)
    name_factory_insurance_branch = models.CharField(
        max_length=100, verbose_name='نام شعبه ی بیمه کارخانه', blank=True, null=True)
    factory_insurance_workshop_code = models.CharField(
        max_length=100, unique=True, verbose_name='کد کارگاهی بیمه کارخانه', blank=True, null=True)

    
    docs = models.ManyToManyField(
        File,
        blank=True,
        verbose_name='مدارک'
    )

    class Meta:
        verbose_name = 'اطلاعات بیمه ای شرکت'
        verbose_name_plural = 'اطلاعات بیمه ای شرکت ها'

    def __str__(self) -> str:
        try:
            return self.Company_insurance_information.title
        except:
            return 'بدون عنوان'

# این کلاس برای  دیتا بیس اطلاعات مالیاتی شرکت ها ایجاد شده است


class tax_information(models.Model):
    Tax_information = models.ForeignKey(general_company_information, blank=True, null=True,
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

    value_added_information = models.CharField(
        max_length=100, verbose_name='اطلاعات مالیات بر ارزش افزوده', blank=True, null=True)
    username_value_information = models.CharField(
        max_length=100, unique=True, verbose_name='(نام کاربری)', blank=True, null=True)
    password_value_information = models.CharField(
        max_length=100, unique=True, verbose_name='(رمز عبور)', blank=True, null=True)

    quarterly_information = models.CharField(
        max_length=100, verbose_name='اطلاعات مالیات فصلی (TTMS)', blank=True, null=True)
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

    def __str__(self) -> str:
        try:
            return self.Tax_information.title
        except:
            return 'بدون عنوان'
