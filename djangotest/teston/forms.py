from django import forms
from teston.models import User
from django.core import validators

# Create your forms here
class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('first_name','last_name','email')
        #fields = '__all__'

class FormName(forms.Form):
    name = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=128)
    verify_email = forms.EmailField(label="Please enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure email match!")
