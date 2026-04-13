from django.shortcuts import render
from django.http import HttpResponse
from .models import Complaint


# 🔹 Homepage (Flask project page)
def home(request):
    return render(request, 'home.html')


# 🔹 Complaint form
def complaint_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        issue = request.POST.get('issue')
        desc = request.POST.get('description')

        # ✅ Flask logic replaced inside Django
        if issue:
            if "no internet" in issue.lower():
                priority = "High"
            elif "slow" in issue.lower():
                priority = "Medium"
            else:
                priority = "Low"
        else:
            priority = "Low"

        # Save to database
        Complaint.objects.create(
            customer_name=name,
            issue_type=issue,
            description=desc,
            status=priority
        )

        return render(request, 'success.html')

    return render(request, 'complaint.html')
