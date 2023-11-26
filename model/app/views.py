from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
  return render(request, "home.html")

def mediform(request):
  if request.method == 'POST':
    name = request.POST.get("name")
    hospital_name = request.POST.get("hospital_name")
    hospital_no = request.POST.get("hospital_no")
    guardian_name = request.POST.get("guardian_name")
    guardian_no = request.POST.get("guardian_no")
    address = request.POST.get("address")
    MediForm.objects.create(name = name,hospital_name = hospital_name,hospital_no = hospital_no, guardian_name = guardian_name, guardian_no = guardian_no, address = address)
    return render(request, "mediform.html")
  else:
    return render(request, "mediform.html")
  
def medicos(request):
      medical = MediForm.objects.all()
      return render(request, 'medicos.html', {'medical': medical,})