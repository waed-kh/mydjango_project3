from django.shortcuts import render
from .models import Student  # استدعاء الموديل

def index(request):
    students = Student.objects.all()  # جلب كل الطلاب
    return render(request, 'pages/index.html', {'students': students})
