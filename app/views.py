from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def display_student_form(request):
    SFO = Student_Form()
    d = {'SFO': SFO}
    if request.method == 'POST':
        SFD = Student_Form(request.POST)
        if SFD.is_valid():
            ## return HttpResponse('<center><h1>Data is Validate</h1></center>')
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('<center><h1 style="color: blue;">Data is Invalid</h1></center>')

    return render(request, 'display_student_form.html',d)
















    