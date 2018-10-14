from django.shortcuts import render
from .models import Resources

def resources_page(request):
    hosts = Resources.objects.all()
    return render(request, "op/host.html", {"hosts":hosts})
