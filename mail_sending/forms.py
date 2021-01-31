from django import forms
from .models import Contact


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email']
        widgets = {'email': forms.EmailInput(
            attrs={'style': "background-color: rgb(237,237,237);padding-top: 0px;padding-bottom: 0px;width: 100%;height: 100%;padding-left: 15px;padding-right: 15px;", 'class': '"border rounded-0 form-control d-flex d-sm-inline-block d-md-flex d-lg-flex d-xl-flex justify-content-center align-items-center justify-content-md-center justify-content-lg-center justify-content-xl-center"', 'placeholder':"E-mail" }
        )}



class SendMailForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    message = forms.CharField(widget=forms.Textarea,required=False)