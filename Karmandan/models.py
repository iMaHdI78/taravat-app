from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels

from Sherkat.models import general_company_information, File

from django.utils.html import format_html






# Create your models here.
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

    sherkat = models.ForeignKey(general_company_information, null=True,
                                related_name='employees', verbose_name='نام شرکت/موسسه', on_delete=models.SET_NULL)
    name = models.CharField(
        max_length=100, verbose_name="نام", null=True)

    # Image field
    profile_photo = models.ImageField(
        upload_to='karmandan/profile/', blank=True, null=True, verbose_name='عکس پروفایل')
    family_name = models.CharField(
        max_length=100, verbose_name="نام خانوادگی",  null=True)
    father_name = models.CharField(
        max_length=100, verbose_name="نام پدر", blank=True, null=True)
    national_code = models.CharField(
        max_length=20, verbose_name="کد ملی",  null=True, unique=True)
    shenasname_code = models.CharField(
        max_length=20, verbose_name="شماره شناسنامه", blank=True, null=True)
    birth_date = jmodels.jDateField(
        max_length=20, verbose_name="تاریخ تولد", blank=True, null=True)
    birth_place = models.CharField(
        max_length=100, verbose_name="محل تولد", blank=True, null=True)
    bimeh_code = models.CharField(
        max_length=11, verbose_name="شماره بیمه", blank=True, null=True)
    tel = models.CharField(
        max_length=20, verbose_name="شماره تلفن ثابت", blank=True, null=True)
    mobile = models.CharField(
        max_length=20, verbose_name="تلفن همراه", blank=True, null=True)
    madrak_tahsili = models.CharField(
        max_length=100, choices=MADRAK_TAHSILY, verbose_name=" مدرک تحصیلی", blank=True, null=True)
    noe_gharardad = models.CharField(
        max_length=15, choices=NOE_GHARARDAD, verbose_name="نوع قرارداد", blank=True, null=True)
    mahale_faliat = models.CharField(
        max_length=100, verbose_name="محل فعالیت", blank=True, null=True)
    semat = models.CharField(
        max_length=100, verbose_name="سمت", blank=True, null=True)
    address = models.TextField(
        max_length=100, verbose_name="آدرس", blank=True, null=True)
    postal_code = models.CharField(
        max_length=20, verbose_name="کد پستی", blank=True, null=True)
    
    docs = models.ManyToManyField(
        File,
        blank=True,
        related_name='karmandan',
        verbose_name='مدارک'
    )

    class Meta:
        verbose_name = "اطلاعات کارمندان"
        verbose_name_plural = "اطلاعات کارمندان"

    def __str__(self) -> str:
        try:
            return self.name + ' ' + self.family_name
        except:
            return 'بدون عنوان'

    def image_tag(self):
        return format_html(f'<img src="{self.profile_photo.url}" width="50" height="50" style="border-radius: 10px; " />')