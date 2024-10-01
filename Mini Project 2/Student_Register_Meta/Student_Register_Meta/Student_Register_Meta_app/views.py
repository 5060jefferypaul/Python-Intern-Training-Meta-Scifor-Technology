import os
from django.shortcuts import render, redirect
from .models import itemDetails, teacherDetails


def Home(request):
    return render(request, 'Home.html')


def Student(request):
    return render(request, 'Student Home.html')


def student_details(request):
    if request.method == 'POST':
        stuid = request.POST['student_id']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        aage = request.POST['age']
        dob = request.POST['date_of_birth']
        gen = request.POST['gender']
        quali = request.POST['qualifications']
        image = request.FILES.get('file')
        register = itemDetails(student_id=stuid, first_name=fname, last_name=lname, age=aage, date_of_birth=dob,
                               gender=gen, qualifications=quali, image=image)
        print("Save data...")
        register.save()
        return redirect('student_showpage')


def student_showpage(request):
    showstudents = itemDetails.objects.all()
    return render(request, 'Show Details.html', {'register': showstudents})


def student_editpage(request, pk):
    pr = itemDetails.objects.get(id=pk)
    return render(request, 'Student Edit.html', {'register': pr})


def edit_student_details(request, pk):
    if request.method == 'POST':
        pr = itemDetails.objects.get(id=pk)
        pr.student_id = float(request.POST.get('student_id'))
        pr.first_name = request.POST.get('first_name')
        pr.last_name = request.POST.get('last_name')
        pr.age = float(request.POST.get('age'))
        pr.date_of_birth = (request.POST.get('date_of_birth'))
        pr.gender = request.POST.get('gender')
        pr.qualifications = request.POST.get('qualifications')
        pr.image = request.FILES.get('file')
        pr.save()
        return redirect(student_showpage)
    return render(request, 'Student Edit.html')


def admit_card_student(request, pk):
    admit = itemDetails.objects.get(id=pk)
    return render(request, 'Id Card Student.html', {'reg': admit})


def delete_page_student(request, pk):
    student_details = itemDetails.objects.get(id=pk)
    student_details.delete()
    return redirect('student_showpage')

# def student_editpage(request, pk):
#     pr = itemDetails.objects.get(id=pk)
#     return render(request, 'Student Edit.html', {'register': pr})

# TEACHER


def Teacher(request):
    return render(request, 'Teacher Form.html')


def teacher_details(request):
    if request.method == 'POST':
        teach = request.POST['teacher_id']
        nam = request.POST['nname']
        aage = request.POST['age']
        gen = request.POST['gender']
        posi = request.POST['position']
        pho = request.POST['phone']
        mail = request.POST['email']
        image = request.FILES.get('file')
        register = teacherDetails(teacher_id=teach, nname=nam, age=aage, gender=gen, position=posi, phone=pho,
                                  email=mail, image=image)
        print("Save data...")
        register.save()
        return redirect('teacher_showpage')


def teacher_showpage(request):
    showteachers = teacherDetails.objects.all()
    return render(request, 'Teacher Show Details.html', {'register': showteachers})

def admit_card_teacher(request, pk):
    teach = teacherDetails.objects.get(id=pk)
    return render(request, 'Id Card Teacher.html', {'reg': teach})


def teacher_editpage(request, pk):
    pr = teacherDetails.objects.get(id=pk)
    return render(request, 'Teacher Edit.html', {'register': pr})


def edit_teacher_details(request, pk):
    if request.method == 'POST':
        pr = teacherDetails.objects.get(id=pk)
        pr.teacher_id = float(request.POST.get('teacher_id'))
        pr.nname = request.POST.get('nname')
        pr.age = float(request.POST.get('age'))
        pr.gender = request.POST.get('gender')
        pr.position = request.POST.get('position')
        pr.phone = float(request.POST.get('phone'))
        pr.email = request.POST.get('email')
        pr.image = request.FILES.get('file')
        pr.save()
        return redirect(teacher_showpage)
    return render(request, 'Teacher Edit.html')

def delete_page_teacher(request, pk):
    teacher_details = teacherDetails.objects.get(id=pk)
    teacher_details.delete()
    return redirect('teacher_showpage')

# Create your views here.
