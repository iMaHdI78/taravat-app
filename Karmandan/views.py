from django.shortcuts import render
from django.http import HttpResponse
from .models import employee_information
from .models import phone_book

# Create your views here.

#این فانکشن برای فایل های کارمندان ایجاد شده
def File(request):
    File_information = File.objects.all()
    context = {
        "File_information": File_information.objects.all()
       
    }
    
#این فانکشن برای دفترچه تلفن ایجاد شده 

def phonebook(request):
    phone_book = phone_book.objects.all()
    context = {
        "phone_book": phone_book.objects.all()
    }

# این فانکشن برای دریافت اطلاعات کاربران است

def Karmandan(request):
    context = {

        "employee_information": [
            {
                "name": "نام",
                "family_name": "نام خانوادگی",
                "father_name": "نام پدر",
                "national_code": "کد ملی",
                "birth_date": "تاریخ تولد",
                "birth_place": "محل تولد",
                "shenasname_code": "شماره شناسنامه",
                "bimeh_code": "شماره بیمه",
                "tel": "شماره تلفن ثابت",
                "mobile": "تلفن همراه",
                "address": "آدرس",
                "postal_code": "کد پستی",
                "madrak_tahsili": "مدرک تحصیلی",
                "mahale_faliat": "محل فعالیت",
                "semat": "سمت",
                "noe_gharardad": "نوع قرارداد",

            }

        ]


    }


from django.views import View
from .models import employee_information

class KarmandView(View):
    def get(self, request):
        context = {
            'karamands': employee_information.objects.all(),
        }
        
        return render(request, 'Karmandan.html', context)