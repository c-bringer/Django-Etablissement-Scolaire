from django.forms.models import ModelForm
from .models import Student, Presence


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


class ParticularCallForm(ModelForm):
    class Meta:
        model = Presence
        fields = (
            "reason",
            "is_missing",
            "date",
            "student"
        )
