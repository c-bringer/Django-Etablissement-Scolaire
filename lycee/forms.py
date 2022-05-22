from django.forms.models import ModelForm
from .models import Student, Presence, ParticularPresence
from django.forms.widgets import CheckboxSelectMultiple


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = (
            "first_name",
            "last_name",
            "birth_date",
            "email",
            "phone",
            "comments",
            "cursus",
        )


class ParticularCallRollForm(ModelForm):
    class Meta:
        model = ParticularPresence
        fields = (
            "reason",
            "is_missing",
            "date",
            "student"
        )


class CallRollForm(ModelForm):
  class Meta:
    model = Presence
    fields = [
      'date',
      'student'
      ]
    widgets = {
        'student' : CheckboxSelectMultiple()
    }