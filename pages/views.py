from django.shortcuts import render
from services.models import ServiceCategory

# Create your views here.


def list_service_categories(request):
    service_categories=ServiceCategory.objects.all()
    return render(request, 'pages/index.html',
                  {"service_category_list": service_categories})