from django.shortcuts import render,redirect
from .models import studentdata
def home_page(request):
    students=studentdata.objects.all()
    return render(request,'studentdataapp/homepage.html',{'students':students})

def add_student_view(request):
    return render(request,'studentdataapp/add.html')
def save_data_view(request):
    roll1=request.POST.get('student_roll_number')
    fname=request.POST.get('student_first_name')
    lname=request.POST.get('student_last_name')
    cls=request.POST.get('student_class')
    sec=request.POST.get('student_section')
    telugu=request.POST.get('telugu_marks')
    hindi=request.POST.get('hindi_marks')
    english=request.POST.get('english_marks')
    maths=request.POST.get('mathematics_marks')
    scince=request.POST.get('scince_marks')
    social=request.POST.get('social_marks')
    data=studentdata(
        student_roll_number=roll1,
        student_first_name=fname,
        student_last_name=lname,
        student_class=cls,
        student_section=sec,
        telugu_marks=telugu,
        hindi_marks=hindi,
        english_marks=english,
        mathematics_marks=maths,
        scince_marks=scince,
        social_marks=social
    )
    data.save()
    return redirect('/')


def edit_view(request,id):
    student=studentdata.objects.get(pk=id)
    return render(request,'studentdataapp/edit.html',{"student":student})
def save_edit_data(request,id):
    student=studentdata.objects.get(pk=id)
    student.student_roll_number=request.POST.get('student_roll_number')
    student.student_first_name=request.POST.get('student_first_name')
    student.student_last_name=request.POST.get('student_last_name')
    student.student_class=request.POST.get('student_class')
    student.student_section=request.POST.get('student_section')
    student.telugu_marks=request.POST.get('telugu_marks')
    student.hindi_marks=request.POST.get('hindi_marks')
    student.english_marks=request.POST.get('english_marks')
    student.mathematics_marks=request.POST.get('mathematics_marks')
    student.scince_marks=request.POST.get('scince_marks')
    student.social_marks=request.POST.get('social_marks')
    student.save()
    return redirect('/')


def delete_view(request,id):
    student=studentdata.objects.get(pk=id)
    student.delete()
    return redirect('/')
