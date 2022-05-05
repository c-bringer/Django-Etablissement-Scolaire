from .models import Cursus, Student, Presence
from django.views.generic.edit import CreateView, UpdateView
from .forms import StudentForm, ParticularCallForm
from django.urls import reverse
from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, 'lycee/home.html')


def index(request):
    result_list = Cursus.objects.order_by('name')
    context = {
        'liste': result_list
    }
    return render(request, 'lycee/index.html', context)


def detail(request, cursus_id):
    result_list = Student.objects.order_by('last_name').all().filter(cursus_id=cursus_id)
    result_cursus = Cursus.objects.get(pk=cursus_id)
    context = {
        'liste': result_list,
        'cursus': result_cursus,
    }
    return render(request, 'lycee/detail.html', context)


def detail_student(request, student_id):
    result_list = Student.objects.get(pk=student_id)
    context = {
        'liste': result_list
    }
    return render(request, 'lycee/student/detail_student.html', context)


class StudentEditView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'lycee/student/edit.html'

    def get_success_url(self):
        return reverse('detail_student', args=(self.object.pk,))


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'lycee/student/create.html'

    def get_success_url(self):
        return reverse('detail_student', args=(self.object.pk,))


class ParticularCallCreateView(CreateView):
    model = Presence
    form_class = ParticularCallForm
    template_name = 'lycee/particularcall.html'

    def get_success_url(self):
        return reverse('index')