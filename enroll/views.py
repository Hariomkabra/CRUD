from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# This function will add new items and show all items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # Save form data to the database
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()  # Reset the form after successful submission
    else:
        fm = StudentRegistration()

    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

# This function will update
def update_data(request, id):
    pi = User.objects.get(pk=id)  # Retrieve the user instance outside the if block
    if request.method == "POST":
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')  # Redirect after successful update to prevent resubmission
    else:
        fm = StudentRegistration(instance=pi)  

    return render(request, 'enroll/updatestudent.html', {'form': fm})  # return response

# This function will delete
def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
