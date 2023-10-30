from django import forms
from .models import *
# PURPOSE_CHOICES = [
#     ('Enquiry', 'Enquiry'),
#     ('Place Order', 'Place Order'),
#     ('Return', 'Return'),
# ]
#
MATERIALS_CHOICES = [
    ('Debit Note Book', 'Debit Note Book'),
    ('Pen', 'Pen'),
    ('Exam Papers', 'Exam Papers'),
    # Add more options as needed
]
#
class OrderForm(forms.Form):
    # purpose = forms.ChoiceField(choices=PURPOSE_CHOICES, widget=forms.Select())
    materials = forms.MultipleChoiceField(choices=MATERIALS_CHOICES, widget=forms.CheckboxSelectMultiple())


    def save(self):
        pass





class formCreationForm(forms.ModelForm):
    class Meta:
        model =Form
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).all()
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.all()

