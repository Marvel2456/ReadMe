from django.shortcuts import render

# Create your views here.

def authorDashboard(request):
    return render(request, 'crm/author_dashboard.html')
