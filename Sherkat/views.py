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

#این فانکشن برای دریافت اطلاعات بیمه ای شرکت ایجاد شده
def bimeh(request):

    context = {
        "company_insurance_information": company_insurance_information.objects.all()
    }
    return render(request, 'bimeh.html', context)

#این فانکشن برای دریافت اطلاعات مالیاتی ایجاد شده
def tax(request):

    context = {
        "tax_information": tax_information.objects.all()
    }
    return render(request, 'maliat.html', context)
