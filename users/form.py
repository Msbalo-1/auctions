from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name',  'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }




    def __init__(self, *args, **kwargs):
        super(signupForm, self).__init__(*args, **kwargs)

        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})

        # self.fields['title'].widget.attrs.update({'class': 'form-control'})



class accountForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


    def __init__(self, *args, **kwargs):
        super(accountForm, self).__init__(*args, **kwargs)

        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})

