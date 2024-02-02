from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels
from django.core.validators import FileExtensionValidator
from Sherkat.models import general_company_information, File 
from django.utils.html import format_html



# Create your models here.

class phone_book(models.Model):
    name_sherkat = models.CharField(
        max_length=100, verbose_name="نام شرکت/موسسه",blank=True, null=True)
    name_phonebook = models.CharField(
        max_length=100, verbose_name="نام",blank=True, null=True)
    family_name_phonebook = models.CharField(
        max_length=100, verbose_name="نام خانوادگی", blank=True, null=True)
    tel_phonebook = models.CharField(
        max_length=11, verbose_name="شماره تلفن ثابت", blank=True, null=True)
    dakheli_phonebook = models.CharField(
        max_length=20, verbose_name="داخلی", blank=True, null=True) 
    mobile_phonebook = models.CharField(
        max_length=11, verbose_name="تلفن همراه", blank=True, null=True)
    semat_phonebook = models.CharField(
        max_length=100, verbose_name="سمت", blank=True, null=True)
    email_phonebook = models.EmailField(
        max_length=254, verbose_name="ایمیل", blank=True, null=True)
    rabet_name_phonebook = models.CharField(
        max_length=100, verbose_name="نام رابط", blank=True, null=True)
    address_phonebook = models.TextField(
        max_length=100, verbose_name="آدرس", blank=True, null=True)
    postal_code_phonebook = models.CharField(
        max_length=20, verbose_name="کد پستی", blank=True, null=True)
    fax_phonebook = models.CharField(
        max_length=11, verbose_name="شماره فکس", blank=True, null=True)
    

    class Meta:
        verbose_name = "دفترچه تلفن"
        verbose_name_plural = "دفترچه تلفن"
        db_table = 'phone_book'
        
    def __str__(self) -> str:
        try:
            return self.name + ' ' + self.family_name
        except:
            return 'بدون عنوان'


class employee_information(models.Model):
    MADRAK_TAHSILY = (
        ('zi', "زیر دیپلم",),
        ('di', 'دیپلم'),
        ('li', 'لیسانس'),
        ('fo', 'فوق لیسانس'),
        ('dr', 'دکترا'),
    )

    NOE_GHARARDAD = (
        ('gh', 'قراردادی'),
        ('py', 'پیمانی'),
        ('da', 'دوامی'),
        ('sa', 'ساعتی'),
        ('di', 'دیگر'),
    )

    MARTIAL_STATUS = (
        ('mo','مجرد'),
        ('ma', 'متاهل'),
        ('sa', 'سایر'),
    )

    SEX = (
        ('f', 'زن'),
        ('m', 'مرد'),
        ('s','سایر'),
    )

    sherkat = models.ForeignKey(general_company_information, null=True,
                                related_name='employees', verbose_name='نام شرکت/موسسه', on_delete=models.SET_NULL)
    name = models.CharField(
        max_length=100, verbose_name="نام", null=True)


    shenasname_file = models.FileField(upload_to='karmandan/shenasname/', blank=True, null=True, verbose_name='بارگذاری شناسنامه',
                                        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])])
    
    cartmeli_file = models.FileField(upload_to='karmandan/melicard/', blank=True, null=True, verbose_name='بارگذاری کارت ملی',
                                        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])])
    
    madrak_file = models.FileField(upload_to='karmandan/madrak/', blank=True, null=True, verbose_name='بارگذاری مدرک تحصیلی',
                                        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])])
    
    gharardad_file = models.FileField(upload_to='karmandan/gharardad/', blank=True, null=True, verbose_name='بارگذاری قرارداد',
                                        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])])
    
    bimeh_file = models.FileField(upload_to='karmandan/bimeh/', blank=True, null=True, verbose_name='بارگذاری مدرک بیمه',
                                        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])])


    # Image field
    profile_photo = models.ImageField(
        upload_to='karmandan/profile/', blank=True, null=True, verbose_name='عکس پروفایل')
    family_name = models.CharField(
        max_length=20, verbose_name="نام خانوادگی",  null=True)
    father_name = models.CharField(
        max_length=20, verbose_name="نام پدر", blank=True, null=True)
    national_code = models.CharField(
        max_length=11, verbose_name="کد ملی",  null=True, unique=True)
    shenasname_code = models.CharField(
        max_length=11, verbose_name="شماره شناسنامه", blank=True, null=True)
    birth_date = jmodels.jDateField(
        verbose_name="تاریخ تولد", blank=True, null=True)
    birth_place = models.CharField(
        max_length=20, verbose_name="محل تولد", blank=True, null=True)
    bimeh_code = models.CharField(
        max_length=11, verbose_name="شماره بیمه", blank=True, null=True)
    tel = models.CharField(
        max_length=12, verbose_name="شماره تلفن ثابت", blank=True, null=True)
    mobile = models.CharField(
        max_length=12, verbose_name="تلفن همراه", blank=True, null=True)
    madrak_tahsili = models.CharField(
        max_length=5, choices=MADRAK_TAHSILY, verbose_name=" مدرک تحصیلی", blank=True, null=True)
    noe_gharardad = models.CharField(
        max_length=5, choices=NOE_GHARARDAD, verbose_name="نوع قرارداد", blank=True, null=True)
    mahale_faliat = models.CharField(
        max_length=20, verbose_name="محل فعالیت", blank=True, null=True)
    semat = models.CharField(
        max_length=20, verbose_name="سمت", blank=True, null=True)
    address = models.TextField(
        max_length=100, verbose_name="آدرس", blank=True, null=True)
    postal_code = models.CharField(
        max_length=20, verbose_name="کد پستی", blank=True, null=True)
    marital_status = models.CharField(
       max_length=5, choices=MARTIAL_STATUS, verbose_name="وضعیت تاهل", blank=True, null=True)
    tedade_farzand = models.CharField(
        max_length=10 , verbose_name="تعداد فرزند", blank=True, null=True)
    start_date = jmodels.jDateField(
        verbose_name="تاریخ شروع به کار", blank=True, null=True)
    end_date_of_work = jmodels.jDateField(
        verbose_name="تاریخ اتمام قرار داد", blank=True, null=True)
    reshte_tahsili = models.CharField(
        max_length=20, verbose_name="رشته تحصیلی", blank=True, null=True)
    check_box = models.BooleanField(
        default=1,verbose_name='دارای فعالیت',blank=True ,null = True)
    sex = models.CharField(
        max_length=2, choices=SEX, verbose_name='جنسیت', null=True)
    
    docs = models.ManyToManyField(
        File,
        blank=True,
        related_name='karmandan',
        verbose_name='مدارک'
    )
        
    class Meta:
        verbose_name = "اطلاعات کارمندان"
        verbose_name_plural = "اطلاعات کارمندان"
        db_table = 'employee_information'

    def __str__(self) -> str:
        try:
            return self.name + ' ' + self.family_name
        except:
            return 'بدون عنوان'

    def image_tag(self):
        try:
            return format_html(f'<img src="{self.profile_photo.url}" width="50" height="50" style="border-radius: 10px; " />')
        except:
            return 'فاقد تصویر'
    image_tag.short_description = 'عکس پروفایل'
