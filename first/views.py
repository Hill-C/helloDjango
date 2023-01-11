from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from first.models import Subject, Teacher


def show_subjects(request):
    subjects = Subject.objects.all().order_by('num')
    return render(request, 'subject.html', {'subjects': subjects})


def show_teachers(request):
    try:
        sno = int(request.GET.get('sno'))
        teachers = []
        if sno:
            subject = Subject.objects.only('name').get(num=sno)
            teachers = Teacher.objects.filter(subject=subject).order_by('num')
        return render(request, 'teachers.html',{
            'subject': subject,
            'teachers': teachers
        })
    except (ValueError, Subject.DoesNotExist):
        return redirect('/')