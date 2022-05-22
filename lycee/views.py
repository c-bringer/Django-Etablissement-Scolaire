from .models import Cursus, Student, Presence, ParticularPresence
from django.views.generic.edit import CreateView, UpdateView
from .forms import StudentForm, ParticularCallRollForm, CallRollForm
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


def callview(request):
    Presence_list = Presence.objects.order_by('date')
    ParticularPresence_list = ParticularPresence.objects.order_by('date')
    context = {
        'Presence_list' : Presence_list,
        'ParticularPresence_list': ParticularPresence_list
    }

    return render(request,'lycee/viewcall.html',context)


def detail_callview(request, presence_id):
    Students_abs = Presence.objects.get(pk=presence_id).student.all()
    cursus_id = Presence.objects.get(pk=presence_id).cursus
    Student_pre = Student.objects.filter(cursus = cursus_id)
    for absent in Students_abs:
        Student_pre.exclude(id = absent.id)
    context = {
        'Absent_list' : Students_abs,
        'Present_list' : Student_pre
    }

    return render(request,'lycee/detail_call.html',context)


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


class CallRollCreateView(CreateView):
    model = Presence
    form_class = CallRollForm
    template_name = 'lycee/callroll.html'

    def get_context_data(self, **kwargs):
        context = super(CallRollCreateView, self).get_context_data(**kwargs)
        context['cursus'] = Cursus.objects.get(pk=self.kwargs.get("cursus_id",None))
        return context

    def get_form(self):
        form = super(CallRollCreateView, self).get_form(self.form_class)

        form.instance.cursus = Cursus.objects.get(pk=self.kwargs.get("cursus_id",None))
        form.fields["student"].queryset = Student.objects.filter(cursus=self.kwargs.get("cursus_id",None))
        return form

    def form_valid(self, form):
        form.instance.cursus = Cursus.objects.get(pk=self.kwargs.get("cursus_id",None))
        return super().form_valid(form)


class ParticularCallCreateView(CreateView):
    model = ParticularPresence
    form_class = ParticularCallRollForm
    template_name = 'lycee/particularcall.html'

    def get_success_url(self):
        return reverse('index', args=())
