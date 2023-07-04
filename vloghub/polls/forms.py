from typing import Any
from django import forms
from .models import vlog,ProfileInfor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class VlogForm(forms.ModelForm):
    content = forms.CharField(required=True,
        widget = forms.widgets.Textarea(
            attrs= { 
                "placeholder": "Enter your vlog...",
                "class": "form-control"}
            ),
            label ="",
        )
    class Meta:
        model = vlog
        exclude = ("user","likes")

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username','password1','password2'}
    
    def __init__(self, *args: Any, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class PostProfile(forms.ModelForm):
    class Meta:
        model = ProfileInfor
        fields = {'profile_image','full_name','Email','Phone','Address','Job','About','Company','Country'}
        widgets = {
            'full_name': forms.TextInput(attrs={'class': "form-control"}),
            'Email': forms.TextInput(attrs={'class': "form-control"}),
            'Phone': forms.TextInput(attrs={'class': "form-control"}),
            'Address': forms.TextInput(attrs={'class': "form-control"}),
            'About': forms.Textarea(attrs={'class':"form-control"}),
            'Country': forms.TextInput(attrs={'class': "form-control"}),
            'Company': forms.TextInput(attrs={'class': "form-control"}),
            'Job': forms.TextInput(attrs={'class': "form-control"}),
            'Twitter_Profile': forms.URLInput(attrs={'class': "form-control"}),
            'Facebook_Profile': forms.URLInput(attrs={'class': "input"}),
            'Instagram_Profile': forms.URLInput(attrs={'class': "input"}),
            'Linkedin_Profile': forms.URLInput(attrs={'class': "form-control",'style': 'height: 100px'}),
        }