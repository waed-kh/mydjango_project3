from django.shortcuts import render
from datetime import date



def index(request):
    context = {
         "full_name": "Waed Khalid Ahmed",
        "last_name": "Abu Swise",
        "student_id": "2202555813",
        "address": "Gaza",
        "email": "",
        'dob': date(2005, 11, 22), 
        "extra_info":"I graduated from UCAS with a major in Web Design and Development, and I continued my studies here."
    }
    return render(request, "pages/index.html", context)
