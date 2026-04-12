from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Spider Net 🚀")


import requests
from django.shortcuts import render
from .models import Complaint

def complaint_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        issue = request.POST.get('issue')
        desc = request.POST.get('description')

        # Send data to Flask
        response = requests.post(
            'http://127.0.0.1:5000/analyze',
            json={'issue': issue}
        )

        priority = response.json().get('priority')

        Complaint.objects.create(
            customer_name=name,
            issue_type=issue,
            description=desc,
            status=priority   # 👈 using Flask result
        )

        return render(request, 'success.html')

    return render(request, 'complaint.html')
