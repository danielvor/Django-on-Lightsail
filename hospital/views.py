from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from hospital.models import Patient
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator


# Function to render the Home Page
def frontend(request):
    return render(request, 'hospital/frontend.html')

# Function to render the Backend Page
cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def backend(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_patient_list = Patient.objects.filter(
            Q(name__icontains=q) | Q(phone=q) | Q(email=q) | Q(age=q) | Q(gender=q) | Q(note=q)
        ).order_by('-id')
    else:
        all_patient_list = Patient.objects.all().order_by('-id')

    paginator = Paginator(all_patient_list, 2)
    page = request.GET.get('page')
    all_patient = paginator.get_page(page)

    return render(request, 'hospital/backend.html', {"patients": all_patient})

# Function to Add patient
cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def add_patient(request):
    if request.method == 'POST':
        if request.POST.get("name") \
            and request.POST.get("phone") \
            and request.POST.get("email") \
            and  request.POST.get("age") \
            and request.POST.get("gender") \
            or request.POST.get("note"):

            patient = Patient()
            patient.name = request.POST.get("name")
            patient.phone = request.POST.get("phone")
            patient.email = request.POST.get("email")
            patient.age = request.POST.get("age")
            patient.gender = request.POST.get("gender")
            patient.note = request.POST.get("note")
            patient.save()
            messages.success(request, "Patient Added successfully !")
            return HttpResponseRedirect('backend')
    else:
        return render(request, "hospital/add.html")


# Function to delete patient
cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def delete_patient(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    patient.delete()
    messages.success(request, "Patient removed Successfully !")
    return HttpResponseRedirect('/hospital/backend/')

# Function to access the patient individually
cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def patient(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    if patient != None:
        return render(request, "hospital/edit.html", {'patient': patient})

# Function to edit patient
cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def edit_patient(request):
    if request.method == 'POST':
        patient = Patient.objects.get(id= request.POST.get('id'))
        if patient != None:

            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()

            messages.success(request, "Patient updated Successfully !")
            return HttpResponseRedirect('/hospital/backend/')