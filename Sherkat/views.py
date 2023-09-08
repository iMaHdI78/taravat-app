from django.shortcuts import render
from django.http import HttpResponse
from .models import general_company_information, company_insurance_information, tax_information


# Create your views here.

# این فانکشن برای دریافت اطلاعات عمومی شرکت ایجاد شده

def home(request):

    context = {
        "general_company_information": general_company_information.objects.all()
    }
    return render(request, "Sherkat/home.html", context)


def bimeh(request):

    context = {
        "company_insurance_information": company_insurance_information.objects.all()
    }
    return render(request, 'bimeh.html', context)


def tax(request):

    context = {
        "tax_information": tax_information.objects.all()
    }
    return render(request, 'maliat.html', context)

# def home(request):
#     context = {

#         "general_company_information": [
#             {
#                 "title": "نام شرکت / موسسه",
#                 "tel": "شماره تماس",
#                 "tel_fax": "شماره فکس",
#                 "postal_code": "کد پستی",
#                 "national_id": "شناسه ملی",
#                 "company_registration_date": "تاریخ ثبت شرکت",
#                 "postal_code_factory": "کد پستی کارخانه",
#                 "company_activity": "فعالیت شرکت",
#                 "type_activity": "نوع شرکت",
#                 "office_address": "آدرس دفتر",
#                 "office_factory": "آدرس کارخانه",
#             }
#         ]
#     }
#     return render(request, 'home.html',  context)

# # این فانکشن برای دریافت اطلاعات بیمه شرکت ایجاد شده


# def bimeh(request):
#     context = {
#         "company_insurance_information": [

#             {
#                 "username": "نام کاربری",
#                 "password": "رمز عبور",
#                 "name_office_insurance_branch": "نام شعبه بیمه دفتر",
#                 "office_insurance_workshop_code": "کد کارگاهی بیمه دفتر",
#                 "name_factory_insurance_branch": "نام شعبه بیمه کارخانه",
#                 "factory_insurance_workshop_code": "کد کارگاهی بیمه کارخانه",

#             }
#         ]
#     }
#     return render(request, 'bimeh.html',  context)

# # این فانکشن برای دریافت اطلاعات مالیات شرکت ایجاد شده


# def maliat(request):
#     context = {
#         "tax_information": [
#             {
#                 "file_number": "شماره پرونده",
#                 "tax_center": "مرکز مالیاتی",
#                 "tax_branch": "حوزه مالیاتی",
#                 "tax_tracking_code": "کد رهگیری مالیاتی",
#                 "tax_address": "آدرس حوزه مالیاتی",

#                 "value_added_information": "مالیات بر ارزش افزوده",
#                 "username_value_information": "نام کاربری",
#                 "password_value_information": "رمز عبور",

#                 "quarterly_information": "مالیات فصلی",
#                 "username_quarterly_information": "نام کاربری",
#                 "password_quarterly_information": "رمز عبور",
#             }

#         ]
#     }
#     return render(request, 'maliat.html',  context)
