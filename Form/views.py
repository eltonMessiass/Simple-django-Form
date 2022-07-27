from multiprocessing import context
from django.shortcuts import render
from .forms import StudentForm, UniversityForm, CollegeForm
# Create your views here.


def createForm(request):
    form1 = StudentForm(request.POST, request.FILES)
    form2 = UniversityForm(request.POST, request.FILES)
    form3 = CollegeForm(request.POST, request.FILES)

    if request.method == 'POST':
        a_valid = form1.is_valid()
        b_valid = form2.is_valid()
        c_valid = form3.is_valid()

        if a_valid and b_valid and c_valid:
            a = form1.save()
            b = form2.save(commit=False)
            b.foreignKeytoStudentForm = a
            b.save()
            c = form3.save(commit=False)
            c.foreignKeytoUniversityForm = b
            c.save()


    context = {'form1':form1, 'form2':form2, 'form3':form3}
    return render(request, "Form/index.html", context)
    