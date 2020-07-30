from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):


    #goes into PG Admin
    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'emp_code', 'position', 'image')
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'EMP. Code',
            'image': 'Image'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select" 
        self.fields['emp_code'].required = False
        #self.fields['image'].empty_label = "Insert Image" 